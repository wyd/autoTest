import time

import pytest
from selenium import webdriver

from selenium_yonyou.page.login import Login
from selenium_yonyou.page.main import Main
from selenium_yonyou.page.production_order.production_order_list import ProductinOrderList


class TestLogin:
    def setup_class(self):
        my_url = "https://bip-pre.yonyoucloud.com/"
        browser = 'chrome'
        self.login = Login()
        self.login.open_browser(browser)
        self.login.get_url(my_url)

    # my_url = "https://bip-pre.yonyoucloud.com/"
    # browser = 'chrome'

    # 打开节点
    @pytest.mark.parametrize("data", [("")])
    def test_open_node(self, data):
        # self.login = Login()
        # self.login.open_browser(TestLogin.browser)
        # self.login.get_url(TestLogin.my_url)
        self.login.login_common(*data)
        self.result = self.login.goto_main().goto_production_order_list().open_order_assertion()
        assert self.result == True

    # 新增订单
    def test_add_order(self):
        self.login.goto_main().goto_production_order_list().production_order_query().add_production_order()
        # assert self.result == True

    def teardown_class(self):
        time.sleep(10)
        self.login.close_driver()

