import re
from . import models
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        # repeat login is not allowed, so if the user has logged in, report error.
        return render(request, 'error.html', {
            "message": "You've already logged in, repeat login is not allowed."})
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        remember = request.POST.get('remember', None)
        # This None means that if we cannot find this keyword, return None.
        if remember:
            request.session.set_expiry(60*60*24*3)  # cookie will be remembered for 3 days
        if username and password:
            umatch = username.strip()  # remove space in username
            pmatch = password.strip()
            message = "Invalid input."
            if umatch and pmatch:  # if username and password are legal
                try:
                    user = models.User.objects.get(username=username)
                    if user.password == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_username'] = user.username
                        return redirect('/index/')
                    else:
                        message = "Wrong password, please try again."
                except:
                    message = "Username does not exist, please register."
            return render(request, 'login/login.html', {"message": message})
    return render(request, 'login/login.html')


def register(request):
    if request.session.get('is_login', None):
        # status login is not allowed
        return render(request, 'error.html', {"message": "You've already logged in."})
    if request.method == "POST":
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
        umatch = re.match(r'^[\d\w_]{5,32}$', username)  # the length of username should be 5~32
        pmatch = re.match(r'^[*?_\w\d]{6,32}$', password)  # the length of password should be 6~32
        if umatch and pmatch:  # if username, password and phone are valid
            same_username = models.User.objects.filter(username=username)
            same_email = models.User.objects.filter(email=email)
            if same_username:
                # same username is not allowed
                message = "Username already exists, please login or create a new one"
                return render(request, 'login/register.html', {'message': message})
            if same_email:
                # same email is not allowed
                message = "Email address already exists, please login or use a new one"
                return render(request, 'login/register.html', {'message': message})
            # if username, password, and email address are fine, then:
            new_user = models.User()  # get a new User instance
            new_user.username = username
            new_user.name = name
            new_user.homeAddress = address
            new_user.phoneNo = phone
            new_user.email = email
            new_user.password = password
            new_user.save()  # save the info of new users
            send_email(username, password, email)
            return redirect('/login/')
        else:   # if username or password is invalid
            message = ""
            if not umatch:
                message = "Invalid username, can only contain A-Z, a-z, 0-9, the length should be 5~32. "
            if not pmatch:
                message = message + \
                          "Invalid password, can only contain A-Z, a-z, 0-9 and * _ ?, the length should be 6~32"
            return render(request, 'login/register.html', {'message': message})
    return render(request, 'login/register.html')


def logout(request):
    if request.session.get('is_login', None):
        request.session.flush()
    return redirect("/index/")


def profile(request):
    user = get_object_or_404(models.User, pk=request.session.get('user_id', None))
    if request.method == "POST":
        name = request.POST.get('name', None)
        address = request.POST.get('address', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email', None)
        same_email = models.User.objects.filter(email=email)
        if same_email:
            # same email is not allowed
            message = "Email address already exists, please use another one"
            return render(request, 'login/profile.html', {'message': message})
        new_user = models.User.objects.get(pk=request.session.get('user_id', None))
        new_user.name = name
        new_user.homeAddress = address
        new_user.phoneNo = phone
        new_user.email = email
        new_user.save()  # save the info of current user
        return redirect('/index/')
    return render(request, 'login/profile.html', {'user': user})


def change(request):
    if request.method == "POST":
        prepassword = request.POST.get('prepassword', None)
        newpassword = request.POST.get('newpassword', None)
        password2 = request.POST.get('password2', None)
        user = get_object_or_404(models.User, pk=request.session.get('user_id', None))
        if newpassword != password2:
            message = "Passwords are different, please input again."
            return render(request, 'login/change.html', {'message': message})
        if prepassword != user.password:
            message = "Previous password is wrong, please try again."
            return render(request, 'login/change.html', {'message': message})
        newmatch = re.match(r'^[*?_\w\d]{6,32}$', newpassword)  # the length of password should be 6~32
        if newmatch:
            new_user = models.User.objects.get(pk=request.session.get('user_id', None))
            new_user.password = newpassword
            new_user.save()
            request.session.flush()
            return redirect('/index/')
        else:
            message = "Invalid password, can only contain A-Z, a-z, 0-9 and * _ ?, the length should be 6~32"
            return render(request, 'login/change.html', {'message': message})
    return render(request, 'login/change.html')


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