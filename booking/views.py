from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import datetime
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
    # 如果在已注册用户中找不到这个用户，就会报错
    try:
        results = user.booking_set.all  # 不要再重复筛uername
        print('yes')
        return render(request, 'booking/bookings.html', {'results': results})
    except:
        return render(request, 'booking/bookings.html')


def create(request):
    if not request.session.get('is_login', None):
        # if the user is not log in
        return render(request, 'login/index.html', {"message": "Please login or register"})
    listi = range(1, 11)  # i is used in #boxes
    listdate = []
    for i in range(1, 8):
        time = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        listdate.append(time)
    if request.method == "POST":
        numboxes = request.POST.get('#boxes', None)
        Daddress = request.POST.get('daddress', None)
        Paddress = request.POST.get('paddress', None)
        shipdate = request.POST.get('shipdate', None)
        messages = request.POST.get('messages', None)
        username = request.session.get('user_username', None)
        if not messages:
            messages = 'Null'
        user = get_object_or_404(loginmodels.User, username=username)
        new_booking = models.Booking()
        new_booking.username = user
        new_booking.numboxes = numboxes
        new_booking.Daddress = Daddress
        new_booking.Paddress = Paddress
        new_booking.shipdate = shipdate
        new_booking.messages = messages
        new_booking.save()
        return redirect('/bookings/')
    return render(request, 'booking/create.html', {'listdate': listdate, 'listi': listi})


def bookingdetail(request):
    return 0