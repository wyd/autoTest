import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium_yonyou.common.base import Base
from selenium_yonyou.page.production_order.add_production_order_page import AddProductionOrderPage


class ProductinOrderList(Base):
    def __init__(self, driver: WebDriver):
        super().__init__()
        self.driver = driver
        self.driver.implicitly_wait(5)

    def production_order_query(self):
        time.sleep(2)
        # 点击重置
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|reset"]').click()
        time.sleep(3)
        # 输入工厂信息
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|org_id_canzhaoSingle"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@fieldid="bd_factoryorg|inputSearch"]').send_keys("机加车间230608")
        self.driver.find_element(By.XPATH, '//*[@fieldid="bd_factoryorg|inputSearch_sousuo"]').click()
        self.factoryorg_radio_xpath = '//*[@fieldid="bd_factoryorg|CheckBox|0"]/span[@class="custom-radio ' \
                                      'custom-radio-unchecked"] '
        if self.ele_is_existence(self.factoryorg_radio_xpath):
            print("没有选中")
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@fieldid="bd_factoryorg|code|0textCol|content"]').click()
            self.driver.find_element(By.XPATH, '//*[@fieldid="bd_factoryorg|ok"]').click()
        else:
            print("选中了 ")
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@fieldid="bd_factoryorg|ok"]').click()
        time.sleep(3)
        # 输入部门信息
        self.driver.find_element(By.XPATH,
                                 '//*[@fieldid="wjmd_prodOrderList|production_department_id_canzhaoicon_icon"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@fieldid="bd_adminorgsharetreeref|children|searchInput"]').send_keys(
            "wjmd-dept-230608")
        self.driver.find_element(By.XPATH,
                                 '//*[@fieldid="bd_adminorgsharetreeref|children|searchInput_search"]').click()
        self.dept_radio_xpath = '//*[@fieldid="bd_adminorgsharetreeref|children|tree_tree_tree_checkbox_wjmd-dept-230608" and @class="wui-tree-checkbox"]'
        if self.ele_is_existence(self.dept_radio_xpath):
            time.sleep(3)
            self.driver.find_element(By.XPATH,
                                     '//*[@fieldid="bd_adminorgsharetreeref|children|tree_tree_tree_title_wjmd-dept-230608"]/span/span[@title="wjmd-dept-230608 生产部门230608"]').click()
            self.driver.find_element(By.XPATH, '//*[@fieldid="bd_adminorgsharetreeref|ok"]').click()
        else:
            print("选中了 ")
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@fieldid="bd_adminorgsharetreeref|ok"]').click()
        # 输入生产订单编码
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|code"]').clear()
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|code"]').send_keys("MEMO231120002_UI")
        time.sleep(3)
        # 展开/折叠按钮操作
        self.expand_btn_ele = '//*[@fieldid="wjmd_prodOrderList|more-xiangxia-copy_icon"]'
        if self.ele_is_existence(self.expand_btn_ele):
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|more-xiangxia-copy_icon"]').click()
            # 输入物料信息
            self.driver.find_element(By.XPATH,
                                     '//*[@fieldid="wjmd_prodOrderList|material_id_canzhaoicon_icon"]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code"]').clear()
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code"]').send_keys("material_code001")
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|search_icon"]').click()
            self.material_result_ele = '//*[@fieldid="productref|CheckBox|0" and @class="wui-checkbox is-checked wui-checkbox-primary"]'
            if self.ele_is_existence(self.material_result_ele):
                self.driver.find_element(By.XPATH, '//*[@fieldid="productref|ok"]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|search_icon"]').click()
            else:
                self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code|0textCol|content"]').click()
                self.driver.find_element(By.XPATH, '//*[@fieldid="productref|ok"]').click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|search_icon"]').click()

        else:
            # 输入物料信息
            self.driver.find_element(By.XPATH,
                                     '//*[@fieldid="wjmd_prodOrderList|material_id_canzhaoicon_icon"]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code"]').clear()
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code"]').send_keys("material_code001")
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|search_icon"]').click()
            self.material_result_ele = '//*[@fieldid="productref|CheckBox|0" and @class="wui-checkbox is-checked wui-checkbox-primary"]'
            if self.ele_is_existence(self.material_result_ele):
                self.driver.find_element(By.XPATH, '//*[@fieldid="productref|ok"]').click()
                time.sleep(3)
                # self.driver.find_element(By.XPATH,'//*[@fieldid="wjmd_prodOrderList|search_icon"]').click()
            else:
                self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code|0textCol|content"]').click()
                self.driver.find_element(By.XPATH, '//*[@fieldid="productref|ok"]').click()
                time.sleep(3)
                # self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|search_icon"]').click()
        # 点击查询按钮
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|search_icon"]').click()
        time.sleep(3)
        # self.result = '//*[@fieldid="wjmd_prodOrderList|table"]/div/span[@class="no-data-txt"]'
        self.results = self.driver.find_elements(By.XPATH,
                                                 '//*[@fieldid="wjmd_prodOrderList|table"]/div/span[@class="no-data-txt"]')
        # self.result = self.driver.find_element(By.XPATH,
        #                                        '//*[@fieldid="wjmd_prodOrderList|table"]/div/span[@class="no-data-txt"]')
        # print("query_result的text：" + self.result.text)
        if (len(self.results) != 0):
            # if self.result.text == '搜索无结果':
            return AddProductionOrderPage(self.driver)
        else:
            return AddProductionOrderPage(self.driver)

    # def goto_add_production_order_page(self):
    #
    #     return AddProductionOrderPage(self.driver)

    def open_order_assertion(self):
        try:
            self.index_ele = self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|btnAdd_icon"]')
            return True
        except:
            return False
