'''
Description:  
Version: 1.0
Author: Penn
Date: 2020-05-19 20:06:04
LastEditors: Penn
LastEditTime: 2020-12-01 15:10:43
'''
import inspect
import json
import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from other.base_logging import Loggers


# 二次封装一下driver相关内容
class BasePage:
    _base_url = ""
    _driver = None
    _params = {}
    _log = Loggers(level="info")

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(5)
            # self._driver.maximize_window()
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
            self._log.logger.info(f'单元素查找：self._driver.find_element({locator})元组')
        else:
            element = self._driver.find_element(locator, value)
            self._log.logger.info(f'单元素查找：self._driver.find_element({locator}, {value})')
        return element

    def finds(self, locator, value: str = None):
        element: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
            self._log.logger.info(f'多元素查找：self._driver.find_elements({locator})：元组')
        else:
            elements = self._driver.find_elements(locator, value)
            self._log.logger.info(f'多元素查找：self._driver.find_elements({locator}, {value})')
        return elements

    def wait_for_click(self, locator, time=10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_elem(self, conditions, time=10):
        # 显示等待
        '''
        sleep(3)直接等待
        self,driver.implicitly_wait(3)隐式等待，轮询查找元素，直到超时
        WebDriverWait(self.driver, time).until()
        '''
        return WebDriverWait(self._driver, time).until(lambda element: self.find(conditions), message='element not found')

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace(f'${{{key}}}', value)
        steps = json.loads(raw)
        try:
            for step in steps:
                if "action" in step.keys():
                    action = step["action"]
                if action == "count":
                    elements: list = self.finds(step["by"], step["locator"])
                    return elements
                element = self.find(step["by"], step["locator"])
                if action == "click":
                    element.click()
                elif action == "send_keys":
                    element.send_keys(step["value"])
                elif action == "text":
                    element: WebElement = element.text
                    return element
                elif action == "attribute":
                    element = element.get_attribute(step["value"])
                    return element
                elif action == "wait":
                    tuple_conditions = (step["by"], step["locator"])
                    element = self.wait_for_elem(tuple_conditions)
                    action_angin = step['action_angin']
                    if action_angin == "click":
                        element.click()
                    elif action == "text":
                        element = element.text
                        return element
        except NoSuchElementException:
            self._log.logger.info(NoSuchElementException)
            raise EOFError
