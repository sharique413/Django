from django.http.response import HttpResponseServerError
from django.shortcuts import render, HttpResponse
from datetime import datetime
from app.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')
def servicess(request):
    return render(request, 'servicess.html')

def contact(request):
    if request.method =="POST":
        email= request.POST.get('email')
        name= request.POST.get('name')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact=Contact(email=email, name=name, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been send!')
    return render(request, 'contact.html')