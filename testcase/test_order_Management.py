import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.order_Management import dingdanguanli
from public.globalvar import *

log = Log()




class Test_dingdanguanliMethods:
    """订单管理"""
    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = dingdanguanli(driver)
        self.User.click('xpath', "//div[contains(text(),'订单管理')]")
        log.info("展开订单管理菜单")

    def test_orderList(self):
        self.User.click('xpath', "//li[contains(text(),'订单列表')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '订单列表'
            log.info('用例test_orderList通过')
        except AssertionError as e:
            log.error(f'用例test_orderList不通过:{e}')
            raise

    def test_refundList(self):
        self.User.click('xpath', "//li[contains(text(),'退款申请列表')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '订单编号'
            log.info('用例test_refundList通过')
        except AssertionError as e:
            log.error(f'用例test_refundList不通过:{e}')
            raise

    def test_expresSetup(self):
        self.User.click('xpath', "//li[contains(text(),'快递设置')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '我的快递列表'
            log.info('用例test_expresSetup通过')
        except AssertionError as e:
            log.error(f'用例test_expresSetup不通过:{e}')
            raise

    def test_groupManagement(self):
        self.User.click('xpath', "//li[contains(text(),'拼团管理')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '拼团商品'
            log.info('用例test_groupManagement通过')
        except AssertionError as e:
            log.error(f'用例test_groupManagement不通过:{e}')
            raise

    def test_bargainManagement(self):
        self.User.click('xpath', "//li[contains(text(),'砍价管理')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '发起人昵称'
            log.info('用例test_bargainManagement通过')
        except AssertionError as e:
            log.error(f'用例test_bargainManagement不通过:{e}')
            raise

    def test_seckillManagement(self):
        self.User.click('xpath', "//li[contains(text(),'秒杀管理')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '发起人昵称'
            log.info('用例test_seckillManagement通过')
        except AssertionError as e:
            log.error(f'用例test_seckillManagement不通过:{e}')
            raise

    def test_storesOrder(self):
        self.User.click('xpath', "//li[contains(text(),'门店订单')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '订单编号'
            log.info('用例test_storesOrder通过')
        except AssertionError as e:
            log.error(f'用例test_storesOrder不通过:{e}')
            raise

    def test_printerList(self):
        self.User.click('xpath', "//li[contains(text(),'打印机列表')]")
        text = self.User.get_text("xpath", "//tr/th[2]/div")
        try:
            assert text == '打印机名称'
            log.info('用例test_printerList通过')
        except AssertionError as e:
            log.error(f'用例test_printerList不通过:{e}')
            raise

    def test_addPrinter(self):
        self.User.click('xpath', "//li[contains(text(),'添加打印机')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '添加打印机'
            log.info('用例test_addPrinter通过')
        except AssertionError as e:
            log.error(f'用例test_addPrinter不通过:{e}')
            raise

    def test_printSetup(self):
        self.User.click('xpath', "//li[contains(text(),'打印设置')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '商 城'
            log.info('用例test_printSetup通过')
        except AssertionError as e:
            log.error(f'用例test_printSetup不通过:{e}')
            raise

if __name__ == '__main__':
    pytest.main(["-s", "test_order_Management.py::Test_QiyeguanliMethods"])