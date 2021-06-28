import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.content_Management import neirongguanli
from public.globalvar import *

log = Log()




class Test_neirongguanliMethods:
    """内容管理"""
    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = neirongguanli(driver)
        self.User.click('xpath', "//div[contains(text(),'内容管理')]")
        log.info("展开内容管理菜单")

    def test_lunbopeizhi(self):
        self.User.click('xpath', "//li[contains(text(),'轮播配置')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '入口图片'
            log.info('用例test_lunbopeizhi通过')
        except AssertionError as e:
            log.error(f'用例test_lunbopeizhi不通过:{e}')
            raise

    def test_marketingPoster(self):
        self.User.click('xpath', "//li[contains(text(),'营销海报')]")
        text = self.User.get_text("xpath", "//div[@class='button-group']/div[2]/button")
        try:
            assert text == '创建公用模板'
            log.info('用例test_marketingPoster通过')
        except AssertionError as e:
            log.error(f'用例test_marketingPoster不通过:{e}')
            raise

    def test_videoManagement(self):
        self.User.click('xpath', "//li[contains(text(),'营销海报')]/following-sibling::*[1]")
        text = self.User.get_text("class", "el-tabs__item.is-active")
        try:
            assert text == '帖子管理'
            log.info('用例test_videoManagement通过')
        except AssertionError as e:
            log.error(f'用例test_videoManagement不通过:{e}')
            raise

    def test_vrCase(self):
        self.User.click('xpath', "//li[contains(text(),'VR案例库')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == 'VR案例库'
            log.info('用例test_vrCase通过')
        except AssertionError as e:
            log.error(f'用例test_vrCase不通过:{e}')
            raise

    def test_livePage(self):
        self.User.click('xpath', "//li[contains(text(),'直播宣传页面')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '直播间名称'
            log.info('用例test_livePage通过')
        except AssertionError as e:
            log.error(f'用例test_livePage不通过:{e}')
            raise

    def test_informationList(self):
        self.User.click('xpath', "//li[contains(text(),'资讯列表')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '内容标题'
            log.info('用例test_informationList通过')
        except AssertionError as e:
            log.error(f'用例test_informationList不通过:{e}')
            raise

    def test_informationClassification(self):
        self.User.click('xpath', "//li[contains(text(),'资讯分类')]")
        text = self.User.get_text("xpath", "//tr/th[1]/div")
        try:
            assert text == '类别名称'
            log.info('用例test_informationClassification通过')
        except AssertionError as e:
            log.error(f'用例test_informationClassification不通过:{e}')
            raise


if __name__ == '__main__':
    pytest.main(["-s", "test_content_Management.py"])