from home.models import Contact
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse("This is homepage")
    context={"var1" :"hello",
             "var2" :"Sweety"}
    
    return render(request,'index.html',context)
def about(request):
    #return HttpResponse("This is about page")
    return render(request, 'about.html')
def contacts(request):
    #return HttpResponse("This is contact page")
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email,phone=phone, subject=subject, message=message,entrydate=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!!")
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
