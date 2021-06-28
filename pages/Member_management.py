from public.Base import BasePase
from public.log import Log
from testcase.test_Login import Login

log=Log()


"""会员管理"""
class Huiyuanguanli(BasePase):
    """添加个人会员"""
    def Add_member(self,name,telephone):
        self.click('xpath',"//button[3]")#点击添加
        self.Clear('css', "[placeholder='请输入名字']")#清空文本框
        self.type('css',"[placeholder='请输入名字']",name)#输入个人会员名字
        self.Clear('id',"coordinated_saveParam.telephone")#清空文本框
        self.type('id',"coordinated_saveParam.telephone",telephone)#输入个人会员手机号
        self.click('xpath',"//div[@class='ant-modal-footer']/button")#点击提交

    """查询个人会员"""
    def Query_member(self,name):
        self.type('css',"[placeholder='请输入会员名称']",name)  # 输入会员名称
        self.click('xpath', "//button[2]")  # 点击重置
        log.info("重置")
        self.type('css', "[placeholder='请输入会员名称']", name)  # 再次输入会员名称
        self.Sleep(1)
        self.click('xpath', "//button[1]")#点击查询
        self.Sleep(1)

    """会员添加车辆"""
    def Add_Car(self,number,vin):
        #self.click('link', '会员管理')
        self.click('link',  '车辆')#点击车辆
        self.jsclick('xpath', "//span[text()='添加车辆']")
        self.click('xpath',  "//div[text()='请选择运营类型']")#点击选择运营类型
        self.click('class', 'ant-select-dropdown-menu-item')#选择运营类型
        self.type('id', 'coordinated_carSaveData.plateNo',number)#输入车牌号
        self.type('id', 'coordinated_carSaveData.vin', vin)#输入vin
        self.click('id', 'coordinated_carSaveData.vehicleType')  # 点击选择车辆类型
        self.click('class','ant-select-dropdown-menu-item-active' )  # 选择车辆类型
        self.click('xpath', "//form[@class='ant-advanced-search-form ant-form ant-form-horizontal']/../../div[3]/button")# 点击添加
    """会员开卡"""
    def Add_card(self,Care_number):
        #self.click('link', '会员管理')
        self.click('link','开卡')#点击开卡
        self.Sleep(1)
        self.type('id','coordinated_openCardQueryData.number',Care_number)
        self.click('xpath',"//input[@id='coordinated_openCardQueryData.number']/../../../../../../../div[3]/button") # 点击添加

    """会员充值"""
    def Recharge(self,money):
        #self.click('link', '会员管理')
        self.click('link','详细')#点击详细
        self.jsclick('xpath',"//span[text()='点击查看账户']")#点击查看账户
        self.click('link', '充值')#点击充值
        self.type('css',"[placeholder='请输入金额']",money)#输入金额
        self.click('xpath',"//input[@placeholder='请输入金额']/../../../../../../../div[3]/button") # 点击确定

    """会员删除"""
    def Delete_member(self, name):
        # self.click('link', '会员管理')
        self.click('xpath', "//button[2]")  # 点击重置
        self.type('css', "[placeholder='请输入会员名称']", name)  # 输入会员名称
        self.click('xpath', "//button[1]")  # 点击查询
        self.Sleep(1)
        self.click('link', '删除')  # 点击删除
        self.click('xpath', "//div[@class='ant-modal-confirm-btns']/button[1]")  # 取消
        self.Sleep(1)
        self.click('link', '删除')  # 点击删除
        self.click('xpath', "//div[@class='ant-modal-confirm-btns']/button[2]")  # 确定

    """车队注册"""
    def Add_Chedui(self,name,telephone):
        self.click('link','车队管理')#点击车队管理
        self.click('xpath',"//button[3]")#点击添加
        self.Clear('css', "[placeholder='请输入名字']")#清空文本框
        self.type('css',"[placeholder='请输入名字']",name)#输入车队会员名字
        self.Clear('id',"coordinated_saveParam.telephone")#清空文本框
        self.type('id',"coordinated_saveParam.telephone",telephone)#输入车队会员手机号
        self.click('xpath',"//div[@class='ant-modal-footer']/button")#点击提交

    """查询车队会员"""
    def Query_Chedui(self,name):
        #self.click('link', '车队管理')  # 点击车队管理
        self.type('css',"[placeholder='请输入会员名称']",name)  # 输入会员名称
        self.click('xpath', "//button[2]")  # 点击重置
        log.info("重置")
        self.type('css', "[placeholder='请输入会员名称']", name)  # 再次输入会员名称
        self.click('xpath', "//button[1]")#点击查询

    """车队添加车辆"""
    def Add_CheduiCar(self, number, vin):
        #self.click('link', '车队管理')
        self.click('link', '车辆')  # 点击车辆
        self.jsclick('xpath',"//span[text()='添加车辆']")   # 点击添加车辆
        self.click('xpath', "//div[text()='请选择运营类型']")  # 点击选择运营类型
        self.click('class', 'ant-select-dropdown-menu-item')  # 选择运营类型
        self.type('id', 'coordinated_carSaveData.plateNo', number)  # 输入车牌号
        self.type('id', 'coordinated_carSaveData.vin', vin)  # 输入vin
        self.click('id', 'coordinated_carSaveData.vehicleType')  # 点击选择车辆类型
        self.click('class', 'ant-select-dropdown-menu-item-active')  # 选择车辆类型
        self.click('xpath', "//form[@class='ant-advanced-search-form ant-form ant-form-horizontal']/../../div[3]/button")# 点击添加

    """车队开卡"""
    def Add_Cheduicard(self,Care_number):
       # self.click('link', '车队管理')
        self.click('link', '开卡')  # 点击开卡
        self.type('id', 'coordinated_openCardQueryData.number', Care_number)
        self.click('xpath',"//input[@id='coordinated_openCardQueryData.number']/../../../../../../../div[3]/button") # 点击添加

    """添加子成员"""
    def Add_Zichengyuan(self, name, telephone, vin, number, Zibianhao):
        #self.click('link', '车队管理')
        self.click('link', '团队')  # 点击团队
        self.original_driver().switch_to.default_content()
        self.click('xpath', "//span[text()='添加子成员']/..")  # 点击添加子成员
        self.Sleep(1)
        self.original_driver().switch_to.default_content()
        self.type('xpath', "//input[@id='coordinated_leaguerSaveData.name']", name)  # 输入子成员名称
        self.type('id', "coordinated_leaguerSaveData.telephone", telephone)  # 输入会员名称
        self.type('css', "[placeholder='请输入车辆VIN码']", vin)  # 输入vin
        self.type('xpath', "//input[@placeholder='请输入车辆VIN码']/../../../../../div[4]/div[2]/div/span/input", number)  # 输入车牌号
        self.type('xpath', "//input[@placeholder='请输入车辆VIN码']/../../../../../div[5]/div[2]/div/span/input", Zibianhao)  # 输入子成员名称
        self.click('xpath',"//input[@placeholder='请输入车辆VIN码']/../../../../../../../../div[3]/button")# 点击添加

    """车队删除"""
    def Delete_Chedui(self,name):
        #self.click('link', '车队管理')
        self.click('xpath', "//button[2]")  # 点击重置
        self.type('css', "[placeholder='请输入会员名称']", name)  # 输入会员名称
        self.click('xpath', "//button[1]")  # 点击查询
        self.Sleep(1)
        self.click('link', '删除')  # 点击删除
        self.click('xpath', "//div[@class='ant-modal-confirm-btns']/button[1]")  # 取消
        self.click('link', '删除')  # 点击删除
        self.click('xpath', "//div[@class='ant-modal-confirm-btns']/button[2]")  # 确定



    """添加集团"""
    def Add_Group (self, Group, name, telephone):
        self.click('link', '集团管理')  # 点击集团管理
        self.click('xpath', "//button[3]")  # 点击添加
        self.Sleep(1)
        self.type('id', "coordinated_tmp.name", Group)  # 输入集团名称
        self.type('id', "coordinated_tmp.linkman", name)  # 输入联系人
        self.type('id', "coordinated_tmp.phone", telephone)  # 输入联系电话
        self.click('xpath', "//div[@name='checkboxgroup']/div/div[last()]")
        self.click('xpath',"//div[@class='ant-modal-footer']/button")#点击提交


    """添加车队合约"""
    def Add_Cheduiagreement(self,agreement,name, telephone,station):
        self.click('link', '车队合约')  # 点击车队合约
        self.click('xpath', "//button[3]")  # 点击添加
        self.type('id', 'coordinated_saveParam.name', agreement)  # 合约名称
        self.type('id', 'coordinated_saveParam.linkman', name)   # 联系人
        self.type('id', 'coordinated_saveParam.phone', telephone)   # 联系电话
        self.click('class','ant-collapse-header')# 选择站点
        self.click('xpath', "//span[contains(text(),'{}')]".format(station) )  # 选择站点
        self.click('xpath',"//div[@class='ant-modal-footer']/button")  # 点击提交

    """子成员查询"""
    def Query_Zichengyuan(self, name):
        self.click('link', '司机管理')  # 点击司机管理
        self.type('css', "[placeholder='请输入司机名称']", name)  # 输入会员名称
        self.click('xpath', "//button[2]")  # 点击重置
        log.info("重置")
        self.type('css', "[placeholder='请输入司机名称']", name)  # 再次输入会员名称
        self.Sleep(1)
        self.click('xpath', "//button[1]")  # 点击查询

    """子成员开卡"""
    def Add_Zichengyuancard(self, Care_number):
        self.click('link', '开卡')
        self.type('css',"[placeholder='请输入卡号']",Care_number)
        self.click('xpath',"//div[@class='ant-modal-footer']/button")  # 点击提交

    """子成员编辑"""
    def Modify_Zichengyuan(self,num):
        self.click('link', '编辑')
        self.type('css', "[placeholder='请输入车辆自编号']", num)  # 修改自编号
        self.click('xpath',"//input[@placeholder='请输入车辆VIN码']/../../../../../../../../div[3]/button")# 点击添加


    """子成员删除"""
    def Delete_Zichengyuan(self):
        self.click('link', '删除')  # 点击删除
        self.click('xpath', "//div[@class='ant-modal-confirm-btns']/button[1]")  # 取消
        self.Sleep(1)
        self.click('link', '删除')  # 点击删除
        self.click('xpath', "//div[@class='ant-modal-confirm-btns']/button[2]")  # 确定
''' 
driver=Login()
User = Huiyuanguanli(driver)
User.click('xpath',"//*[text()='会员管理']")
log.info("展开会员管理模块")
User.Add_Group('自动化集团','吴亦凡','15000000006')
'''