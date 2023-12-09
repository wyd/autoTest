import time

import pytest
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

    @pytest.mark.parametrize("data", [("yycyh95@test1988.com", "DGYLznzz230802!")])
    def test_login_right(self, data):
        self.login.login_common(*data)
        self.login.goto_main().goto_production_order_list().production_order_query().add_production_order()
        # self.result = self.login.goto_main(*data).goto_production_order_list().production_order_query()
        # assert self.result == True

    def teardown(self):
        time.sleep(10)
        self.login.close_driver()
        # pass
