from django.shortcuts import render
from social.models import users , announcements ,  complaints , assignments , curriculum
from social.forms import form1
from django.http import *
from django.contrib.auth.models import User
import datetime
# Create your views here.

def  signup(request):
    if "username" in request.session:
       return render(request,"redirect.html",{'name':request.session['username']})
    else:
        cform=form1()
        return render(request,"form.html",{'form':cform})
    
def tq(request):
    form=form1(request.POST)
    if form.is_valid():
        form=form.cleaned_data
        g=users(name=form['name'],password=form['password'], year=form['year'],email=form['email'],usertype=form['usertype'],branch=form['branch'])
        ty= User(username=form['name'],password=form['password'])
        g.save()
        ty.save()
        
        return HttpResponseRedirect("/login")

def login(request):
    if "username" in request.session:
        return render(request,"redirect.html",{'name':request.session['username']})
    else:
        return render(request,"login.html")
    
def auth(request):
    try:
        
      j=users.objects.get(name=request.POST['name'],password=request.POST['password'])
      k=users.objects.filter(name=request.POST['name'],password=request.POST['password'])
      for i in k:
          request.session['usertype']=i.usertype
        
      
      #print type(j)
      #po=list(j)
    
      
      request.session['username']=request.POST['name']
      request.session['password']=request.POST['password']
      return HttpResponseRedirect("/home1")
    except usersi.DoesNotExist:
       return render(request,"login.html",{'errors':True})
    
def home(request,value):
    if value =="1":
        if 'text' in request.POST:
            y=announcements(name=request.session['username'],text=request.POST['text'],time=datetime.datetime.now())
            y.save()
        j=announcements.objects.order_by("-time")
    if value =="2":
        if 'text' in request.POST:
           y=complaints(name=request.session['username'],text=request.POST['text'],time=datetime.datetime.now())
           y.save()
        j=complaints.objects.order_by("-time")
    if value =="3":
        if 'text' in request.POST:
           y=assignments(name=request.session['username'],text=request.POST['text'],time=datetime.datetime.now())
           y.save()
        j=assignments.objects.order_by("-time")
    if value =="4":
        if 'text' in request.POST:
           y=curriculum(name=request.session['username'],text=request.POST['text'],time=datetime.datetime.now())
           y.save()
        j=curriculum.objects.order_by("-time")
    print value
    return render(request,"home.html",{'data':j,'value':value,'type':request.session['usertype']})

def logout(request):
    del request.session['username']
    del request.session['usertype']
    return HttpResponseRedirect("/welcome")


def welcome(request):
    return render(request,"welcome.html")
