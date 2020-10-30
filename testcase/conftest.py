'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-10-29 14:01:45
LastEditors: Penn
LastEditTime: 2020-10-30 18:01:43
'''
import os
import sys
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from page.main import Main
import pytest


@pytest.fixture(scope="session")
def main():
    main = Main()
    yield main
