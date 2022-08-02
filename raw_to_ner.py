import json
import numpy as np
from tqdm import tqdm

original_file_path = "/home/user/xiongdengrui/datasets/duie/duie_train/duie_train_1_spo.json"
destination_file_path = "/home/user/xiongdengrui/datasets/duie/duie_ner_train/duie_ner_train_1_spo.json"

# destination_file = open(file = destination_file_path, mode = "w", encoding = "utf-8")

object_type_num_dict = {}
subject_type_num_dict = {}

object_type_mapping = {'人物': 'Person', 'Text': 'Text', 'Date': 'Date', '国家': 'Country', '学校': 'School', '气候': 'Climate', '奖项': 'Award', 'Number': 'Number', '地点': 'Location', '歌曲': 'Song', 
                       '城市': 'City', '音乐专辑': 'Album', '企业': 'Enterprise', '语言': 'Language', '作品': 'Work'}
subject_type_mapping = {'图书作品': 'Book', '机构': 'Institute', '影视作品': 'Movie', '人物': 'Person', '电视综艺': 'Variety', '行政区': 'AdministrativeDistrict', '企业': 'Enterprise', '娱乐人物': 'EntertainmentPerson', 
                        '文学作品': 'Literature', '学校': 'School', '歌曲': 'Song', '历史人物': 'HistoricalPerson', '景点': 'Sight', '国家': 'Country', '地点': 'Location', '企业/品牌': 'EnterpriseOrBrand', '学科专业': 'Subject'}

# open file, get load_ori(_io.TextIOWrapper type)
with open(original_file_path,'r') as load_ori:
    # read the lines
    for line in load_ori.readlines():
        line_dict = eval(line)
        # predicate_list.append(spo['predicate'])
        object_type = line_dict['spo_list'][0]['object_type']['@value']
        if object_type_mapping[object_type] not in object_type_num_dict:
            object_type_num_dict[object_type_mapping[object_type]] = 1
        else:
            object_type_num_dict[object_type_mapping[object_type]] += 1
        subject_type = line_dict['spo_list'][0]['subject_type']
        if subject_type_mapping[subject_type] not in subject_type_num_dict:
            subject_type_num_dict[subject_type_mapping[subject_type]] = 1
        else:
            subject_type_num_dict[subject_type_mapping[subject_type]] += 1
        object = line_dict['spo_list'][0]['object']['@value']
        subject = line_dict['spo_list'][0]['subject']
        # print(object_type_list, '\n', subject_type_list, '\n', object_list, '\n', subject_list, '\n')
        # print(" ")
        line_dict_ner = {}
        line_dict_ner["text"] = line_dict["text"]
        line_dict_ner["label"] = {}
        line_dict_ner["label"][object_type_mapping[object_type]] = {}
        line_dict_ner["label"][subject_type_mapping[subject_type]] = {}
        line_dict_ner["label"][object_type_mapping[object_type]][object] = [[line_dict["text"].find(object), line_dict["text"].find(object) + len(object) - 1]]   
        line_dict_ner["label"][subject_type_mapping[subject_type]][subject] = [[line_dict["text"].find(subject), line_dict["text"].find(subject) + len(subject) - 1]] 
        # print(line_dict_ner)
        # print(" ")
        # destination_file.write(json.dumps(line_dict_ner, ensure_ascii = False) + "\n")
        
print("object_type_num_dict", object_type_num_dict)
print("subject_type_num_dict", subject_type_num_dict)