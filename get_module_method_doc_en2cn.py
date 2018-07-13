#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:33:45 2018

@author: Calvin
"""

import requests
import execjs
import json
import re

tk_js = '''
var b = function (a, b) {
    for (var d = 0; d < b.length - 2; d += 3) {
        var c = b.charAt(d + 2),
            c = "a" <= c ? c.charCodeAt(0) - 87 : Number(c),
            c = "+" == b.charAt(d + 1) ? a >>> c : a << c;
        a = "+" == b.charAt(d) ? a + c & 4294967295 : a ^ c
    }
    return a
}

var tk =  function (a,TKK) {
    for (var e = TKK.split("."), h = Number(e[0]) || 0, g = [], d = 0, f = 0; f < a.length; f++) {
        var c = a.charCodeAt(f);
        128 > c ? g[d++] = c : (2048 > c ? g[d++] = c >> 6 | 192 : (55296 == (c & 64512) && f + 1 < a.length && 56320 == (a.charCodeAt(f + 1) & 64512) ? (c = 65536 + ((c & 1023) << 10) + (a.charCodeAt(++f) & 1023), g[d++] = c >> 18 | 240, g[d++] = c >> 12 & 63 | 128) : g[d++] = c >> 12 | 224, g[d++] = c >> 6 & 63 | 128), g[d++] = c & 63 | 128)
    }
    a = h;
    for (d = 0; d < g.length; d++) a += g[d], a = b(a, "+-a^+6");
    a = b(a, "+-3^+b+-f");
    a ^= Number(e[1]) || 0;
    0 > a && (a = (a & 2147483647) + 2147483648);
    a %= 1E6;
    return a.toString() + "." + (a ^ h)
}
'''

pattern = '\[\[".+?\]\],'
reg_obj =  re.compile(pattern)

def get_googtran_tk(query_str):
    ctx = execjs.compile(tk_js)
    return ctx.call('tk', query_str, '425400.1881569881')
        

def get_translate_info(query_str):
    if not query_str:
        return '[[[[]]]]'
    url = 'https://translate.google.cn/translate_a/single'
    data = {'client': 't',
            'sl': 'auto',
            'tl': 'zh-CN',
            'hl': 'zh-CN',
            'dt': 'at',
            'dt': 'bd',
            'dt': 'ex',
            'dt': 'ld',
            'dt': 'md',
            'dt': 'qca',
            'dt': 'rw',
            'dt': 'rm',
            'dt': 'ss',
            'dt': 't',
            'ie': 'UTF-8',
            'oe': 'UTF-8',
            'source': 'bh',
            'ssel': '0',
            'tsel': '0',
            'kc': '1',
            'tk': get_googtran_tk(query_str),
            'q': query_str
        }
    headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://translate.google.cn/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            "Content-Type" : "application/json; charset=UTF-8",
            'X-Client-Data': 'CJC2yQEIpbbJAQjBtskBCKmdygEI2J3KAQioo8oB'
        }
    res = requests.get(url, params=data, headers=headers)
#    res.encoding('utf-8')
    tran_str = ''
    for tran in json.loads(reg_obj.findall(res.text)[0][:-1]):
        tran_str += tran[0]
    return tran_str


def info(object, spacing=20, collapse=0, tran=0):
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
    print('\n'.join(['{} {}'.format(method.ljust(spacing), get_translate_info(processFun(getattr(object, method).__doc__))) for method in methodList
            ]))

if __name__ == '__main__':
    import os
    info(os.path, 18, 1)
