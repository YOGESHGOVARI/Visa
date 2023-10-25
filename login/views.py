from django.http  import HttpResponse
from django.shortcuts import render
from details.models import Details
from details.models import A_Details

def home(request):
    return render(request,'eng.html')

def arab(request):
    return render(request,'arab.html')

def save_e(request):
    if request.method=='POST':
        uname=request.POST.get('usrnm')
        passw=request.POST.get('passw')
        en=Details(uname=uname,passw=passw)
        en.save()
    return render(request,'eng.html')

def save_a(request):
    if request.method=='POST':
        uname1=request.POST.get('usrname')
        passw1=request.POST.get('password')
        print(uname1,passw1)
        ab=A_Details(uname1=uname1,passw1=passw1)
        ab.save()
    return render(request,'arab.html')