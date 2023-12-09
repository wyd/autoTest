from selenium import webdriver

from selenium_yonyou.common.base import Base
from selenium_yonyou.page.login import Login
from selenium_yonyou.page.main import Main


class TestRun:
    def setup(self):
        self.base = Base()
        my_browser = 'chrome'
        self.driver = self.base.open_browser(my_browser)
        # self.list_url=["https://bip-pre.yonyoucloud.com/","https://r2-2302-mysqlpatch.yyuap.com"]
        my_url = "https://bip-pre.yonyoucloud.com/"
        self.base.get_url(my_url)

    def test_run(self):
        login = Login(self.base.driver)
        # main = Main(self.driver)
        # main.goto_production_order_list()
        login.goto_main()
        # login.goto_main().goto_production_order_list().goto_add_production_order_page().add_production_order()

    # def teardown(self):
    #     self.base.close_driver()
