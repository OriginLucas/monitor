#!/usr/bin/python

import requests
import json
import queue

class get_data(object):
    def __init__(self,url='http://127.0.0.1:1621/data'):
        self.url=url
        a=requests.get(url=self.url).content.decode('utf-8')
        a=eval(a)

        # print(type(a))
        # print(a)
        self.data=a

    def get_cpu_data(self):
        if  self.data:
            cpu_data=self.data['cpu_data'] #这里得到列表
            # print(cpu_data)
            cpu_infomation=[]
            cpu_usage=[]
            for i in cpu_data:
                cpu_infomation.append(i['cpu_infomation'])
                cpu_usage.append( i['cpu_usage'])
            # print(cpu_usage)
            # print(cpu_infomation)
            return cpu_infomation,cpu_usage

        else:
            print('invalid data...')
            return False,False
