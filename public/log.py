#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:写入log文件和打印
 @author: yansh
"""
import logging
import time
import os
from public.readconfig import ReadConfig
import colorlog

read = ReadConfig()
logLevel = read.getValue("logLevel", "level")


# 设置控制台打印的颜色
log_colors_config = {
    'DEBUG': 'yellow',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}
class Log:
    def __init__(self):
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.logname = os.path.join(root_path, 'report', 'log', '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        if logLevel == 'debug':
            logger.setLevel(logging.DEBUG)
        elif logLevel == 'info':
            logger.setLevel(logging.INFO)
        elif logLevel == 'warn':
            logger.setLevel(logging.WARN)
        elif logLevel == 'error':
            logger.setLevel(logging.ERROR)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        #fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        #ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = colorlog.ColoredFormatter('%(log_color)s %(asctime)s - %(levelname)s - %(message)s',
                                              log_colors=log_colors_config)
        formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter1)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)
