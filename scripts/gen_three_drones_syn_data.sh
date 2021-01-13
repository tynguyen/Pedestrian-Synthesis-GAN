data_name="fake_imgs/256x256_fla_450"
split_name="train"
data_path="./datasets/${data_name}"
results_dir="datasets"
python3.7 gen_syn_data.py\
   --dataroot ${data_path}\
   --name ${data_name}\
   --resize_or_crop None\
   --model test\
   --phase ${split_name}\
   --results_dir ${results_dir}\
   --which_model_netG unet_128\
   --which_direction BtoA\
   --dataset_mode single\
   --norm batch
