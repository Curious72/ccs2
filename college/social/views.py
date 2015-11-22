from django.shortcuts import render
from social.models import users , announcements ,  complaints , assignments , curriculum
from social.forms import form1
from django.http import *
from django.contrib.auth.models import User
import datetime
from djangoChat.models import ChatUser
from django.contrib import auth
from django.utils.timezone import now as utcnow

# Create your views here.

def  signup(request):
    if "username" in request.session:
       return render(request,"Logout.html",{'name':request.session['username']})
    else:
        cform=form1()
        return render(request,"form.html",{'form':cform})
    
def tq(request):
    form=form1(request.POST)
    if form.is_valid():
        form=form.cleaned_data
        g=users(name=form['name'],password=form['password'], year=form['year'],email=form['email'],usertype=form['usertype'],branch=form['branch'])
        ty= User.objects.create_user(username=form['name'],email=form['email'],password=form['password'])
        g.save()
        username = form['name'] #retunr '' if no username
        password = form['password']
        pi=ChatUser(username=username,is_chat_user=True)
        return HttpResponseRedirect("/login")

def login(request):
    if "username" in request.session:
        return render(request,"Logout.html",{'name':request.session['username']})
    
    else:
        return render(request,"login.html")
    
def autho(request):
    try:
        
      j=users.objects.get(name=request.POST['name'],password=request.POST['password'])
      k=users.objects.filter(name=request.POST['name'],password=request.POST['password'])
      for i in k:
          request.session['usertype']=i.usertype
          
      t= request.session['usertype']
      name=request.POST['name']
      password=request.POST['password']
      user=auth.authenticate(username=name,password=password)
      auth.login(request,user)
      cu = request.user.profile
      cu.is_chat_user = True
      cu.last_accessed = utcnow()
      cu.save()
      request.session['username']=name
      request.session['password']=password
      request.session['usertype']=t
      return HttpResponseRedirect("/index")
    except users.DoesNotExist:
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
    return render(request,"in.html",{'data':j,'value':value,'type':request.session['usertype'],'bool':True})

def logout(request):
    del request.session['username']
    #del request.session['usertype']
    return HttpResponseRedirect("/welcome")


def welcome(request):
    return render(request,"guest.html")
def index(request):
    return render(request,"index.html")
def intr(request):
        return render(request,"in.html")

