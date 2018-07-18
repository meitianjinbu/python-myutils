#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:58:49 2018

@author: Calvin
"""

import logging

class SimpleLogger(logging.Logger):
    def __init__(self, name='SimpleLogger', log_path='myLogger.log', level=logging.DEBUG, formatter=None):
        super().__init__(name)
        # 指定logger的输出格式
        if not formatter:
            self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        else:
            self.formatter = formatter
        # 文件日志，终端日志
        self.file_handler = logging.FileHandler(log_path)
        # 文件日志按照指定的格式来写
        self.file_handler.setFormatter(self.formatter)
        # 可以设置日志的级别，下面是设置低于debug级别的日志不写入
        self.setLevel(level)
        # 把文件日志，终端日志处理对象添加到日志处理器logger中
        if len(self.handlers) == 0:
            self.addHandler(self.file_handler)
    
    def release(self):
        # 不需要些日志要把handler移除掉，因为logging会常驻内存，然后每次都添加一个句柄，会重复写log信息
        self.removeHandler(self.file_handler)
        self.file_handler.close()