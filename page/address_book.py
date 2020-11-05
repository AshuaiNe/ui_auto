'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-10-29 12:12:05
LastEditors: Penn
LastEditTime: 2020-11-05 15:18:33
'''
from page.addmember import AddMember
from page.base_page import BasePage


class AddressBook(BasePage):

    def goto_addmember(self):
        self.steps("./data/member.yaml")
        return AddMember(self._driver)
