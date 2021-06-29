import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.data_Analysis import shujufenxi
from public.globalvar import *

log = Log()


class Test_shujufenxiMethods:
    """数据分析"""

    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = shujufenxi(driver)
        self.User.click('xpath', "//div[contains(text(),'数据分析')]")
        log.info("展开数据分析菜单")

    def test_profileData(self):
        self.User.click('xpath', "//li[contains(text(),'数据概况')]")
        text = self.User.get_text("xpath", "//div[@class='distance']/h4")
        try:
            assert text == '昨日概况'
            log.info('用例test_profileData通过')
        except AssertionError as e:
            log.error(f'用例test_profileData不通过:{e}')
            raise

    def test_accessAnalysis(self):
        self.User.click('xpath', "//li[contains(text(),'访问分析')]")
        text = self.User.get_text("xpath", "//div[@class='distance']/div[2]/div[2]")
        try:
            assert text == '粒度'
            log.info('用例test_accessAnalysis通过')
        except AssertionError as e:
            log.error(f'用例test_accessAnalysis不通过:{e}')
            raise

    def test_userPortrait(self):
        self.User.click('xpath', "//li[contains(text(),'用户画像')]")
        text = self.User.get_text("xpath", "//div[@class='distance']/div/h4")
        try:
            assert text == '性别及年龄分布'
            log.info('用例test_userPortrait通过')
        except AssertionError as e:
            log.error(f'用例test_userPortrait不通过:{e}')
            raise

    def test_cardData(self):
        self.User.click('xpath', "//li[contains(text(),'名片日客数据')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '数据报表'
            log.info('用例test_cardData通过')
        except AssertionError as e:
            log.error(f'用例test_cardData不通过:{e}')
            raise


if __name__ == '__main__':
    pytest.main(["-s", "test_data_Analysis.py::Test_shujufenxiMethods"])