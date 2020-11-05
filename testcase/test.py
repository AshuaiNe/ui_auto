'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-10-30 10:13:38
LastEditors: Penn
LastEditTime: 2020-11-05 14:27:44
'''
from pathlib import Path
import os


abspath = os.path.dirname(os.path.abspath(__file__))
path = Path(__file__).parents[0]
print(path)
