import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.customer_Management import kehuguanli
from public.globalvar import *

log = Log()


class Test_KehuguanliMethods:
    """客户管理"""

    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = kehuguanli(driver)
        self.User.click('xpath', "//div[contains(text(),'客户管理')]")
        log.info("展开客户管理菜单")

    def test_kehushuju(self):
        self.User.click('xpath', "//li[contains(text(),'客户数据')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '客户资源'
            log.info('用例test_kehushuju通过')
        except AssertionError as e:
            log.error(f'用例test_kehushuju不通过:{e}')
            raise

    def test_weixinyonghu(self):
        self.User.click('xpath', "//li[contains(text(),'微信用户')]")
        text = self.User.get_text("xpath", "//form[@class='el-form query-form']/div[1]/label")
        try:
            assert text == '微信昵称'
            log.info('用例test_weixinyonghu通过')
        except AssertionError as e:
            log.error(f'用例test_weixinyonghu不通过:{e}')
            raise

    def test_gonghaikehu(self):
        self.User.click('xpath', "//li[contains(text(),'公海客户')]")
        text = self.User.get_text("class", "el-tabs__item.is-active")
        try:
            assert text == '未分配'
            log.info('用例test_gonghaikehu通过')
        except AssertionError as e:
            log.error(f'用例test_gonghaikehu不通过:{e}')
            raise


if __name__ == '__main__':
    pytest.main(["-s", "test_customer_Management.py::Test_KehuguanliMethods"])
