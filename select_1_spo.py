import json
import numpy as np
from tqdm import tqdm
import os

original_file_path = "/home/user/xiongdengrui/datasets/duie/duie_train/duie_train.json"
destination_file_path = "/home/user/xiongdengrui/datasets/duie/duie_train/duie_train_1_spo.json"

# if not os.path.exists(destination_file_path):
#     os.mkdir()

destination_file = open(file = destination_file_path, mode = "w", encoding = "utf-8")

# open file, get load_ori(_io.TextIOWrapper type)
with open(original_file_path,'r') as load_ori:
    # read the lines
    for line in load_ori.readlines():
        line_dict = eval(line)
        if len(line_dict['spo_list']) != 1:
            continue
        destination_file.write(json.dumps(line_dict, ensure_ascii = False) + "\n")
        