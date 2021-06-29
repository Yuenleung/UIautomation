from public.Base import BasePase
from public.readconfig import ReadConfig

class Loginpage(BasePase):

    # def login(self,sellerNo,username,password):
    #     self.type('css', "[placeholder='商家编号']", sellerNo)
    #     self.Clear('css',"[placeholder='账号']")
    #     self.type('css',"[placeholder='账号']",username)
    #     self.Clear('css', "[placeholder='密码']")
    #     self.type('css',"[placeholder='密码']",password)
    #    # self.click("css","[type='button']")
    #     self.click('class','login-button')

    def login(self, phone, password, miniProgramName):
        self.click('xpath', "//span[text()='我是管理员']")
        self.type('id', "phoneNumber", phone)
        self.type('id', "passwd", password)
        self.click('id', "login_btn")
        if miniProgramName == "美家咖":
            self.click('xpath', f"//h3[text()='{miniProgramName}']")
        elif miniProgramName == "营客云":
            self.click('link', '2')
            self.click('xpath', f"//h3[text()='{miniProgramName}']")

