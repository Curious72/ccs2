from django.shortcuts import render
from social.models import users
from social.forms import form1
from django.http import HttpResponseRedirect
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
        g=users(name=form['name'],password=form['password'],email=form['email'],usertype=form['usertype'],branch=form['branch'])
        g.save()
        
        return HttpResponseRedirect("/profile.html")

def login(request):
    if "username" in request.session:
        return render(request,"redirect.html",{'name':request.session['username']})
    else:
        return render(request,"login.html")
    
def auth(request):
    try:
      
      j=users.objects.get(name=request.POST['name'],password=request.POST['password'])
      request.session['username']=request.POST['name']
      return render(request,"profile.html")
    except users.DoesNotExist:
       return render(request,"login.html",{'errors':True})