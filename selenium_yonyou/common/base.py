import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver


class Base:

    # 封装selenium初始化,获取driver
    def open_browser(self, browser='chrome'):
        self.browser = browser
        try:
            if self.browser == 'chrome':
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
            elif self.browser == 'firefox':
                self.driver = webdriver.Firefox()
                self.driver.maximize_window()
            elif self.browser == 'ie':
                self.driver = webdriver.Ie()
                self.driver.maximize_window()
            else:
                self.driver = webdriver.Edge()
                self.driver.maximize_window()
            time.sleep(2)
            return self.driver
        except:
            print("open browser fail!")
            return None

    # 打开网页
    def get_url(self, my_url):
        self.driver.get(my_url)

    # 关闭浏览器
    def close_driver(self):
        self.driver.close()
        # 获取元素公共方法

    # 登录系统
    def login_common(self, username, password):
        self.driver.switch_to.frame("yonbip_login_id")
        # 输入账号密码，点击登录
        time.sleep(3)
        self.driver.find_element('xpath', "//*[@id=\"username\"]").clear()
        self.driver.find_element('xpath', "//*[@id=\"username\"]").send_keys(username)
        time.sleep(3)
        self.driver.find_element('xpath', "//*[@id=\"password\"]").send_keys(password)
        time.sleep(3)
        self.driver.find_element('xpath', '//*[@id="submit_btn_login"]').click()
        time.sleep(5)

    def get_element(self, loca_method, local_ele):
        self.local_method = loca_method
        self.local_ele = local_ele
        try:
            if self.local_method == "xpath":
                self.my_element = self.driver.find_element(By.XPATH, local_ele)
            elif self.local_method == 'id':
                self.my_element = self.driver.find_element(By.ID, local_ele)
            elif self.local_method == 'name':
                self.my_element = self.driver.find_element(By.NAME, local_ele)
            elif self.local_method == 'class':
                self.my_element = self.driver.find_element(By.CLASS_NAME, local_ele)
            else:
                self.my_element = self.driver.find_element(By.CSS_SELECTOR, local_ele)
        except:
            print("get ele fail!")
            return None
        return self.my_element

    # 判断元素是否存在
    def ele_is_existence(self, local_ele):
        self.ele_len = self.driver.find_elements(By.XPATH, local_ele)
        if len(self.ele_len) != 0:
            return True

        else:
            return False
