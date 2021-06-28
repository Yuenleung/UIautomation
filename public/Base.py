import os
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.log import Log
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

log = Log()

class BasePase:
    """调用方法"""
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def isdisplayed(element):
        """元素是否存在"""
        try:
            value = element.is_displayed()
            if value:
                log.info('元素{}存在'.format(element))
            else:
                log.info('元素{}不存在'.format(element))
            return value
        except AttributeError as e:
            log.error(e)


    @staticmethod
    def Sleep(secondes):
        """强制等待"""
        time.sleep(secondes)
        log.info('暂停%d秒' % secondes)

    def implicitly_wait(self, seconds):
        """隐式等待"""
        self.driver.implicitly_wait(seconds)
        log.info("隐式等待{}秒".format(seconds))


    def get_img(self, rq=time.strftime('%Y%m%d%H%M', time.localtime(time.time()))):
        """截图"""
        path = os.path.join(os.path.abspath('..'), 'report', 'img')
        # path = os.path.join(getcwd.get_cwd(), 'screenshots/')  # 拼接截图保存路径
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 按格式获取当前时间
        screen_name = path + rq + '.png'  # 拼接截图文件名
        # noinspection PyBroadException
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log.info("截图保存成功{}".format(screen_name))
        except BaseException as e:
            log.error("截图失败{}".format(e))

    def find_element(self, by, value):
        """定位元素"""
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            try:
                if by == 'id':
                    element = self.driver.find_element(By.ID, value)
                    log.info('元素定位成功。定位方式：%s,使用的值：%s' % (by, value))
                elif by == 'name':
                    element = self.driver.find_element(By.NAME,value)
                    log.info('元素定位成功。定位方式：%s,使用的值：%s' % (by, value))
                elif by == 'class':
                    element = self.driver.find_element(By.CLASS_NAME,value)
                    log.info('元素定位成功。定位方式：%s,使用的值：%s' % (by, value))
                elif by == 'tag':
                    element = self.driver.find_element(By.TAG_NAME,value)
                    log.info('元素定位成功。定位方式：%s,使用的值：%s' % (by, value))
                elif by == 'link':
                    element = self.driver.find_element(By.LINK_TEXT,value)
                    log.info('元素定位成功。定位方式：%s,使用的值：%s' % (by, value))
                elif by == 'plink':
                    element = self.driver.find_element(By.PARTIAL_LINK_TEXT,value)
                    log.info('元素定位成功。定位方式：%s,使用的值：%s' % (by, value))
                elif by == 'css':
                    element = self.driver.find_element(By.CSS_SELECTOR,value)
                    log.info('元素定位成功。定位方式：%s,使用的值：%s' % (by, value))
                elif by == 'xpath':
                    element = self.driver.find_element(By.XPATH,value)
                    log.info('元素定位成功。定位方式：%s,使用的值：%s' % (by, value))
                else:
                    log.error('没有找到输入的定位方式')
                return element
            #输入的元素的值有误
            except NoSuchElementException as e:
                log.error("报错信息：{}".format(e))
        #输入的定位方式有误就报错
        else:
            log.error('输入的元素定位方式错误,参考[id, name, class, tag, link, plink, css,xpath]')

    def type(self,by,value,text):
        """输入内容"""
        element=self.find_element(by,value)
        """
        try:
            element.clear()
            log.info('清空成功')
        except:
           log.error("清空失败")
        """
        # noinspection PyBroadException
        try:
            element.send_keys(text)
            log.info('输入的内容：%s' % text)
        except :
            try:
                self.Sleep(1)
                element.send_keys(text)
                log.info('输入的内容：%s' % text)
            except BaseException as e:
                log.error('内容输入报错{}'.format(e))
                raise
            #self.get_img()
            raise

    def click(self,by,value):
        """点击元素"""
        element = self.find_element(by,value)
        # noinspection PyBroadException
        try:
            element.click()
            log.info('点击元素成功')
        except Exception as e:
            display = self.isdisplayed(element)
            if display is True:
                self.Sleep(3)
                element.click()
                log.info('点击元素成功')
            else:
                log.error('点击元素失败{}'.format(e))
                raise


    def get_text(self,by,value):
        """获取元素文本信息"""
        try:
            text = self.find_element(by,value).text
            log.info('获取元素{}的文本信息为：{}'.format((by,value), text))
            return text
        except Exception as e:
            log.error('获取元素{}的文本信息错误,{}'.format((by,value), e))

    def quit_browser(self):
        """关闭浏览器"""
        self.driver.quit()
        log.info('关闭浏览器')

    def switch_ifarme(self,by,value):
        """切换ifarme"""
        element = self.find_element(by,value)
        # noinspection PyBroadException
        try:
            self.driver.switch_to.frame(element)
            log.info('切换frame成功')
        except BaseException as e:
            log.error('切换frame报错:{}'.format(e))

    def alert_text(self):
        """获取弹窗文本"""
        text = self.driver.switch_to.alert.text()
        log.info('获取弹窗内容为%s'%text)
        return text

    def Clear(self,by,value):
        element = self.find_element(by, value)
        element.clear()
        log.info("清空成功")

    def maximize_window(self):
        """窗口最大化"""
        self.driver.maximize_window()
        log.info("窗口最大化")
        # t1 = time.time()
       # self.driver.set_window_size(wide, high)
        #log.info('设置浏览器宽：{} 高：{}'.format(wide, high))

    def Zoom(self,proportion):
        js = "document.body.style.zoom={}".format(proportion)
        self.driver.execute_script(js)

    def use_js(self, js):
        """调用js"""
        # noinspection PyBroadException
        try:
            self.driver.execute_script(js)
            log.info('js执行成功，js内容为：%s' % js)
        except BaseException as e:
            log.error('js执行报错：{}'.format(e))

    def original_driver(self):
        """返回原生driver"""
        return self.driver

    def Assert(self,asserttext,text,succeedlog,faillog):
        try:
            assert asserttext == text
            log.info(succeedlog )
        except:
            log.error(faillog)
            raise

    def Double_click(self,by, value):

        """双击元素"""
        try:
            element = self.find_element(by, value)
            ActionChains(self.driver).double_click(element).perform()
            log.info('双击元素{}'.format(by, value))
        except Exception as e:
            log.error('双击元素{}错误'.format(by, value, e))
            raise

    def set_window(self,wide, high):
        """窗口自定义宽高"""
        self.driver.set_window_size(wide, high)
        log.info('设置浏览器宽：{} 高：{}'.format(wide, high))

    def Esc(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        log.info("------------用例执行失败退出弹窗执行下一用例------------------")

    def jsclick(self,by, value):
        element = self.find_element(by, value)
        try:
            self.driver.execute_script('arguments[0].click();', element)
            log.info('JS点击元素成功')
        except BaseException as e:
            display = self.isdisplayed(element)
            if display is True:
                self.Sleep(3)
                try:
                    self.driver.execute_script('arguments[0].click();', element)
                    log.info('JS点击元素成功')
                except BaseException as e:
                    log.error('JS点击元素报错{}'.format(e))

    def element_wait(self, by,value ,seconds=5):
        """显性等待"""
        messages = '元素: {0} 没有找到 ：在{1}S内.'.format((by, value), seconds)
        try:
            if by == "id":
                element =WebDriverWait(self.driver, seconds,1).until(EC.presence_of_element_located((By.ID, value)), messages)
            elif by == "name":
                element =WebDriverWait(self.driver, seconds,1).until(EC.presence_of_element_located((By.NAME, value)), messages)
            elif by == "class":
                element =WebDriverWait(self.driver, seconds,1).until(EC.presence_of_element_located((By.CLASS_NAME, value)),
                                                             messages)
            elif by == "link_text":
                element =WebDriverWait(self.driver, seconds,1).until(EC.presence_of_element_located((By.LINK_TEXT, value)),
                                                             messages)
            elif by == "xpath":
                element =WebDriverWait(self.driver, seconds,1).until(EC.presence_of_element_located((By.XPATH, value)),
                                                             messages)
            elif by == "css":
                element =WebDriverWait(self.driver, seconds,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)),
                                                             messages)
            else:
                raise NameError(
                    "请检查输入是否正确！!>>'id','name','class','link_text','xpaht','css'.")
            return element
        except:
            log.error(messages)
    """显性等待点击"""
    def xclick(self, by, value):
        try:
            self.element_wait(by,value).click()
            log.info('显性等待点击元素成功')
        except:
            log.error('显性等待点击元素失败')
            raise

