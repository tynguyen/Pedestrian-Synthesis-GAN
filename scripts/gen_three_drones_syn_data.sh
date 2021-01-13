data_name="fake_imgs/256x256_autel"
split_name="test"
data_path="./datasets/${data_name}"
results_dir="datasets"
python3.7 gen_syn_data.py\
   --dataroot ${data_path}\
   --name ${data_name}\
   --model test\
   --phase ${split_name}\
   --results_dir ${results_dir}\
   --which_model_netG unet_128\
   --which_direction BtoA\
   --dataset_mode single\
   --norm batch
