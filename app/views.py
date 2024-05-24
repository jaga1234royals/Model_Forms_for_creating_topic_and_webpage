from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    EMFO=TopicForm()
    d={'EMFO':EMFO}
    if request.method=="POST":
        TFO=TopicForm(request.POST)
        if TFO.is_valid():
            TFO.save()
            return HttpResponse('TOPIC INSERTED')
        else:
            return HttpResponse('INVALID DATA')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WMFO=WebpageForm()
    d={'WMFO':WMFO}
    if request.method=="POST":
        WFO=WebpageForm(request.POST)
        if WFO.is_valid():
            WFO.save()
            return HttpResponse('WEBPAGE INSERTED')
        else:
            return HttpResponse('INVALID WEBPAGE')

    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AMFO=AccessForm()
    d={'AMFO':AMFO}
    if request.method=="POST":
        AFO=AccessForm(request.POST)
        if AFO.is_valid():
            AFO.save()
            return HttpResponse('ACCESS RECORD INSERTED')
        else:
            return HttpResponse('INVALID ACCESS RECORD')
        
    return render(request,'insert_access.html',d)