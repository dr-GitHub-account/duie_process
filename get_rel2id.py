import json

original_file_path = "/home/user/xiongdengrui/datasets/duie/duie_re_train/duie_re_train_1_spo_noWork.json"
destination_file_path = "/home/user/xiongdengrui/datasets/duie/duie_re_train/duie_re_1_spo_noWork_rel2id.json"

destination_file = open(file = destination_file_path, mode = "w", encoding = "utf-8")

i = 0
rel2id = {}

# open file, get load_ori(_io.TextIOWrapper type)
with open(original_file_path,'r') as load_ori:
    # read the lines
    for line in load_ori.readlines():
        line_dict = eval(line)
        if line_dict["relation"] not in rel2id:
            rel2id[line_dict["relation"]] = i
            i += 1

destination_file.write(json.dumps(rel2id, ensure_ascii = False))
        