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
    user_id = request.session.get('user_id', None)
    user = get_object_or_404(loginmodels.User, pk=user_id)
    # 如果在已注册用户中找不到这个用户，就会报错。目前只要正常登陆，就可以找到user
    try:
        results = user.booking_set.order_by('-crttime')  # results里是这个user的全部booking
        return render(request, 'booking/bookings.html', {'results': results})
    except:
        return render(request, 'booking/bookings.html')


def create(request):
    if not request.session.get('is_login', None):
        # if the user is not log in
        return render(request, 'login/index.html', {"message": "Please login or register"})
    listi = range(1, 11)  # i is used in #boxes
    listdate = []
    for i in range(5, 13):
        time = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime('%Y-%m-%d, %A')
        listdate.append(time)
    if request.method == "POST":
        numboxes = request.POST.get('#boxes', None)
        Daddress = request.POST.get('daddress', None)
        Paddress = request.POST.get('paddress', None)
        shipdate = request.POST.get('shipdate', None)
        shiptime = request.POST.get('shiptime', None)
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
        new_booking.shipdate = shipdate + ' ' + shiptime
        new_booking.messages = messages
        new_booking.save()
        new_ack = models.Ack()
        new_ack.booking = new_booking
        new_ack.cost = ('%.2f' % float(int(numboxes) * 35.00))
        new_ack.pickuptime = 'Null'
        new_ack.status = 'To be Approved'
        new_ack.HBLnum = 'Null'
        new_ack.messagec = 'Null'
        new_ack.save()
        return redirect('/bookings/')
    return render(request, 'booking/create.html', {'listdate': listdate, 'listi': listi})


def details(request, booking_id):
    if not request.session.get('is_login', None):
        # if the user is not log in
        return render(request, 'login/index.html', {"message": "Please login or register"})
    # if the user logged in
    current_user = request.session.get('user_username', None)
    if current_user != 'susanto111':
        user = get_object_or_404(loginmodels.User, pk=request.session.get('user_id', None))
        results = user.booking_set.get(pk=booking_id)  # results = current booking
        temp = float(results.numboxes * 35)
        price = ('%.2f' % temp)
        try:
            acks = models.Ack.objects.get(booking=results)
            return render(request, 'booking/details.html', {
                'results': results,
                'price': price,
                'acks': acks,
            })
        except:
            return render(request, 'booking/details.html', {
                'results': results,
                'price': price,
            })
    else:
        results = models.Booking.objects.get(pk=booking_id)
        temp = float(results.numboxes * 35)
        price = ('%.2f' % temp)
        try:
            acks = models.Ack.objects.get(booking=results)
            return render(request, 'booking/details.html', {
                'results': results,
                'price': price,
                'acks': acks,
            })
        except:
            return render(request, 'booking/details.html', {
                'results': results,
                'price': price,
            })


def ack(request):
    if not request.session.get('is_login', None):
        # if the user is not log in
        return render(request, 'login/index.html', {"message": "Please login or register"})
    # if the user logged in
    current_user = request.session.get('user_username', None)
    if current_user != 'susanto111':
        # if the user is not susanto111
        return render(request, 'login/index.html', {"message": "Access Denied"})
    # if the user is administrator
    allbookings = models.Booking.objects.order_by('-crttime')
    return render(request, 'booking/ack.html', {
        'allbookings': allbookings,
    })


def ackdetail(request, booking_id):
    if not request.session.get('is_login', None):
        # if the user is not log in
        return render(request, 'login/index.html', {"message": "Please login or register"})
    current_user = request.session.get('user_username', None)
    if current_user != 'susanto111':
        # if the user is not susanto111
        return render(request, 'login/index.html', {"message": "Access Denied"})
    thisbooking = models.Booking.objects.get(pk=booking_id)
    thisack = models.Ack.objects.get(booking=thisbooking)
    return render(request, 'booking/ackdetail.html', {
        'booking_id': booking_id,
        'thisack': thisack,
        'thisbooking': thisbooking,
    })
