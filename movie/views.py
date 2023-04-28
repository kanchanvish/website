from django.shortcuts import render
from .models import Customer, Carrers, portfolio as Portfolio
from django.core.mail import send_mail,EmailMessage
from django.conf import settings


# Create your views here.

def index(request):
    return render(request,"movie/index.html")

def about(request):
    return render(request,"movie/about.html")

def contact(request):
    if request.POST:
        name = request.POST['volunteer-name']
        email = request.POST['volunteer-email']
        service_type = request.POST['service_type']
        comment = request.POST['volunteer-message']
        # print(name, email, service_type)
        subject = 'Responce of user'
        message = 'You responce is' + '\n' + 'name:'+ ' '+ name + '\n' +'email :'+' '+ email + '\n' +'servive type :'+''+ service_type + '\n' + 'comment:'+' '+comment
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['kanchanvishwakarma199@gmail.com',]
        send_mail(subject, message, email_from, recipient_list)

    return render(request,"movie/contact.html")

def service(request):
    return render(request,"movie/service.html")

def service_details(request):
    return render(request,"movie/services_details.html")

# def comming_soon(request):
#     return render(request,"movie/comming_soon.html")

# def page_404(request):
#     return render(request,"movie/page_404.html")

def gallary(request):
    gallary_data = Portfolio.objects.all()
    context = {
        'gallary_data' : gallary_data
    }
    return render(request,"movie/gallary.html", context)


def carrier(request):
    carrer_data = Carrers.objects.all()
    context = {
        'carrer_data' : carrer_data
    }
    return render(request,"movie/carrier.html", context)


def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'contect.html', context)

def jobs(request, id):
    print(id)
    job_data = Carrers.objects.get(id=id)
    context = {
        'job' : job_data
    }
    return render(request,"movie/product.html", context)


def register(request):
     print(request.method)
     if request.POST:
        print(request.FILES)
        name = request.POST['fullname']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        zip = request.POST['zip']
        telephone = request.POST['tel']
    
        # upload_your_CV = request.POST['file']
        upload_your_CV = request.FILES['myfile']
        # print(name, email, service_type)
        subject = 'Responce of user'
        message = 'You responce is' + '\n' + 'name:'+' ' + name + '\n' +'email:'+' '+email + '\n' + 'address :' +' ' +address + '\n' + 'city :'+' '+ city + '\n' + 'zip :'+' '+ zip + '\n' + 'telephone :' +' '+ telephone 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['kanchanvishwakarma199@gmail.com',]
        mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        mail.attach(upload_your_CV.name, upload_your_CV.read(), upload_your_CV.content_type)
        mail.send()
        # subject = 'Responce of user'
        # message = 'You responce is' + '\n' + name + '\n' + email + '\n' + address + '\n' + city + '\n' + zip + '\n' + telephone + '\n' + start_date  + '\n' + upload_your_CV
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['kanchanvishwakarma199@gmail.com',]
        # send_mail(subject, message, email_from, recipient_list, fail_silently=False)

     return render(request,"movie/register.html")


def web(request):
    return render(request,"movie/web.html")



def description(request,id):
    print(id)
    portfolio = Portfolio.objects.get(id=id)
    context = {
        'portfolio' : portfolio
    }
    return render(request,"movie/description.html", context)