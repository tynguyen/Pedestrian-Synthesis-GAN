data_name="autel"
data_path="datasets/${data_name}"
python3.7 train.py \
   --dataroot ${data_path}\
   --name ${data_name}\
   --model pix2pix\
   --which_model_netG unet_128\
   --which_direction BtoA\
   --lambda_A 100\
   --dataset_mode aligned\
   --use_spp\
   --no_lsgan\
   --norm batch
