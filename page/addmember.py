'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-05-19 20:29:58
LastEditors: Penn
LastEditTime: 2020-11-05 15:19:00
'''
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        self.steps("./data/add_member.yaml")
        return self

    def update_page(self):
        content_page: str = self.steps("./data/member.yaml")
        if content_page:
            return [int(_) for _ in content_page.split('/', 1)]
        else:
            return [1, 1]

    def next_page(self):
        self.steps("./data/member.yaml")

    def get_member(self, value):
        self.wait_for_click((By.CSS_SELECTOR, ".ww_checkbox"))
        cur_page, total_page = self.update_page()
        # 1/10
        while True:
            # 先执行条件判断，最后执行更新
            elements = self.steps("./data/member.yaml")
            for element in elements:
                if value == element.get_attribute("title"):
                    return True
            if cur_page == total_page:
                return False
            self.next_page()
            cur_page = self.update_page()[0]
