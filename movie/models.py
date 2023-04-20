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
