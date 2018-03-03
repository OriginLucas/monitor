#!/usr/bin/python
import time
from monitor.save_data import trigger_data
from trigger.sendMail import Mail
from trigger.save_redis import Storage


class data_alert(object):
    def __init__(self):
        self.count=0

    def cpu_data(self):
        usage,infomation=trigger_data()  #两个列表  【】  【【】】
        if usage:
            for i in usage:
                if i>=80:
                    self.count+=1
                else:continue
            Mail().rank(self.count)
            print(usage)
        else:
            print('no data to analyze')




    def memory_data(self):
        pass
    def disk_data(self):
        pass