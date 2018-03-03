#!/usr/bin/python
from Agent.plugin.launch import launch_items
'''
等待接收监控参数
'''
import time
if __name__=='__main__':
    while True:
        time.sleep(1)
        a=launch_items().start_item()
    print("working...")