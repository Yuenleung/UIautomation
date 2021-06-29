import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.marketing_Promotion import yingxiaotuiguang
from public.globalvar import *

log = Log()




class Test_yingxiaotuiguangMethods:
    """营销推广"""
    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = yingxiaotuiguang(driver)
        self.User.click('xpath', "//div[contains(text(),'营销推广')]")
        log.info("展开营销推广菜单")

    def test_taskManagement(self):
        self.User.click('xpath', "//li[contains(text(),'任务管理')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '任务标题'
            log.info('用例test_taskManagement通过')
        except AssertionError as e:
            log.error(f'用例test_taskManagement不通过:{e}')
            raise

    def test_distributionSetup(self):
        self.User.click('xpath', "//li[contains(text(),'分销设置')]")
        text = self.User.get_text("class", "el-tabs__item.is-active")
        try:
            assert text == '分销设置'
            log.info('用例test_distributionSetup通过')
        except AssertionError as e:
            log.error(f'用例test_distributionSetup不通过:{e}')
            raise

    def test_marketingBag(self):
        self.User.click('xpath', "//li[contains(text(),'营销福袋')]")
        text = self.User.get_text("class", "el-tabs__item.is-active")
        try:
            assert text == '福袋列表'
            log.info('用例test_marketingBag通过')
        except AssertionError as e:
            log.error(f'用例test_marketingBag不通过:{e}')
            raise

    def test_promotionActivity(self):
        self.User.click('xpath', "//li[contains(text(),'推广活动')]")
        text = self.User.get_text("class", "el-tabs__item.is-active")
        try:
            assert text == '推广活动列表'
            log.info('用例test_promotionActivity通过')
        except AssertionError as e:
            log.error(f'用例test_promotionActivity不通过:{e}')
            raise

    def test_enterpriseActivity_management(self):
        self.User.click('xpath', "//li[contains(text(),'企业活动管理')]")
        text = self.User.get_text("class", "section-header")
        try:
            assert text == '企业活动管理'
            log.info('用例test_enterpriseActivity_management通过')
        except AssertionError as e:
            log.error(f'用例test_enterpriseActivity_management不通过:{e}')
            raise

    def test_CouponList(self):
        self.User.click('xpath', "//li[contains(text(),'优惠券列表')]")
        text = self.User.get_text("class", "section-header")
        try:
            assert text == '优惠券列表'
            log.info('用例test_CouponList通过')
        except AssertionError as e:
            log.error(f'用例test_CouponList不通过:{e}')
            raise

    def test_placeOrders_Coupon(self):
        self.User.click('xpath', "//li[contains(text(),'下单赠券')]")
        text = self.User.get_text("class", "el-form-item__label")
        try:
            assert text == '商品名称'
            log.info('用例test_placeOrders_Coupon通过')
        except AssertionError as e:
            log.error(f'用例test_placeOrders_Coupon不通过:{e}')
            raise


if __name__ == '__main__':
    pytest.main(["-s", "test_marketing_Promotion.py::Test_yingxiaotuiguangMethods"])