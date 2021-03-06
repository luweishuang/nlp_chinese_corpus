# -*- coding: utf-8 -*-
import os
import glob
import json

base_dir = "/path_to_/wiki_zh_2019"
for sub_folder in os.listdir(base_dir):
    sub_folder_path = os.path.join(base_dir, sub_folder)
    for file in os.listdir(sub_folder_path):
        cur_file = os.path.join(sub_folder_path, file)
        if os.path.exists(cur_file):
            cur_file_saved = sub_folder_path + "_" + file + ".json"
            os.system("mv %s %s" % (cur_file, cur_file_saved))
            
            
base_dir = "/path_to_txt/*/*"
file_paths = sorted(glob.glob(base_dir))
all_text_list = []
for input_path in file_paths:
    print("Processing %s", input_path)
    with open(input_path, 'r', encoding='utf8') as file:
        for line in file:
            json_string = json.loads(line.strip())
            text = json_string.get('text', '')
            cur_string = "。".join(text.split())
            all_text_list.append(cur_string)

save_txt = os.path.dirname(base_dir) + ".txt"
with open(save_txt, "w") as fw:
    for cur_line in all_text_list:
        fw.write(cur_line + "\n")

'''
# ------------------ wiki_zh_2019 ----------------------
            text = json_string.get('text', '')
            # line_list = text.split()
            # all_text_list.extend(line_list)
            cur_string = "。".join(text.split())
            all_text_list.append(cur_string)

# --------------- webtext2019zh  new2016zh --------------------
            all_text_list.append(json_string.get('title', ''))
            all_text_list.append(json_string.get('desc', ''))
            line_list = json_string.get('content', '').split()
            all_text_list.extend(line_list)
            
# ------------------ translation2019zh --------------------
            all_text_list.append(json_string.get('chinese', ''))

# ------------------ baike2018qa --------------------
            l1 = ",".join(json_string.get('title', '').split())
            l2 = ",".join(json_string.get('answer', '').split())
            cur_string = l1 + ". " + l2
            all_text_list.append(cur_string)
'''
