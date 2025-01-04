from django.shortcuts import render,redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import *
import requests
import os
def index(request):
    return render(request, "index.html")
def contact(request):
    return render(request, "contact.html")
def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect('login')
def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect('login')
def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Username or Password is incorrect')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            try:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.success(request,'User created successfully')
                return redirect('login')
            except:
                messages.error(request,'Username already exists')
        else:
            messages.error(request,'Password and Confirm Password must be same')
    return render(request,'signup.html')

from django.http import JsonResponse
from urllib.parse import urlencode

def generate_image(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '').strip()
        if not prompt:
            return JsonResponse({'error': 'Prompt is required.'}, status=400)

        try:
            # Construct the image URL
            base_url = "https://image.pollinations.ai/prompt/"
            image_url = f"{base_url}{prompt.replace(' ', '%20')}"

            return JsonResponse({'image_url': image_url})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Deletes the user from the database
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')  # Redirect to homepage or login page
    return render(request, 'profile.html')


