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
for input_path in file_paths:
    print("Processing %s", input_path)
    with open(input_path, 'r', encoding='utf8') as file:
        for line in file:
            json_string = json.loads(line.strip())
            text = json_string.get('text', '')
            line_list = text.split()
