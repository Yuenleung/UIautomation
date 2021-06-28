from selenium import webdriver
from public.log import Log
from public.readconfig import ReadConfig
log = Log()
def open_browser():
    read = ReadConfig()
    browser = read.getValue("browserType", "browserName")
    url = read.getValue("testServer", "URL")
    if browser == "Firefox":
        driver = webdriver.Firefox()
        log.info("启动{}浏览器".format(browser))
        driver.get(url)
        log.info("打开链接：{}".format(url))
        return driver
    elif browser == "Chrome":
        # 加启动配置
        option = webdriver.ChromeOptions()
        # 关闭“chrome正受到自动测试软件的控制”
        # V75以及以下版本
        # option.add_argument('disable-infobars')
        # V76以及以上版本
        option.add_experimental_option('useAutomationExtension', False)
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 不自动关闭浏览器
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=option)
        log.info("启动{}浏览器".format(browser))
        driver.get(url)
        log.info("打开链接：{}".format(url))
        return driver

if __name__ == '__main__':
    open_browser()



