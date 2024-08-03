from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, get_user_model, logout
from .models import User
from arizalar.models import Yangiliklar


@csrf_exempt
def home(request):
    data = Yangiliklar.objects.all()
    
    contex = {
        'data':data,
    }
    return render(request, 'asosiy/home.html', contex)


@csrf_exempt
def chiqish(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def kirish(request):
    data = 'Kirish sahifasi'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user.save()
            return redirect('/')
        else:
            messages.warning(request, 'Id yoki parol xato')
            return redirect('/kirish') 
            
    contex = {
        'data':data,
    }
    return render(request, 'asosiy/kirish.html', contex)


@csrf_exempt
def superadmin_qoshish(request):    
    habar = ''
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']                     
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username):
            habar = 'Bunday foydalanuvchi mavjud'                  
        else:
            user = get_user_model().objects.create(
                lavozim='super', username = username, last_name = last_name, 
                first_name = first_name,
                password = make_password(password1), parol=password2
            )
            user.is_active = False
            user.is_staff = False 
            return redirect('/')  
    contex = {        
        'habar':habar,
    }
    return render(request, 'asosiy/royhat.html', contex)