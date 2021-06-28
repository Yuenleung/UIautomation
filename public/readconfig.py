import os
import configparser
import codecs

conf_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\config\\conf.ini'

class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """

    def __init__(self, filename=conf_path):
        with open(filename, 'r', encoding='UTF-8') as f:
            data = f.read()
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                files = codecs.open(filename, "w")
                files.write(data)
                files.close()


        self.cf = configparser.ConfigParser()
        self.cf.read(filename, encoding='UTF-8')  # read(file_path, encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误

    def getValue(self, env, name):
        """读取配置文件中的值"""
        return self.cf.get(env, name)