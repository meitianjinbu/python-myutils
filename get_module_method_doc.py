#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:33:45 2018

@author: Calvin
"""

def info(object, spacing=20, collapse=0):
    '''
    遍历一遍Object对象，把里面可以被调用的方法及方法的doc string打印出来
    '''
    # 第一步：提取出当前Object可以被调用的方法列表
    methodList = [method for method in dir(object) if callable(
                getattr(object, method))]
    # print(methodList)
    # 第二步：需要把doc string的方法按照一个格式提取出来
    processFun = collapse and (lambda s:' '.join(str(s).split())) or (lambda s:s)
    
    # 第三步：把所有方法的名称及doc string都打印出来
    print('\n'.join(['{} {}'.format(method.ljust(spacing), processFun(getattr(object, method).__doc__)) for method in methodList
            ]))

# test case
info('str', 18, 1)