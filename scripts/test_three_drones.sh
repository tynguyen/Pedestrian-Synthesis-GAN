data_name="autel"
data_path="datasets/${data_name}"
python3.7 test.py\
   --dataroot ${data_path}\
   --name ${data_name}\
   --model pix2pix\
   --which_model_netG unet_128\
   --which_direction BtoA\
   --dataset_mode aligned\
   --norm batch
