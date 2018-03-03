#!/usr/bin/python
from Agent.plugin.Items.CPU import CPU_info
from Agent.plugin.Items.Memory import Mem_info
from Agent.plugin.Items.Disk import Disk_info
import queue
import  time


class Trans_data(object):
    space=queue.Queue(maxsize=20)
    def __init__(self,func):
        self.func=func
        if func=="CPU_info":
            self.func=CPU_info
        elif func=='Mem_info':
            self.func=Mem_info
        elif func=='Disk_info':
            self.func=Disk_info
        else:
            print('指令错误')

    def save_place(self):
        while True:
            data=self.func()
            # data=CPU_info()
            # print(data)
            if self.space.qsize()<20:
                self.space.put(data)
            else :
                self.get_data()
                continue
            time.sleep(0.1)

    def get_data(self):
        while True:
            if self.space.qsize()>0:
                for i in range(self.space.qsize()):
                    data=self.space.get()
                    return data
            else:
                continue
