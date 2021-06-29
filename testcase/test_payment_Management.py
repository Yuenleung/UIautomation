import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.payment_Management import zhifuguanli
from public.globalvar import *

log = Log()


class Test_zhifuguanliMethods:
    """支付管理"""

    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = zhifuguanli(driver)
        self.User.click('xpath', "//div[contains(text(),'支付管理')]")
        log.info("展开支付管理菜单")

    def test_paymentWithdrawal_Management(self):
        self.User.click('xpath', "//li[contains(text(),'货款提现管理')]")
        text = self.User.get_text("class", "section-header")
        try:
            assert text == '资金管理'
            log.info('用例test_paymentWithdrawal_Management通过')
        except AssertionError as e:
            log.error(f'用例test_paymentWithdrawal_Management不通过:{e}')
            raise


    def test_commissionWithdrawal_Management(self):
        self.User.click('xpath', "//li[contains(text(),'佣金提现管理')]")
        text = self.User.get_text("class", "el-tabs__item.is-active")
        try:
            assert text == '提现管理'
            log.info('用例test_commissionWithdrawal_Management通过')
        except AssertionError as e:
            log.error(f'用例test_commissionWithdrawal_Management不通过:{e}')
            raise

    def test_withdrawalRecord(self):
        self.User.click('xpath', "//li[contains(text(),'提现记录')]")
        text = self.User.get_text("class", "el-tabs__item.is-active")
        try:
            assert text == '货款提现'
            log.info('用例test_withdrawalRecord通过')
        except AssertionError as e:
            log.error(f'用例test_withdrawalRecord不通过:{e}')
            raise



if __name__ == '__main__':
    pytest.main(["-s", "test_payment_Management.py"])