
import pytest
import yaml
from selenium import webdriver
from selenium_yonyou.common.base import Base
from selenium_yonyou.page.login import Login
from selenium_yonyou.page.main import Main


class TestLogin:
    def setup(self):
        my_url = "https://bip-pre.yonyoucloud.com/"
        browser = 'chrome'
        self.login = Login()
        self.login.open_browser(browser)
        self.login.get_url(my_url)

    @pytest.mark.parametrize(["username","password"], yaml.safe_load(open("C:\python_workspace\PycharmProjects\pythonProject\selenium_yonyou\data\login.yaml")))
    def test_login_right(self, username,password):
        # login = Login(self.base.driver)
        self.login.login_common(username,password)
        self.result = self.login.goto_main().login_assertion()
        assert self.result == True

    # @pytest.mark.parametrize("data", [("test", "test")])
    # def test_login_error(self, data):
    #     self.login.login_common(*data)
    #     self.result = self.login.goto_main().login_assertion()
    #     assert self.result == False

    def teardown(self):
        self.login.close_driver()

