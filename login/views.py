from django.shortcuts import render, redirect
from django.conf import settings
from . import models
import re


# Create your views here.
def index(request):
    if request.session.get('is_login', None):
        return render(request, 'login/index.html', {'message': 'hello! '+request.session.get('user_username')})
    return render(request,'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        # repeat login is not allowed
        return render(request, 'login/index.html', {"message": "You've already logged in."})
    if request.method == "POST":
        # 这个None是指，当请求数据中没有键值时，不抛出异常而是返回我们指定的默认值None
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        remember = request.POST.get('remember', None)
        if remember:
            request.session.set_expiry(60*60*24*3)
        if username and password:
            # username = username.strip()  # remove space in username
            umatch = re.match(r'^[\d\w_]{5,}$', username)
            pmatch = re.match(r'^([*?_\w]*\d+[*?_\w]*)$', password)
            message = "Invalid attempt."
            if umatch and pmatch:  # if username and password are legal
                try:
                    user = models.User.objects.get(username=username)
                    if user.password == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_username'] = user.username
                        return render(request, 'login/index.html', {"message": "hello! "+username})
                    else:
                        message = "Wrong password, please try again."
                except:
                    message = "Username does not exist, please register."
            return render(request, 'login/login.html', {"message": message})
    return render(request, 'login/login.html')


def register(request):
    if request.session.get('is_login', None):
        # status login is not allowed
        return render(request, 'login/index.html', {"message": "You've already logged in."})
    if request.method == "POST":
        # 这个None是指，当请求数据中没有键值时，不抛出异常而是返回我们指定的默认值None
        username = request.POST.get('username', None)
        name = request.POST.get('name', None)
        address = request.POST.get('address', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        if password != password2:
            message = "Passwords are different, please input again."
            return render(request, 'login/register.html', {'message': message})
        umatch = re.match(r'^[\d\w_]{5,}$', username)  # the length of username should >=5
        pmatch = re.match(r'^[*?_\w\d]*$', password)  # the length of password should >6
        if umatch and pmatch:  # if username, password and phone are valid
            same_username = models.User.objects.filter(username=username)
            same_email = models.User.objects.filter(email=email)
            if same_username:
                message = "Username already exists, please login or create a new one"
                return render(request, 'login/register.html', {'message': message})
            if same_email:
                message = "Email address already exists, please login or use a new one"
                return render(request, 'login/register.html', {'message': message})
            # if username, password, phone number and email are fine, then:
            new_user = models.User()
            new_user.username = username
            new_user.name = name
            new_user.HomeAddress = address
            new_user.phoneNo = phone
            new_user.email = email
            new_user.password = password
            new_user.save()
            send_email(username, password, email)
            return redirect('/login/')
        else:   # if one (or more) of username, password or phone is invalid
            message = ""
            if not umatch:
                message = "Invalid username, can only contain A-Z, a-z, 0-9, the length should >5. "
            if not pmatch:
                message = message + "Invalid password, can only contain A-Z, a-z, 0-9 and * _ ?, the length should >6"
            return render(request, 'login/register.html', {'message': message})
    return render(request, 'login/register.html')

def logout(request):
    if request.session.get('is_login', None):
        request.session.flush()
    return redirect("/index/")


def send_email(username, password, email):
    from django.core.mail import EmailMultiAlternatives
    subject, from_email = 'Register successfully - from Shipping Site', 'forshippingsite@sina.com'
    text_content = 'You have created an account successfully! Please remember your username and password.'
    html_content = '<p>Dear Customer: </p>' \
                   '<p>&emsp;&emsp;You have created an account successfully!</p>' \
                   '<p>&emsp;&emsp;Please remember your username and password listed below:' \
                   '<p> <strong>&emsp;&emsp;Username: </strong> {} </p>'\
                   '<p> <strong>&emsp;&emsp;Password: </strong> {} </p>'.format(username, password)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()