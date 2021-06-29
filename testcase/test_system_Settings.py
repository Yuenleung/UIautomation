import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.system_Settings import xitongshezhi
from public.globalvar import *

log = Log()


class Test_xitongshezhiMethods:
    """系统设置"""

    def setup_class(self):
        driver = Login()
        creatdict()
        set_value('driver', driver)
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
        text = self.User.get_text("xpath", "//div[@class='widget-app-board-info']/h3")
        try:
            assert text == '您已授权以下小程序给营客智能导购系统'
            log.info('用例test_Authorization_Settings通过')
        except AssertionError as e:
            log.error(f'用例test_Authorization_Settings不通过:{e}')
            raise


if __name__ == '__main__':
    pytest.main(["-s", "test_system_Settings.py::Test_xitongshezhiMethods::test_Authorization_Settings"])