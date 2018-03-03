#!/usr/bin/python
from __future__ import division #放到第一行  py2版本使用时 / 变为精确除法  py3无影响


import redis



'''
将redis中的数据分别整合为10min 。。。 的平均值，
然后另外存储
'''

class Manager(object):
    def __init__(self,name):
        self.name=name
        self.pool=redis.ConnectionPool(host='172.196.70.3', port=6379)
        self.ten_min(self.name)
    '''
    十分钟数据整合
    '''
    def ten_min(self,name):
        '''
        name是上一个的name
        next是本次的name
        '''
        next=name+'_ten_min'
        obj = redis.Redis(connection_pool=self.pool)
        len1=obj.llen(name)
        len2=obj.llen(next)
        if int(len1/10) > len2:
            list=eval(obj.lrange(name,len2*10,len2*10+9).decode('utf-8'))
            sum=0
            for i in list:
                sum+=i
            sum=sum/10
            obj.lpush(next,sum)
        else:
            pass
        self.one_houer(next)
    '''
    一小时数据整合
    '''
    def one_houer(self,name):
        obj = redis.Redis(connection_pool=self.pool)
        next = name.strip('_ten_min') + '_one_honer'
        len1 = obj.llen(name)
        len2 = obj.llen(next)
        if int(len1/6) > len2:
            list=eval(obj.lrange(name,len2*6,len2*6+5).decode('utf-8'))
            sum=0
            for i in list:
                sum+=i
            sum=sum/6
            obj.lpush(next,sum)
        else:
            pass
        self.one_day(next)
    '''
    一天数据整合
    '''
    def one_day(self,name):
        obj = redis.Redis(connection_pool=self.pool)
        next = name.strip('_one_honer')+'_one_day'
        len1 = obj.llen(name)
        len2 = obj.llen(next)
        if int(len1 / 24) > len2:
            list = eval(obj.lrange(name, len2 * 24, len2 * 24 + 23).decode('utf-8'))
            sum = 0
            for i in list:
                sum += i
            sum = sum / 24
            obj.lpush(next, sum)
        else:
            pass
        self.one_month(next)

    '''
    一个月数据整合
    '''
    def one_month(self,name):
        obj = redis.Redis(connection_pool=self.pool)
        next = name.strip('_one_day')+'_one_month'
        len1 = obj.llen(name)
        len2 = obj.llen(next)
        if int(len1 / 30) > len2:
            list = eval(obj.lrange(name, len2 * 30, len2 * 30 + 29).decode('utf-8'))
            sum = 0
            for i in list:
                sum += i
            sum = sum / 24
            obj.lpush(next, sum)
        else:
            pass
        self.one_year(next)

    '''
    一年数据整合
    '''
    def one_year(self):
        pass