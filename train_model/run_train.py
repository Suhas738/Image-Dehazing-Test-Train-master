import os
from test import test

no_of_epochs = input('No of epochs : ')
model_name = input("Model name : ")

os.system("python3 train.py --epochs " + no_of_epochs + " \
                 --net_name " + model_name + " \
                 --lr 1e-4 \
                 --use_gpu true \
                 --gpu 3 \
                 --ori_data_path train/ori/ \
                 --haze_data_path train/haze/ \
                 --val_ori_data_path val/ori/ \
                 --val_haze_data_path val/haze/ \
                 --num_workers 2 \
                 --batch_size 8 \
                 --val_batch_size 16 \
                 --print_gap 500 \
                 --model_dir model/ \
                 --log_dir logs \
                 --sample_output_folder samples")

test(model_name)