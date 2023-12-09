import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium_yonyou.common.base import Base
from selenium_yonyou.page.production_order.production_order_list import ProductinOrderList


class Main(Base):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def goto_production_order_list(self):
        # 搜索菜单，打开生产订单节点
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@fieldid="menu_img"]').click()
        time.sleep(2)
        self.caidan_sousuo_ele = self.driver.find_elements(By.XPATH, '//*[@fieldid="nav-domain"]/div/div/div')[0]
        self.caidan_sousuo_ele.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="search-input" and @placeholder="搜索服务名称"]').clear()
        self.driver.find_element(By.XPATH, '//*[@class="search-input" and @placeholder="搜索服务名称"]').send_keys("车间生产订单")
        self.order_caidan_ele = self.driver.find_elements(By.XPATH, '//*[@class="search-result-wrap"]/div/div/div/ul/li'
                                                                    '/span')[0]
        self.order_caidan_ele.click()
        time.sleep(2)
        return ProductinOrderList(self.driver)

    # 判断元素是否存在
    def login_assertion(self):
        try:
            self.index_ele = self.driver.find_element(By.XPATH, '//*[@class="homePage"]')
            return True
        except:
            return False
