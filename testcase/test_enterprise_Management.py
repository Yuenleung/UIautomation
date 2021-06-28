import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.enterprise_Management import qiyeguanli
from public.globalvar import *

log = Log()




class Test_QiyeguanliMethods:
    """企业管理"""
    def setup_class(self):
        driver = Login()
        creatdict()
        set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = qiyeguanli(driver)
        self.User.click('xpath', "//div[contains(text(),'企业管理')]")
        log.info("展开企业管理菜单")

    def test_jingxiaoshangguanli(self):
        self.User.click('xpath', "//li[contains(text(),'经销商管理')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '经销商管理'
            log.info('用例test_jingxiaoshangguanli通过')
        except AssertionError as e:
            log.error(f'用例test_jingxiaoshangguanli不通过:{e}')
            raise

    def test_yuangongguanli(self):
        self.User.click('xpath', "//li[contains(text(),'员工管理')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '员工管理'
            log.info('用例test_yuangongguanli通过')
        except AssertionError as e:
            log.error(f'用例test_yuangongguanli不通过:{e}')
            raise

    def test_mingpianguanli(self):
        self.User.click('xpath', "//li[contains(text(),'名片管理')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '名片管理'
            log.info('用例test_mingpianguanli通过')
        except AssertionError as e:
            log.error(f'用例test_mingpianguanli不通过:{e}')
            raise

    def test_qudaoguanli(self):
        self.User.click('xpath', "//li[contains(text(),'渠道管理')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '渠道管理'
            log.info('用例test_qudaoguanli通过')
        except AssertionError as e:
            log.error(f'用例test_qudaoguanli不通过:{e}')
            raise

    def test_qiyeshipingguanli(self):
        self.User.click('xpath', "//li[contains(text(),'企业视频管理')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '企业视频管理'
            log.info('用例test_qiyeshipingguanli通过')
        except AssertionError as e:
            log.error(f'用例test_qiyeshipingguanli不通过:{e}')
            raise

    def test_zhanneixin(self):
        self.User.click('xpath', "//li[contains(text(),'站内信')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '基本信息'
            log.info('用例zhanneixin通过')
        except AssertionError as e:
            log.error(f'用例test_zhanneixin不通过:{e}')
            raise

if __name__ == '__main__':
    pytest.main(["-s", "test_enterprise_Management.py::Test_QiyeguanliMethods"])
