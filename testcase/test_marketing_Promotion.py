import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.marketing_Promotion import yingxiaotuiguang
from public.globalvar import *

log = Log()




class Test_yingxiaotuiguangMethods:
    """营销推广"""
    def setup_class(self):
        driver = Login()
        creatdict()
        set_value('driver', driver)
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
        text = self.User.get_text("xpath", "//*[@id=’app‘]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]")
        try:
            assert text == '分销设置'
            log.info('用例test_distributionSetup通过')
        except AssertionError as e:
            log.error(f'用例test_distributionSetup不通过:{e}')
            raise

if __name__ == '__main__':
    pytest.main(["-s", "test_marketing_Promotion.py::Test_yingxiaotuiguangMethods::test_distributionSetup"])