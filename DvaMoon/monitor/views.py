from django.shortcuts import render,redirect,HttpResponse
import json
# Create your views here.
from data.get_cpu_data import get_data
from monitor.get_model import get_host_info
from monitor.agent_login import addAgent
#
# def data(request):
#     if request.method=="GET":
#         return render(request,'chart.html',{'data':json.dumps(cpu_data)})
#     else:
#         return HttpResponse("ss")



def cpu_data(request):
    if request.method=="GET":
        cpu_infomation,cpu_usage=get_data().get_cpu_data()
        print(cpu_infomation)
        if  cpu_infomation and cpu_usage:#有数据
            return render(request,'chart.html',{'data':cpu_usage})
        else:
            return HttpResponse("holy shit，where is my data。。。")
    elif request.method=="POST":


        return HttpResponse("gun")


def add_agent(request):
    if request.method=="GET":
        return render(request,'add_agent.html')
    elif request.method=='POST':
        ip=request.POST('ip')
        port=request.POST('port')
        hostname=request.POST('hostname')
        addAgent(ip,port,hostname)


        return render(request,'add_agent.html',{'msg':'success'})

def index(request):
    if request.method=="GET":
        list=get_host_info()
        # for i in list:
        #     print(i)
        dic={
            'ip':list
        }
        return render(request,'index.html',dic)
    elif request.method=="POST":
        ip=request.POST['ip']
        url='http://'+ip+':1621/data'
        a=get_data(url)
        info,usage=a.get_cpu_data()
        if  info and usage:#有数据
            return render(request,'chart.html',{'data':usage})
        else:
            return HttpResponse("holy shit，where is my data。。。")


from monitor.save_data import save_place
from monitor.save_data import put_data
from monitor import conf
conf_dic={
    'interval':conf.interval,
    'identification_code':'DvaSun.monitor.com'
    }
def loopdata(request):
    while True:
        if request.method=="GET":
            # return HttpResponse('ok')
            return HttpResponse(json.dumps(conf_dic))
        elif request.method=="POST":
            data=eval(request.body.decode('utf-8'))#{'cpu_data':'...'  , 'memory_data':'...'   ,   'disk_data':'...' }
            # print(data)
            ip=request.META['REMOTE_ADDR']
            save_place(data,ip)

            return HttpResponse('en')

'''
实时数据监控
'''
def display(request):
    if request.method=="GET":
        a=[]
        usage=put_data()
        infomation=put_data()
        if usage:
            for i in usage:
                a.append(i['cpu_usage'])
            return render(request,'chart.html',{"data":usage})
        else:
            return render(request, 'chart.html', {"data": a})
'''
监控历史数据
'''
from monitor.acquire_data import Acquire
def history(request):
    if request.method=="POST":
        shaft=request.POST('time')
        item=request.POST('item')   #需要提供 项目 和 时间段
        data=Acquire(shaft,item)
        if data:

            return render(request,'')
        else:
            return HttpResponse('The data is not generated for the time being...')
    else:
        return HttpResponse('Error')