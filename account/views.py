from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from .models import CustomerUserModel

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contactus.html')

def about(request):
    return render(request, 'aboutus.html')

def loging(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = authenticate(request,username=username ,password=password)
        if customer is not None:
            login(request, customer)
            return redirect('dashboard')
        return  HttpResponse('login failed......')
    
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:  #checking if both password matches
            return render(request, 'signup.html', {'error': 'Password doesnot match'})
        if CustomerUserModel.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already existed'})
        if CustomerUserModel.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already existed'})
        
        CustomerUserModel.objects.create(username=username, email=email, password=make_password(password), confirm_password=make_password(confirm_password))
        # customer.save()
        return HttpResponse('Account Created Successfully')

    return render(request, 'signup.html')
# Create your views here.
