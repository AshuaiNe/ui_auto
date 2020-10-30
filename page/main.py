'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-05-21 19:49:43
LastEditors: Penn
LastEditTime: 2020-10-30 17:46:09
'''
from page.address_book import AddressBook
from page.base_page import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_address_book(self):
        self.steps("../data/main.yaml")
        # self.find(By.ID, "menu_contacts").click()
        return AddressBook(self._driver)
