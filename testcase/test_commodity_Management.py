import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.commodity_Management import shangpinguanli
from public.globalvar import *

log = Log()


class Test_shangpinguanliMethods:
    """商品管理"""

    def setup_class(self):
        # driver = Login()
        # creatdict()
        # set_value('driver', driver)
        driver = get_value('driver')  # 获取 企业管理 保存的driver对象
        self.User = shangpinguanli(driver)
        self.User.click('xpath', "//div[contains(text(),'商品管理')]")
        log.info("展开商品管理菜单")

    def test_xuanpinList(self):
        self.User.click('xpath', "//li[contains(text(),'选品列表')]")
        text = self.User.get_text("xpath", "//form[@class='el-form query-form']/div[1]/label")
        try:
            assert text == '商品名称'
            log.info('用例test_xuanpinList通过')
        except AssertionError as e:
            log.error(f'用例test_xuanpinList不通过:{e}')
            raise

    def test_shangpinList(self):
        self.User.click('xpath', "//li[contains(text(),'商品列表')]")
        text = self.User.get_text("xpath", "//form[@class='el-form query-form']/div[1]/label")
        try:
            assert text == '商品名称'
            log.info('用例test_shangpinList通过')
        except AssertionError as e:
            log.error(f'用例test_shangpinList不通过:{e}')
            raise

    def test_tianjiafenlei(self):
        self.User.click('xpath', "//li[contains(text(),'添加分类')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '添加分类'
            log.info('用例test_tianjiafenlei通过')
        except AssertionError as e:
            log.error(f'用例test_tianjiafenlei不通过:{e}')
            raise

    def test_classificationList(self):
        self.User.click('xpath', "//li[contains(text(),'分类列表')]")
        text = self.User.get_text("xpath", "//tr/th[1]")
        try:
            assert text == '类别名称'
            log.info('用例test_classificationList通过')
        except AssertionError as e:
            log.error(f'用例test_classificationList不通过:{e}')
            raise

    def test_zhulichongzhi(self):
        self.User.click('xpath', "//li[contains(text(),'助力重置')]")
        text = self.User.get_text("css", ".section-header")
        try:
            assert text == '营销管理'
            log.info('用例test_zhulichongzhi通过')
        except AssertionError as e:
            log.error(f'用例test_zhulichongzhi不通过:{e}')
            raise

    def test_pinglunguanli(self):
        self.User.click('xpath', "//li[contains(text(),'评论中心')]")
        text = self.User.get_text("class", "el-tabs__item.is-active")
        try:
            assert text == '基础设置'
            log.info('用例test_pinglunguanli通过')
        except AssertionError as e:
            log.error(f'用例test_pinglunguanli不通过:{e}')
            raise


if __name__ == '__main__':
    pytest.main(["-s", "test_commodity_Management.py"])