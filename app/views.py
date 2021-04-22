from django.shortcuts import render
from app.models import *

# Create your views here
def display_topic(request):
    topics=Topic.objects.all()

    topics={'topics':topics}
    return render(request,'display_topic.html',topics)

def display_webpage(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(url__startswith='http://')
    webpages=Webpage.objects.filter(url__endswith='o/')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by('-topic_name')
    webpages=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{1}h')
    webpages=Webpage.objects.filter(topic_name__in=['WWE','Swimming'])
    w1={'webpages':webpages}
    return render(request,'display_webpage.html',w1)
def display_access(request):
    acess=Access_Records.objects.all()
    acess=Access_Records.objects.filter(date__year__gte='1998')
    acess=Access_Records.objects.filter(date__month__gte='6')
    acess=Access_Records.objects.filter(date__day__gte='11')
    acess=Access_Records.objects.all().order_by('name')
    acess=Access_Records.objects.all().order_by('-name')
    a={'acess':acess}
    return render(request,'display_access.html',a)    