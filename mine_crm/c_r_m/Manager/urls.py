from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
#     # path('councellor_signin',views.signin,name='signin'),
#     # path('councellor_login',views.login,name='councellor_login'),
     path('manager-home',views.home,name='manager-home'),
     path('manager-page-clientleads',views.manager_page_clientleads,name='manager-page-clientleads'),
     path('manager-page-customerleads',views.manager_page_customerleads,name='manager-page-customerleads'),
     path("add-customer-record",views.add_customer_record,name='add-customer-record'),
     path('add-client-record',views.add_client_record,name='add-client-record'),
     path('client-info/<int:id>',views.client_info,name='client-info'), 
     path('manager-client-follow-up/<str:stage>',views.followup_record,name='manager-client-follow-up'),
     path('manager-client-prospect/<str:stage>',views.prospects_record,name='manager-client-prospect'),
     path('manager-client-registered',views.registered_record,name='manager-client-registered'),
     path('manager-clientrecord-close/<str:stage>',views.closed_record,name='manager-clientrecord-close'),
     path('manager-activities',views.manager_activities,name='manager-activities'
          ),
     path('manager_activity_count',views.manager_activity_count,name='manager_activity_count'),
     path('assign_to/<lead>/<int:id>/<checks>',views.assign_to),    
     path('bar-chart/', views.bar_chart_view, name='bar_chart'),

    path('import/', views.import_data, name='import'),
    path('export', views.export_data, name='export'),
]