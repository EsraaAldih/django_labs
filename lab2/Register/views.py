from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import myuser
from django.contrib.auth.models import User

# Create your views here.
def registeruser(req):
    context = {}
    if(req.method=='GET'):
        return  render(req,'register.html')
    else:
        username = req.POST['username']
        password = req.POST['pass']
        repeatPassword=req.POST['repass']
        email=req.POST['email']

        #cretae myuser
        new_user= myuser.objects.create(name=username,email=email,password=password,repeatPassword=repeatPassword,)
        User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        req.session['user'] =  username

        return redirect('/home')

def login(request):
    context={}
    if(request.method=='GET'):
        # context['users']=myuser.objects.all()
        # return render(request, 'login.html',context)
        return render(request, 'login.html')
    else:
        #check for user and passs
        email=request.POST['email']
        password=request.POST['pass']
        #if correct
        user= myuser.objects.filter(email=email,password=password)
        if(len(user)>0):
            user=user[0]
        if(user):
            #go to home page
            # request.session['user'] =  username
            return HttpResponseRedirect('/home')

        else:
            #else print errr statment
            context['errormsg']='invalid cred.'
            return render(request, 'login.html', context)


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect(login)
    return redirect(login)