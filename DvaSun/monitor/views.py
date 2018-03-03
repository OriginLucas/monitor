import json
import requests
from django.shortcuts import HttpResponse,render

from  Agent.plugin.collectData import get_totalInfo


# Create your views here.



def listening(request):
    '''限制对方的端口为1611'''
    while True:
        if request.method=='GET' :#  and request.META['SERVER_PORT']==1611:
            # print(request.META['SERVER_PORT'])
            data_dic=get_totalInfo().post_info()#接收的是字典  无法json
            print(data_dic)
            # print(type(data_dic))
            return HttpResponse(json.dumps(data_dic))
        else:
            dic={'aa':'okkk'}
            return HttpResponse(json.dumps(dic))

from monitor import TransData


def transmit(request):
    if request.method=="GET":
        # a=request.META('HTTP_HOST')
        # print(a)
        url = 'http://127.0.0.1:1611/save/'
        TransData.TransLoop(url)  #这里开始传送数据
        return HttpResponse('invalid identification code,please check your file "conf.py" and try again...')
    elif request.method=='POST':
        a=request.body.decode('utf-8')
        print(a[0])
        print(type(a))
        a=eval(a)
        print(a)
        print(type(a))
        return HttpResponse('ojbk')
