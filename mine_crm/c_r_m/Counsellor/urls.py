from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
#     # path('councellor_signin',views.signin,name='signin'),
#     # path('councellor_login',views.login,name='councellor_login'),
     path('councellor_home',views.home,name='councellor_home'),
     path('councellor-page-clientleads',views.councellor_page_clientleads,name='councellor-page-clientleads'),
     path('councellor-page-customerleads',views.councellor_page_customerleads,name='councellor-page-customerleads'),
     path('councellor-client-follow-up/<str:stage>',views.followup_record,name='councellor-client-follow-up'),
     path('councellor-client-prospect/<str:stage>',views.prospects_record,name='councellor-client-prospect'),
     path('councellor-client-registered',views.registered_record,name='councellor-client-registered'),
     path('councellor-clientrecord-close/<str:stage>',views.closed_record,name='councellor-clientrecord-close'),
     path('councellor-activities',views.councellor_activities,name='councellor-activities'),

     path('councellor-activity-count/<stage>',views.councellor_activity_count,name='councellor-activity-count'),

    #  path('councellor-callcount',views.councellor_callcount,name='councellor-callcount'),
    #  path('councellor-messagecount',views.councellor_messagecount,name='councellor-messagecount'),
    #  path('councellor-mailcount',views.councellor_mailcount,name='councellor-mailcount'),
    #  path('councellor-whatsappcount',views.councellor_whatsappcount,name='councellor-whatsappcount'),
    #  path('councellor-councellingcount',views.councellor_councellingcount,name='councellor-councellingcount'),
    #  path('councellor-collegevisitcount',views.councellor_collegevisitcount,name='councellor-collegevisitcount'),
    #  path('councellor-corporatecount',views.councellor_corporatecount,name='councellor-corporatecount'),
]