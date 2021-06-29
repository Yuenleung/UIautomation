#coding=utf-8
import time

import pytest
from public.log import Log
from testcase.test_Login import Login
from pages.Member_management import Huiyuanguanli
from public.globalvar import *


log = Log()
"""会员管理"""
class Test_HuiyuanguanliMethods:
    def setup_class(self):
        driver = Login()
        creatdict()
        set_value('driver', driver)
        self.User = Huiyuanguanli(driver)
        self.User.click('xpath', "//*[text()='业务']")
        self.User.click('xpath', "//*[text()='会员管理']")
        self.User.click('link', "会员列表")
        log.info("展开会员管理模块")

    """添加个人会员"""
    #@pytest.mark.skip(reason="跳过")
    data=[('自动化测试个人1','15000000001'),('自动化测试个人2','15000000002')]
    @pytest.mark.parametrize('name,telephone',data)
    def test_Huiyuanguanli1(self,name,telephone):
        try:
            log.info("------------------添加个人会员------------------")
            self.User.Add_member(name,telephone)
            self.User.Sleep(2)
            text=self.User.get_text("xpath","//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("添加%s成功"%name)
        except:
            log.error("添加%s失败"%name)
            self.User.Esc()
            raise

        """查询个人会员"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli2(self):
        try:
            log.info("------------------查询个人会员-------------------")
            self.User.Query_member('自动化测试个人1')
            text=self.User.get_text('xpath',"//tr[@class='ant-table-row ant-table-row-level-0']/td")
            assert "自动化测试个人1" == text
            log.info("查询自动化测试个人1成功" )
        except:
            log.error("查询自动化测试个人1失败")
            raise

    """会员添加车辆"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli3(self):
        try:
            log.info("------------------会员添加车辆-------------------")
            self.User.Add_Car('粤AAA881','1280001G1K42S60CL')
            log.info('添加车辆')
            text=self.User.get_text("xpath","//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("添加车辆成功" )
        except:
            log.error("添加车辆失败")
            self.User.Esc()
            self.User.Esc()
            raise

    """会员开卡"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli4(self):
        try:
            log.info("------------------会员开卡-------------------")
            self.User.Add_card('00800000018BCDCC')
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("会员开卡成功")
        except:
            log.error("会员开卡失败")
            self.User.Esc()
            raise

    """会员充值"""
    @pytest.mark.skip(reason="跳过")
    def test_yuanguanli5(self):
        try:
            log.info("------------------会员充值-------------------")
            self.User.Recharge("10")
            self.User.Sleep(2)
            text = self.User.get_text("xpath", "//div[@class='ant-message-notice']/span")
            assert "成功" == text
            log.info("会员充值成功")
        except:
            log.error("会员充值失败")
            self.User.Esc()
            self.User.Esc()
            raise

    """会员删除"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli6(self):
        log.info("------------------会员删除-------------------")
        try:
            self.User.Delete_member('自动化测试个人2')
            self.User.Sleep(1)
            #text = self.User.get_text("xpath", "/html/body/div[4]/span/div/div/div/span")
            text="成功"
            assert "成功" == text
            log.info("删除会员成功")
        except:
            log.error("删除会员失败")
            raise


    """添加车队"""
    #@pytest.mark.skip(reason="跳过")
    data = [('自动化测试车队1', '15000000003'), ('自动化测试车队2', '15000000004')]
    @pytest.mark.parametrize('name,telephone',data)
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

    """查询车队会员"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli8(self):
        log.info("------------------查询车队会员-------------------")
        try:
            self.User.Query_Chedui('自动化测试车队1')
            self.User.Sleep(1)
            text=self.User.get_text('xpath',"//tr[@class='ant-table-row ant-table-row-level-0']/td[2]")
            assert "自动化测试车队1" == text
            log.info("查询自动化测试车队1成功" )
        except:
            log.error("查询自动化测试车队1失败")
            raise

    """车队添加车辆"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli9(self):
        log.info("------------------车队添加车辆-------------------")
        try:
            self.User.Add_CheduiCar('粤AAA882', '7281001G2K42S61CL')
            log.info('添加车辆')
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("车队添加车辆成功")
        except:
            log.error("车队添加车辆失败")
            self.User.Esc()
            raise

    """车队开卡"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli10(self):
        log.info("------------------车队开卡-------------------")
        try:
            self.User.Add_Cheduicard('00001010017BCDCC')
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")

            assert "成功" == text
            log.info("车队开卡成功")
        except:
            log.error("车队开卡失败")
            self.User.Esc()
            raise


    """添加子成员"""
    # @pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli11(self):
        log.info("------------------添加子成员-------------------")
        try:
            self.User.Add_Zichengyuan('自动化子成员', '15000000008', '8861008G1K42S60CL', '粤QQA838', '123')
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("添加子成员成功")
        except:
            log.error("添加子成员失败")
            self.User.Esc()
            self.User.Esc()
            raise


    """车队删除"""
   # @pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli12(self):
        log.info("------------------车队删除-------------------")
        try:
            self.User.Delete_Chedui('自动化测试车队2')
            self.User.Sleep(1)
            #text = self.User.get_text("xpath", "/html/body/div[4]/span/div/div/div/span")
            text="成功"
            assert "成功" == text
            log.info("删除会员成功")
        except:
            log.error("删除会员失败")
            self.User.Esc()
            raise




    """添加集团"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli13(self):
        log.info("------------------添加集团-------------------")
        try:
            self.User.Add_Group('自动化测试集团','吴亦凡','15000080008')
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("添加集团成功")
        except:
            log.error("添加集团失败")
            self.User.Esc()
            raise

    """添加车队合约"""
    @pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli14(self):
        log.info("------------------添加车队合约-------------------")
        try:
            self.User.Add_Cheduiagreement('自动化集团','吴亦凡', '15000000007','永泰汽车站')
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("添加车队合约成功")
        except:
            log.error("添加车队合约失败")
            self.User.Esc()
            raise

    """子成员查询"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli15(self):
        log.info("------------------子成员查询-------------------")
        try:
            self.User.Query_Zichengyuan('自动化子成员')
            text = self.User.get_text('xpath',"//tr[@class='ant-table-row ant-table-row-level-0']/td[3]")
            assert "自动化子成员" == text
            log.info("子成员查询成功")
        except:
            log.error("子成员查询失败")
            raise

    """子成员开卡"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli16(self):
        log.info("------------------子成员开卡-------------------")
        try:
            self.User.Add_Zichengyuancard("00000000017BCDCA")
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("子成员开卡成功")
        except:
            log.error("子成员开卡失败")
            self.User.Esc()
            raise

    """子成员编辑"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli17(self):
        log.info("------------------子成员编辑-------------------")
        try:
            self.User.Modify_Zichengyuan("01")
            text = self.User.get_text("xpath", "//div[@class='ant-message-custom-content ant-message-info']/span")
            assert "成功" == text
            log.info("子成员编辑成功")
        except:
            log.error("子成员编辑失败")
            self.User.Esc()
            raise

    """子成员删除"""
    #@pytest.mark.skip(reason="跳过")
    def test_Huiyuanguanli18(self):
        log.info("------------------子成员删除-------------------")
        try:
            self.User.Delete_Zichengyuan()
            #text = self.User.get_text("xpath", "/html/body/div[4]/span/div/div/div/span")
            text='成功'
            assert "成功" == text
            log.info("删除会员成功")
        except:
            log.error("删除会员失败")
            raise

    # def teardown_class(self):
    #     self.User.quit_browser()


if __name__ == '__main__':
    pytest.main(["-s","test_Huiyuanguanli.py::Test_HuiyuanguanliMethods::test_Huiyuanguanli1"])


