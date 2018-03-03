#!/usr/bin/python
import redis
from  monitor import models
'''
从redis中取得数据  根据不同参数取不同的时间段数据

grade1--10分钟
grade2--1小时
grade3--1天
grade4--1月
grade5--1年
'''
class Acquire(object):
    def __init__(self,shaft,item):
        self.shaft=shaft
        self.item=item
        self.pool = redis.ConnectionPool(host='172.196.70.3', port=6379)
        if shaft==1:
            self.grade1()
        elif shaft==2:
            self.grade2()
        elif shaft==3:
            self.grade3()
        elif shaft==4:
            self.grade4()
        elif shaft==5:
            self.grade5()
        else:
            self.err()


    def grade1(self):
        obj = redis.Redis(connection_pool=self.pool)
        name=models.Redis_name.objects.filter(grade=1,item=self.item)#取到redis中对应时间和项目的name
        data=obj.lrange(name,0,-1).decode('utf-8')
        if data:
            data=eval(data)
            return data
        else:
            return False


    def grade2(self):
        pass
    def grade3(self):
        pass
    def grade4(self):
        pass
    def grade5(self):
        pass
    def err(self):
        return False