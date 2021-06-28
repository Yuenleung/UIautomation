from public.Base import BasePase
from public.browser import open_browser
from public.log import Log
import pytest
from pages.login import Loginpage
from public.readconfig import ReadConfig
log = Log()

"""
class Test_LoginMethod:

    def setup_class(self):
        self.driver=open_browser()
        BasePase(self.driver).implicitly_wait(10)
        return self.driver
    def test_login(self):
        self.User = Loginpage(self.driver)
        self.User.login("nz","admin","admin")
        text=self.User.get_text("xpath","//div[@class='logo']/a/h1")
        try:
            assert "充电桩综合平台" == text
            log.info("断言登录成功")
        except:
            log.error("断言登录失败")
            raise

    #def teardown_class(self,driver):
        #BasePase(driver).quit_browser()
if __name__ == '__main__':
    pytest.main(["-s","test_Login.py"])
"""

def Login():
    read = ReadConfig()
    driver = open_browser()
    User = Loginpage(driver)
    User.implicitly_wait(20)
    User.maximize_window()
    User.login(read.getValue("Account", "phone"), read.getValue("Account", "password"),
               read.getValue("miniProgram", "miniProgramName"))  # 读取配置信息的登录信息
    text = User.get_text("css", ".shop-info")
    try:
        assert text == f'小程序名称：{read.getValue("miniProgram", "miniProgramName")}  小程序二维码'
        log.info("登录成功")
    except:
        log.error("登录失败")
        raise
    return driver

if __name__ == '__main__':
    Login()