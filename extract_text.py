import json
import numpy as np
from tqdm import tqdm

original_file_path = "/home/user/xiongdengrui/datasets/duie/duie_ner_train/duie_ner_train_1_spo_noWork.json"
destination_file_path = "/home/user/xiongdengrui/datasets/duie/duie_ner_train/duie_ner_train_1_spo_noWork_text.txt"

destination_file = open(destination_file_path, 'w')

# open file, get load_ori(_io.TextIOWrapper type)
with open(original_file_path,'r') as load_ori:
    # read the lines
    for line in load_ori.readlines():
        line_dict = eval(line)
        text = line_dict["text"]
        destination_file.writelines(text)
        destination_file.write('\n')
destination_file.close()