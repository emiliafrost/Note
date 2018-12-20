from django.shortcuts import render,HttpResponse


# Create your views here.
def booking(request):
    # return render(request,'login/index.html')
    return HttpResponse('hello, this is booking')