data_path="datasets/autel"
python3.7 test.py\
   --dataroot ${data_path}\
   --name autel\
   --model pix2pix\
   --which_model_netG unet_128\
   --which_direction BtoA\
   --dataset_mode aligned\
   --norm batch
