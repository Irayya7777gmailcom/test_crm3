# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
#     # path('adminstrator_signin',views.signin,name='signin'),
#     # path('adminstrator_login',views.login,name='login'),
     path('adminstrator_home',views.adminstrator_home,name='adminstrator_home'),
     path('admin-page-clientleads',views.admin_page_clientleads,name='admin-page-clientleads'),
     path('admin-page-customerleads',views.admin_page_customerleads,name='admin-page-customerleads')
#     # path('import_csv',views.import_csv,name='import_csv')
    
 ]