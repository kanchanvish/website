from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    SERVICE_TYPE_CHOICES = [
        ('WEBDEV', 'Web Development'),
        ('LEADERSHIP', 'Leadership'),
        ('WEBAPP', 'Web Application'),
        ('APPDEPLOY', 'Application Deployment'),
    ]
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)

class Carrers(models.Model):
    job_title = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    Job_Description = models.CharField(max_length=400)
    Responsibilities = models.CharField(max_length=400)
    Requirements = models.CharField(max_length=400)  
    image_path = models.CharField(max_length=100)

class portfolio(models.Model):
    title = models.CharField(max_length=100)
    image_path1 = models.CharField(max_length=300)
    image_path2 = models.CharField(max_length=300)
    image_path3 = models.CharField(max_length=300)
    image_path4 = models.CharField(max_length=300)
    image_path5 = models.CharField(max_length=300)
    des = models.TextField(max_length=1000)
    
