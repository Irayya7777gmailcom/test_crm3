from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as dj_login,logout
from django.http import HttpResponse
from . models import CustomerLeads,ClientLeads,UserProfile
from django.urls import reverse

    
def adminstrator_home(request):
    if request.user.is_authenticated:
        desig=UserProfile.objects.get(user=request.user).designation
        #admin_url = reverse('admin/')
        #CLIENTS
        client_leads= ClientLeads.objects.filter(stage='newlead')
        client_followup_leads= ClientLeads.objects.filter(stage='followup')
        client_closed_leads=ClientLeads.objects.filter(stage='closed')
        client_prospect_leads=ClientLeads.objects.filter(stage='prospect')
        client_registered_leads=ClientLeads.objects.filter(stage='registered')
        #CUSTOMERS
        customer_leads= ClientLeads.objects.filter(stage='newlead')
        customer_followup_leads= CustomerLeads.objects.filter(stage='followup')
        customer_closed_leads=CustomerLeads.objects.filter(stage='closed')
        customer_prospect_leads=CustomerLeads.objects.filter(stage='prospect')
        customer_registered_leads=CustomerLeads.objects.filter(stage='registered')
        data_labels = ["Client leads + Customer Leads", "ClientFollowups + CustomerFollowups", "ClientProspects + CustomerProspects","ClientClosed + prospectClosed","ClientRegistered + CustomerRegistered",]
        data_values = [customer_leads.count()+client_leads.count(),
                       client_followup_leads.count()+customer_followup_leads.count(),
                       client_prospect_leads.count()+customer_prospect_leads.count(),
                       client_closed_leads.count()+customer_closed_leads.count(),
                       client_registered_leads.count()+customer_registered_leads.count()
                       ]
        naukri_source= ClientLeads.objects.filter(source='naukri').count()+CustomerLeads.objects.filter(source='naukri').count()
        indeed_source= ClientLeads.objects.filter(source='indeed').count()+CustomerLeads.objects.filter(source='indeed').count()
        foundit_source= ClientLeads.objects.filter(source='foundit').count()+CustomerLeads.objects.filter(source='foundit').count()
        mail_source= ClientLeads.objects.filter(source='mail').count()+CustomerLeads.objects.filter(source='mail').count()
        whatsapp_source= ClientLeads.objects.filter(source='whatsapp').count()+CustomerLeads.objects.filter(source='whatsapp').count()
        justdial_source= ClientLeads.objects.filter(source='justdial').count()+CustomerLeads.objects.filter(source='justdial').count()

        # python_course= ClientLeads.objects.filter(stage='newlead',course='python').count()
        # java_source= ClientLeads.objects.filter(stage='followup').count()
        # webdesigning_source= ClientLeads.objects.filter(stage='prospect').count()
        # marketing_source= ClientLeads.objects.filter(stage='closed').count()
        

        data={
            
            
            'user': request.user,
            'admin_url': 'admin',
            'new_leads_count':customer_leads.count()+client_leads.count(),
            'followup_count':client_followup_leads.count()+customer_followup_leads.count(),

            
            'closed_count':client_closed_leads.count()+customer_closed_leads.count(),
                  
            'prospect_count':client_prospect_leads.count()+customer_prospect_leads.count(),
            
            'registered_count':client_registered_leads.count()+customer_registered_leads.count(),

            'designation':desig,         
            'labels': data_labels,
            'values': data_values,
            'naukri_source':naukri_source, 
            'indeed_source': indeed_source,
            'foundit_source':foundit_source,
            'mail_source':  mail_source,
            'whatsapp_source': whatsapp_source,
            'justdial_source':justdial_source,
            'source_data': [naukri_source, indeed_source, mail_source, whatsapp_source, foundit_source, justdial_source],
            'course_data':[]
        }
        return render(request,'Adminstrator_templates/admin-dashboard.html',data)
    else:
        return render(request,'401.html')
    

def admin_page_clientleads(request):
    if request.user.is_authenticated:
        leads = CustomerLeads.objects.all()
        return render(request,'Adminstrator_templates/admin-page-clientleads.html',{'user':request.user})
    else:
        return HttpResponse("Adminstrator is not logged in. Please log in first.")



def admin_page_customerleads(request):
    if request.user.is_authenticated:
        leads = CustomerLeads.objects.all()
        return render(request,'Adminstrator_templates/admin-page-customerleads.html',{'user':request.user})
    else:
        return HttpResponse("Adminstrator is not logged in. Please log in first.")
    



# from tablib import Dataset
# from .models import csv
# from .resources import PersonResource
# def import_csv(request):
#     if request.method=='POST':
#         person_resource=PersonResource()
#         dataset=Dataset()
#         new_persons=request.FILES['my_file']
#         imported_data=dataset.load(new_persons.read(),format="xlsx")

#         for data in imported_data:
#             value=csv(
#                 data[0],
#                 data[1],
#                 data[2]
#             )
#             value.save()
#     return render(request,'adminstratortemplates/csv_data.html')