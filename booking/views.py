from django.shortcuts import render, get_object_or_404
from . import models
from login import models as loginmodels


# Create your views here.
def bookings(request):
    if not request.session.get('is_login', None):
        # if the user is not log in
        return render(request, 'login/index.html', {"message": "Please login or register"})
    # if the user logged in
    username = request.session.get('user_username', None)
    user = get_object_or_404(loginmodels.User, username=username)
    # 现在到这行，能找到在User表里对应的User了，之后参考第一个project的外键写法
    if user:
        message = 'hello'
        return render(request, 'booking/bookings.html', {'message': message})
    return render(request, 'login/index.html')