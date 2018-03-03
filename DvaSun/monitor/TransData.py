#!/usr/bin/python
from Agent.plugin.collectData import get_totalInfo
from Agent.plugin.collectData import collect_api
import requests
import time
import json

def TransLoop(url):
    while True:
        time.sleep(1)
        res=requests.get(url=url)
        res=eval(res.text)
        interval=res['interval']
        if res['identification_code']=='DvaSun.monitor.com':   #确定标识码
            while True:
                data={}
                time.sleep(interval)
                # data=get_totalInfo().post_info()
                cpu_data=collect_api().col_cpu()
                memory_data=collect_api().col_memory()
                disk_data=collect_api().col_disk()
                data['cpu_data']=cpu_data
                data['memory_data']=memory_data
                data['disk_data']=disk_data
                print(data)
                data=json.dumps(data)#  {'cpu_data':'...'  , 'memory_data':'...'   ,   'disk_data':'...' }
                requests.post(url=url,data=data)
        else:
            break
