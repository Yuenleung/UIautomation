import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.system_Settings import xitongshezhi
from public.globalvar import *

log = Log()


class Test_xitongshezhiMethods:
    """系统设置"""

    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = xitongshezhi(driver)
        self.User.click('xpath', "//div[contains(text(),'系统设置')]")
        log.info("展开系统设置菜单")

    def test_miniProgram_setting(self):
        self.User.click('xpath', "//li[contains(text(),'小程序设置')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '小程序设置'
            log.info('用例test_miniProgram_setting通过')
        except AssertionError as e:
            log.error(f'用例test_miniProgram_setting不通过:{e}')
            raise

    def test_Authorization_Settings(self):
        self.User.click('xpath', "//li[contains(text(),'授权配置')]")
        # text = self.User.get_text("xpath", "//div[@class='widget-app-board-info']/h3")
        # try:
        #     assert text == '您已授权以下小程序给营客智能导购系统'
        #     log.info('用例test_Authorization_Settings通过')
        # except AssertionError as e:
        #     log.error(f'用例test_Authorization_Settings不通过:{e}')
        #     raise

    def test_functionSetting(self):
        self.User.click('xpath', "//li[contains(text(),'功能设置')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '底部栏配置'
            log.info('用例test_functionSetting通过')
        except AssertionError as e:
            log.error(f'用例test_functionSetting不通过:{e}')
            raise

    def test_permissions_Management(self):
        self.User.click('xpath', "//li[contains(text(),'权限管理')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '权限管理'
            log.info('用例test_permissions_Management通过')
        except AssertionError as e:
            log.error(f'用例test_permissions_Management不通过:{e}')
            raise

    def test_releaseManagement(self):
        self.User.click('xpath', "//li[contains(text(),'发布管理')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '发布管理'
            log.info('用例test_releaseManagement通过')
        except AssertionError as e:
            log.error(f'用例test_releaseManagement不通过:{e}')
            raise

    def test_wechatDocking(self):
        self.User.click('xpath', "//li[contains(text(),'微信公众号对接')]")
        text = self.User.get_text("css", ".el-tabs__item.is-active")
        try:
            assert text == '公众号配置'
            log.info('用例test_wechatDocking通过')
        except AssertionError as e:
            log.error(f'用例test_wechatDocking不通过:{e}')
            raise

    def test_card_style_Settings(self):
        self.User.click('xpath', "//li[contains(text(),'名片样式设置')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '名片信息'
            log.info('用例test_card_style_Settings通过')
        except AssertionError as e:
            log.error(f'用例test_card_style_Settings不通过:{e}')
            raise

    def test_card_expansion_field(self):
        self.User.click('xpath', "//li[contains(text(),'名片拓展字段')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '名片拓展字'
            log.info('用例test_card_expansion_field通过')
        except AssertionError as e:
            log.error(f'用例test_card_expansion_field不通过:{e}')
            raise


    def test_subscribeNews_Management(self):
        self.User.click('xpath', "//li[contains(text(),'订阅消息管理')]")
        # text = self.User.get_text("css", ".section-header")
        # try:
        #     assert text == '订阅消息管理'
        #     log.info('用例test_card_expansion_field通过')
        # except AssertionError as e:
        #     log.error(f'用例test_card_expansion_field不通过:{e}')
        #     raise


if __name__ == '__main__':
    pytest.main(["-s", "test_system_Settings.py::Test_xitongshezhiMethods"])