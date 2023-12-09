import pytest
from selenium import webdriver

from selenium_yonyou.common.base import Base
from selenium_yonyou.page.login import Login
from selenium_yonyou.page.main import Main


class TestLogin:
    def setup(self):
        self.base = Base()
        my_browser = 'chrome'
        self.base.open_browser(my_browser)
        my_url = "https://bip-pre.yonyoucloud.com/"
        self.base.get_url(my_url)
        self.login = Login(self.base.driver)

    @pytest.mark.parametrize("data", [("yycyh95@test1988.com", "DGYLznzz230802!")])
    def test_login_right(self, data):
        # login = Login(self.base.driver)
        self.result = self.login.goto_main(*data).login_assertion()
        assert self.result == True

    @pytest.mark.parametrize("data", [("yycyh96@test1988.com", "DGYLznzz230802!")])
    def test_login_error(self, data):
        self.result = self.login.goto_main(*data).login_assertion()
        assert self.result == False

    def teardown(self):
        self.base.close_driver()
