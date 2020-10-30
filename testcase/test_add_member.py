'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-10-29 12:12:05
LastEditors: Penn
LastEditTime: 2020-10-30 14:47:58
'''
import os
import sys
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)
from page.main import Main
import allure
import pytest


@allure.epic("通讯录")
@allure.feature("添加成员")
class TestAddMember:
    def setup(self):
        self.main = Main()

    @allure.testcase("")  # 测试用例
    @allure.issue("")  # 测试缺陷
    @allure.title("")  # 测试用例标题
    @allure.story("")  # 测试用例故事
    @allure.severity("")  # 用例等级
    @pytest.mark.parametrize("value", ['pengshuai'])
    def test_add_member(self, value):
        with allure.step("点击通讯录"):
            step = self.main.goto_address_book()
        with allure.step("点击添加成员"):
            step1 = step.goto_addmember()
        with allure.step("添加成员"):
            step1.add_member()
        with allure.step("断言是否添加成功"):
            assert step1.get_member(value)
