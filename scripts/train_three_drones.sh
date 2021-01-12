data_path="datasets/autel"
python3.7 train.py \
   --dataroot ${data_path}\
   --name autel\
   --model pix2pix\
   --which_model_netG unet_128\
   --which_direction BtoA\
   --lambda_A 100\
   --dataset_mode aligned\
   --use_spp\
   --no_lsgan\
   --norm batch
