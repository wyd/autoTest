import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium_yonyou.common.base import Base


class AddProductionOrderPage(Base):
    def __init__(self, driver: WebDriver):
        super().__init__()
        self.driver = driver
        self.driver.implicitly_wait(5)

    def add_production_order(self):
        # 点击新增按钮
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrderList|btnAdd_icon"]').click()
        time.sleep(5)
        # 输入工厂信息
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|org_id_name_canzhaoSingle"]').click()
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
                                 '//*[@fieldid="wjmd_prodOrder|production_department_id_name_canzhaoSingle"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@fieldid="bd_adminorgsharetreeref|children|searchInput"]').send_keys(
            "wjmd-dept-230608")
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 '//*[@fieldid="bd_adminorgsharetreeref|children|searchInput_search"]').click()
        # self.dept_radio_xpath = '//*[@fieldid="bd_adminorgsharetreeref|children|tree_tree_tree_checkbox_wjmd-dept-230608" and @class="wui-tree-checkbox"]'
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 '//*[@fieldid="bd_adminorgsharetreeref|children|tree_tree_tree_title_wjmd-dept-230608"]/span/span[@title="wjmd-dept-230608 生产部门230608"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@fieldid="bd_adminorgsharetreeref|ok"]').click()

        # 输入生产订单编码
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|code"]').clear()
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|code"]').send_keys("MEMO231120002_UI")
        time.sleep(3)

        # 输入物料信息
        self.driver.find_element(By.XPATH,
                                 '//*[@fieldid="wjmd_prodOrder|material_id_code_canzhaoSingle"]').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code"]').clear()
        self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code"]').send_keys("material_code001")
        self.driver.find_element(By.XPATH, '//*[@fieldid="productref|search_icon"]').click()
        self.material_result_ele = '//*[@fieldid="productref|CheckBox|0" and @class="wui-checkbox is-checked wui-checkbox-primary"]'
        if self.ele_is_existence(self.material_result_ele):
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|ok"]').click()
            time.sleep(3)
        else:
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|code|0textCol|content"]').click()
            self.driver.find_element(By.XPATH, '//*[@fieldid="productref|ok"]').click()
            time.sleep(3)

        # 输入工艺清单信息
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|route_id_version_canzhaoSingle"]').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@fieldid="dfm_route_ref|inputSearch"]').clear()
        self.driver.find_element(By.XPATH, '//*[@fieldid="dfm_route_ref|inputSearch"]').send_keys("wjmd_bop_code0001")
        self.driver.find_element(By.XPATH, '//*[@fieldid="dfm_route_ref|inputSearch_sousuo"]').click()
        self.route_result_ele = '//*[@fieldid="dfm_route_ref|CheckBox|0"]/span[@class="custom-radio custom-radio-checked"]'
        if self.ele_is_existence(self.route_result_ele):
            self.driver.find_element(By.XPATH, '//*[@fieldid="dfm_route_ref|ok"]').click()
            time.sleep(3)
        else:
            self.driver.find_element(By.XPATH, '//*[@fieldid="dfm_route_ref|name|0textCol|content"]').click()
            self.driver.find_element(By.XPATH, '//*[@fieldid="dfm_route_ref|ok"]').click()
            time.sleep(3)

        # 输入计划生产件数
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|quantity"]').clear()
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|quantity"]').send_keys('10')

        # 输入时间信息
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|start_date_suffix"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|start_date-now"]').click()
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|finish_date_suffix"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|finish_date-now"]').click()
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|delivery_date_suffix"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|delivery_date_footer_today_btn"]').click()

        # 保存
        self.driver.find_element(By.XPATH, '//*[@fieldid="wjmd_prodOrder|btnSave"]').click()


