import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.page_Layout import yemianpeizhi
from public.globalvar import *

log = Log()


class Test_yemianpeizhiMethods:
    """页面配置"""

    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = yemianpeizhi(driver)
        self.User.click('xpath', "//div[contains(text(),'页面配置')]")
        log.info("展开页面配置菜单")

    def test_pageTemplate(self):
        self.User.click('xpath', "//li[contains(text(),'页面模板')]")
        text = self.User.get_text("class", "my-button.my-button-tpl.my-button-cut")
        try:
            assert text == '我的模板'
            log.info('用例test_pageTemplate通过')
        except AssertionError as e:
            log.error(f'用例test_pageTemplate不通过:{e}')
            raise

    def test_intelligenceForm(self):
        self.User.click('xpath', "//li[contains(text(),'智能表单')]")
        text = self.User.get_text("xpath", "//form[@class='el-form query-form']/div")
        try:
            assert text == '表单名称'
            log.info('用例test_intelligenceForm通过')
        except AssertionError as e:
            log.error(f'用例test_intelligenceForm不通过:{e}')
            raise


if __name__ == '__main__':
    pytest.main(["-s", "test_page_Layout.py"])