'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-10-29 14:01:45
LastEditors: Penn
LastEditTime: 2020-10-29 14:36:56
'''
import os
import sys
import yaml
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

with open("data/main.yaml", encoding="utf-8") as f:
        steps = yaml.safe_load(f)["goto_address_book"]
print(steps)
