'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-10-29 12:12:05
LastEditors: Penn
LastEditTime: 2020-10-30 12:00:50
'''
import os
import sys
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        add_menber = self.main.goto_address_book().goto_addmember()
        add_menber.add_member()
        assert add_menber.get_member('pengshuai')
