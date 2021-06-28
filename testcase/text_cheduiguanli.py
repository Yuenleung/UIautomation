import pytest
from public.log import Log
from public.Base import BasePase
from pages.Member_management import Huiyuanguanli
from public.globalvar import *


log=Log()
"""会员管理"""
class Test_CheduiguanliMethods:
    def setup_class(self):
        driver = get_value('driver')
        self.User = Huiyuanguanli(driver)
        self.User.click('xpath', "//*[text()='车队管理']")
        self.User.click('link', "车队管理")

    """添加车队"""
    # @pytest.mark.skip(reason="跳过")
    data = [('自动化测试车队1', '15000000003'), ('自动化测试车队2', '15000000004')]
    @pytest.mark.parametrize('name,telephone', data)
    def test_Huiyuanguanli7(self, name, telephone):
        log.info("------------------添加车队-------------------")
        try:
            self.User.Add_Chedui(name, telephone)
            self.User.Sleep(2)
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("添加%s成功" % name)
        except:
            log.error("添加%s失败" % name)
            self.User.Esc()
            raise