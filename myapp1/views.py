from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import Operatelog
from django.contrib.auth.models import User
from .forms import UserForm
from .forms import UserRegInfoForm

#
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home1(request):
    #return HttpResponse("this is homepage")
    return render(request,"myapp1/Home.html")

#@login_required
#def controllight(request):
    #return render(request,"myapp1/blighta.html")
@login_required
def turn_on(request):
    if request.method=="POST":
        st=request.POST.get('control1')
        ope=Operatelog(status=st)
        ope.save()
        return render(request,"myapp1/SmartHubadmin.html")
    return render(request,"myapp1/blighta.html")
def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        register_form=UserRegInfoForm(data=request.POST)

        if user_form.is_valid() and register_form.is_valid():
            user=user_form.save(commit=False)
            #Encrypt password
            user.set_password(user.password)
            #Split full name into first and last name
            full_name=user_form.cleaned_data['full_name']
            parts=full_name.split(" ", 1)
            user.first_name=parts[0]
            if len(parts) > 1:
                user.last_name=parts[1]
            user.save()

            profile2=register_form.save(commit=False)
            profile2.user=user
            profile2.save()

            registered=True
        else:
            print(user_form.errors, register_form.errors)
    else:
        user_form=UserForm()
        register_form=UserRegInfoForm()
    return render(request,"myapp1/Signup.html",context={'user_form':user_form, 'register_form':register_form, 'registered':registered})
def user_login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user_obj=User.objects.get(email=email)
            username=user_obj.username
        except User.DoesNotExist:
            username=None

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('myapp1:home2'))
                #return redirect('myapp1:home2')
            else:
                return HttpResponse("Your account is inactive.")
        else:
            print("Login failed")
            return HttpResponse("Invalid login details")
    else:
        return render(request,"myapp1/Login.html")
@login_required
def home2(request):
    #return HttpResponse("this is homepage")
    return render(request,"myapp1/SmartHubadmin.html")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp1:home1'))
    #return redirect('myapp1:home1')

@login_required
def get_status(request):
    #return HttpResponse("this is output page")
    bobj=Operatelog.objects.last()
    status_value=bobj.status
    return JsonResponse({'statuso':status_value})
