import os.path
import random
import torchvision.transforms as transforms
import torch
from data.base_dataset import BaseDataset
from data.image_folder import make_dataset
from PIL import Image
import json
import pdb

class AlignedDataset(BaseDataset):
    """
    *Params:
        opt.loadSize: 286 - scale raw input image to this size
        opt.fineSize: 256 - then crop such image to this size 
    """
    def initialize(self, opt):
        self.opt = opt
        self.root = opt.dataroot
        self.dir_AB = os.path.join(opt.dataroot, 'images', opt.phase)
        self.dir_bbox = os.path.join(opt.dataroot, 'bbox', opt.phase)

        #self.AB_paths, self.bbox_paths = sorted(make_dataset(self.dir_AB, self.dir_bbox))
        self.AB_paths, self.bbox_paths = make_dataset(self.dir_AB, self.dir_bbox)
        self.AB_paths = sorted(self.AB_paths)
        self.bbox_paths = sorted(self.bbox_paths)

        assert(opt.resize_or_crop == 'resize_and_crop')

        transform_list = [transforms.ToTensor(),
                          transforms.Normalize((0.5, 0.5, 0.5),
                                               (0.5, 0.5, 0.5))]

        self.transform = transforms.Compose(transform_list)

    def __getitem__(self, index):
        AB_path = self.AB_paths[index]
        #print(AB_path)
        bbox_path = self.bbox_paths[index]
        #print(bbox_path)
        # Horizontally attach two images
        w_total = self.opt.loadSize * 2
        w = int(w_total / 2)
        h = self.opt.loadSize
        w_offset = random.randint(0, max(0, w - self.opt.fineSize - 1))
        h_offset = random.randint(0, max(0, h - self.opt.fineSize - 1))

        bbox = json.load(open(bbox_path))
        #print(f"{__file__}: Bbox:\n {bbox}")
        #print(f"{__file__}: h_offset: {h_offset}, w_offset: {w_offset}")

        AB = Image.open(AB_path).convert('RGB')
        AB = self.transform(AB)
        A = AB[:, :self.opt.fineSize,
           :self.opt.fineSize]
        B = AB[:, :self.opt.fineSize,
            self.opt.fineSize:2*self.opt.fineSize]
        # Return bbox in the format: x1, y1, x2, y2
        bbox = [bbox['x1'], bbox['y1'], bbox['x2'], bbox['y2']]        
        
        # Horizontally flip
        if (not self.opt.no_flip) and random.random() < 0.5:
            idx = [i for i in range(A.size(2) - 1, -1, -1)]
            idx = torch.LongTensor(idx)
            A = A.index_select(2, idx)
            B = B.index_select(2, idx)
            #print(f"A size: {A.shape}, A2: {A.size(2)}")
            bbox = [A.size(2)-bbox[2], bbox[1], A.size(2) - bbox[0], bbox[3]]
        return {'A': A, 'B': B, 'bbox': bbox,
                'A_paths': AB_path, 'B_paths': AB_path}

    def __len__(self):
        return len(self.AB_paths)

    def name(self):
        return 'AlignedDataset'
