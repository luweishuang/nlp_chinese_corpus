# -*- coding: utf-8 -*-

import glob
import json


base_dir = "/path_to_/txt/wiki_zh_2019/*/*"
file_paths = sorted(glob.glob(base_dir))
for input_path in file_paths:
    print("Processing %s", input_path)
    with open(input_path, 'r', encoding='utf8') as file:
        for line in file:
            json_string = json.loads(line.strip())
            text = json_string.get('text', '')
            line_list = text.split()
