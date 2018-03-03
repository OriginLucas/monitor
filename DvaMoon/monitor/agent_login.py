#!/usr/bin/python
from django.db import models
from monitor import models
'''
注册监控端数据

'''
agent_info={
        'ip':'127.0.0.1',
        'hostname':'127.0.0.1',
        'port':'127.0.0.1',
    }

def addAgent(ip,port,hostname):
    models.Agent_info.objects.create(ip=ip,
                                     hostname=hostname,
                                     port=port)

