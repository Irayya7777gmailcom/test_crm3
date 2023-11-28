from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
   path('tellecaller-home',views.home,name='tellecaller-home'),
   path('tellecaller-page-clientleads',views.tellecaller_page_clientleads,name='tellecaller-page-clientleads'),
   path('tellecaller-page-customerleads',views.tellecaller_page_customerleads,name='tellecaller-page-customerleads'),

   path('tellecaller-client-follow-up/<str:stage>',views.followup_record,name='tellecaller-client-follow-up'),
     path('tellecaller-client-prospect/<str:stage>',views.prospects_record,name='tellecaller-client-prospect'),
     path('tellecaller-client-registered',views.registered_record,name='tellecaller-client-registered'),
     path('tellecaller-clientrecord-close/<str:stage>',views.closed_record,name='tellecaller-clientrecord-close'),
]