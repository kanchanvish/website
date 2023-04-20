from django.shortcuts import render
from .models import Customer
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def index(request):
    return render(request,"movie/index.html")

def about(request):
    return render(request,"movie/about.html")

def contect(request):
    if request.POST:
        name = request.POST['volunteer-name']
        email = request.POST['volunteer-email']
        service_type = request.POST['service_type']
        comment = request.POST['volunteer-message']
        print(name, email, service_type)
        subject = 'Responce of user'
        message = 'You responce is' + '\n' + name + '\n' + email + '\n' + service_type + '\n' + comment
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['kanchanvishwakarma199@gmail.com',]
        send_mail(subject, message, email_from, recipient_list)

    return render(request,"movie/contect.html")

def service(request):
    return render(request,"movie/service.html")

def service_details(request):
    return render(request,"movie/services_details.html")

def comming_soon(request):
    return render(request,"movie/comming_soon.html")

def page_404(request):
    return render(request,"movie/page_404.html")

def gallary(request):
    return render(request,"movie/gallary.html")

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'contect.html', context)
