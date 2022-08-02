import json
import numpy as np
from tqdm import tqdm

original_file_path = "/home/user/xiongdengrui/datasets/duie/duie_train/duie_train_1_spo.json"
destination_file_path = "/home/user/xiongdengrui/datasets/duie/duie_re_train/duie_re_train_1_spo.json"

destination_file = open(file = destination_file_path, mode = "w", encoding = "utf-8")

# open file, get load_ori(_io.TextIOWrapper type)
with open(original_file_path,'r') as load_ori:
    # read the lines
    for line in load_ori.readlines():
        line_dict = eval(line)
        token = list(line_dict["text"])
        h_name = line_dict["spo_list"][0]["subject"]
        h_pos = [line_dict["text"].find(h_name), line_dict["text"].find(h_name) + len(h_name) - 1]
        t_name = line_dict["spo_list"][0]["object"]["@value"]
        t_pos = [line_dict["text"].find(t_name), line_dict["text"].find(t_name) + len(t_name) - 1]
        relation = line_dict["spo_list"][0]["predicate"]
        # print(h_name, h_pos, t_name, t_pos, relation)
        line_dict_re = {}
        line_dict_re["token"] = token
        line_dict_re["h"] = {"name": h_name, "pos": h_pos}
        line_dict_re["t"] = {"name": t_name, "pos": t_pos}
        line_dict_re["relation"] = relation
        destination_file.write(json.dumps(line_dict_re, ensure_ascii = False) + "\n")