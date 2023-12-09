import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium_yonyou.common.base import Base
from selenium_yonyou.page.main import Main


class Login(Base):
    def goto_main(self):
        return Main(self.driver)

