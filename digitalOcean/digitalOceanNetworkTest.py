#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python2
"""
Package  : 
Function : 
Author   : bihuchao <bihuchao1995@gmail.com>
"""

import os
import re

if __name__ == "__main__":
    dominNames = [
        "speedtest-nyc1.digitalocean.com",
        "speedtest-nyc2.digitalocean.com",
        "speedtest-nyc3.digitalocean.com",
        "speedtest-ams2.digitalocean.com",
        "speedtest-ams3.digitalocean.com",
        "speedtest-sfo1.digitalocean.com",
        "speedtest-sfo2.digitalocean.com",
        "speedtest-sgp1.digitalocean.com",
        "speedtest-lon1.digitalocean.com",
        "speedtest-fra1.digitalocean.com",
        "speedtest-tor1.digitalocean.com",
        "speedtest-blr1.digitalocean.com",
    ]
    num = 200
    delayData = {}
    print("数据包个数为{0}".format(num))
    for dominName in dominNames:
        os.system("ping {0} -n {1}> temptemptemp.txt".format(dominName, num))
        data = []
        f = open("temptemptemp.txt", "r")
        content = f.read()
        f.close()
        for x in re.findall(r'数据包: 已发送 \= (.*?)，已接收 \= (.*?)，丢失 \= (.*?) \((.*?) 丢失\)', content, re.S):
            data.append(x)
        for x in re.findall(r'最短 = (.*?)ms，最长 = (.*?)ms，平均 = (.*?)ms', content, re.S):
            data.append(x)
        os.remove("temptemptemp.txt")
        delayData[dominName] = data
        print("{0} {1} {2}".format(dominName[10:14], data[0][3], data[1][2]))
