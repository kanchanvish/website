from django.urls import path

from . import views

urlpatterns=[
    path('index/',views.index),
    path('about/',views.about),
    path('service/',views.service),
    path('contact/',views.contact),
    path('services_details/',views.service_details),
    # path('page_404/',views.page_404),
    # path('comming_soon/',views.comming_soon),
    path('gallary/',views.gallary),
    path('carrier/',views.carrier),
    path('carrier/<int:id>/',views.jobs),
    path('register/',views.register),
    path('web/',views.web),
 
]