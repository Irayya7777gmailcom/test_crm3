from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as dj_login,logout
from django.http import HttpResponse
from Administrator.models import CustomerLeads,ClientLeads,FollowUp,Closed,Prospects,Activities,Registered,UserProfile,EmployeeActivities
from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from datetime import date
from Administrator.forms import CustomerLeadsImportForm, CustomerLeadsExportForm
from import_export.formats.base_formats import XLSX, CSV

def import_data(request):
    if request.method == 'POST':
        form = CustomerLeadsImportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_view')  # Redirect to a success page
    else:
        form = CustomerLeadsImportForm(import_formats=[XLSX, CSV])

        return render(request, 'Manager_templates/importexcel.html', {'form': form})

def export_data(request):
    form = CustomerLeadsExportForm(formats = [XLSX, CSV])
    if request.method == 'POST':
        form = CustomerLeadsExportForm(request.POST)
        if form.is_valid():
            # Process export logic
            response = form.export()
            return response

    return render(request, 'Manager_templates/exportexcel.html', {'form': form})
    

def home(request):
    if request.user.is_authenticated:
        
        desig=UserProfile.objects.get(user=request.user).designation
        
        #CLIENTS
        client_leads= ClientLeads.objects.filter(stage='newlead')
        
        client_followup_leads= ClientLeads.objects.filter(stage='followup')
        client_closed_leads=ClientLeads.objects.filter(stage='closed')
        client_prospect_leads=ClientLeads.objects.filter(stage='prospect')
        client_registered_leads=ClientLeads.objects.filter(stage='registered')
        #CUSTOMERS
        customer_leads= CustomerLeads.objects.filter(stage='newlead')
        
        customer_followup_leads= CustomerLeads.objects.filter(stage='followup')
        customer_closed_leads=CustomerLeads.objects.filter(stage='closed')
        customer_prospect_leads=CustomerLeads.objects.filter(stage='prospect')
        customer_registered_leads=CustomerLeads.objects.filter(stage='registered')
        data_labels = ["New Leads", "Followup", "Prospect","Closed","Registered",]
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
        return render(request, 'Manager_templates/managerdashboard.html', data)
    else:
        return HttpResponse("User is not logged in. Please log in first.")
    
def manager_page_clientleads(request): 
    if request.user.is_authenticated: #business men
        form = CustomerLeadsImportForm(import_formats=[XLSX, CSV])
        desig=UserProfile.objects.get(user=request.user).designation
        customer_leads = CustomerLeads.objects.all()
        client_leads= ClientLeads.objects.filter(stage='newlead')

        followup_leads= ClientLeads.objects.filter(stage='followup')
        closed_leads=ClientLeads.objects.filter(stage='closed')
        prospect_leads=ClientLeads.objects.filter(stage='prospect')
        registered_leads=ClientLeads.objects.filter(stage='registered')

        auth_users=User.objects.all()
        data={
            'form': form,
            'designation':desig,
            'leads': customer_leads, 
            'user': request.user,
            'user_id':request.user.id,
            'newlead_count':customer_leads.count(),
            'client_leads':client_leads,
            'client_lead_count':client_leads.count(),
            'followup':followup_leads,
            'closed':closed_leads,
            'prospect':prospect_leads,
            'followup_count':followup_leads.count(),
            'closed_count':closed_leads.count(),
            'prospect_count':prospect_leads.count(),
            'registered':registered_leads,
            'registered_count':registered_leads.count(),
            'client':'client',
            'auth_users':auth_users,
            'array':'array'
        }

        return render(request, 'Manager_templates/managerpage-clientleads.html', data)
    else:
        return HttpResponse("User is not logged in. Please log in first.")
    
def manager_page_customerleads(request):  #students
    if request.user.is_authenticated:
        #customer_leads = CustomerLeads.objects.all()
        desig=UserProfile.objects.get(user=request.user).designation
        customer_leads= CustomerLeads.objects.filter(stage='newlead')

        followup_leads= CustomerLeads.objects.filter(stage='followup')
        closed_leads=CustomerLeads.objects.filter(stage='closed')
        prospect_leads=CustomerLeads.objects.filter(stage='prospect')
        registered_leads=CustomerLeads.objects.filter(stage='registered')

        auth_users=User.objects.all()

        data={
            
            
            'user': request.user,
            'user_id':request.user.id,
            
            'customer_leads':customer_leads,
            
            'customer_followup':followup_leads,
            'customer_closed':closed_leads,
            'customer_prospect':prospect_leads,
            
            
            'customer_registered':registered_leads,
            
            'client':'client',
            'auth_users':auth_users,
            'array':'array',
            'customer':'customer',
            'designation':desig
        }
        return render(request, 'Manager_templates/managerpage-customerleads.html', data)
    else:
        return HttpResponse("User is not logged in. Please log in first.")
    

def add_client_record(request):
    if request.method=='POST':
        
        created_by=request.POST.get('created_by')
        lead_name=request.POST.get('lead_name')
        contact_number=request.POST.get('contact_number')
        door_number=request.POST.get('door_number')
        street_name=request.POST.get('street_name')
        area=request.POST.get('area')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        enquiry_location=request.POST.get('enquiry_location')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        # photo=request.POST.get('photo')
        master_degree=request.POST.get('master_degree')
        master_specification=request.POST.get('master_specification')
        master_percentage=request.POST.get('master_percentage')
        bachelor_degree=request.POST.get('bachelor_degree')
        bachelor_specification=request.POST.get('bachelor_specification')
        bachelor_percentage=request.POST.get('bachelor_percentage')
        course_enquired=request.POST.get('course_enquired')
        source=request.POST.get('source')
        assigned_to=request.POST.get('assigned_to')
        
        #Extra Fields
        #priority=models.SmallIntegerField(default=0)
        technologies_known=request.POST.get('technologies_known')
        level_of_lead=request.POST.get('level_of_lead')
        company_name=request.POST.get('company_name')
        company_door_number=request.POST.get('company_door_number')
        company_street_name=request.POST.get('company_street_name')
        company_area=request.POST.get('company_area')
        company_city=request.POST.get('company_city')
        company_state=request.POST.get('company_state')
        company_pincode=request.POST.get('company_pincode')
        company_gstnumber=request.POST.get('company_gstnumber')
        company_field=request.POST.get('company_field')
        comapny_website=request.POST.get('comapny_website')
        company_contact_number=request.POST.get('company_contact_number')
        # stage=request.POST.get('stage')
        print("client source is= ",source)
        create_record=ClientLeads.objects.create(

        created_by=str(request.user),
        lead_name=lead_name,
        contact_number=contact_number,
        door_number=door_number,
        street_name=street_name,
        area=area,
        city=city,
        state=state,
        pincode=pincode,
        enquiry_location=enquiry_location,
        dob=dob,
        email=email,
        gender=gender,
        # photo=request.POST.get('photo')
        master_degree=master_degree,
        master_specification=master_specification,
        master_percentage=master_percentage,
        bachelor_degree=bachelor_degree,
        bachelor_specification=bachelor_specification,
        bachelor_percentage=bachelor_percentage,
        course_enquired=course_enquired,
        source=source,
        assigned_to=assigned_to,
        
        #Extra Fields
        #priority=models.SmallIntegerField(default=0)
        technologies_known=technologies_known,
        level_of_lead=level_of_lead,
        company_name=company_name,
        company_door_number=company_door_number,
        company_street_name=company_street_name,
        company_area=company_area,
        company_city=company_city,
        company_state=company_state,
        company_pincode=company_pincode,
        company_gstnumber=company_gstnumber,
        company_field=company_field,
        comapny_website=comapny_website,
        company_contact_number=company_contact_number,
        stage='newlead',
        
        )

        create_record.save()
        messages.success(request, 'Record inserted successfully!')
        return redirect('manager-page-clientleads')

def bar_chart_view(request):
    # Fetch data from your model
    #data_from_model = YourModel.objects.all()  # Retrieve data from your model

    # Prepare the data for the chart
    # labels = [item.label for item in data_from_model]  # Example: List of labels
    # values = [item.value for item in data_from_model]  # Example: List of values
    data_labels = ["New Leadsss", "Followup Leads", "Prospects", "Registered", "Closed"]
    data_values = [100, 20, 30, 40, 1000]
    return render(request, 'leadsChart.html', {
        'labels': data_labels,
        'values': data_values,
    })


def add_customer_record(request):
    if request.method=='POST':
        
        created_by=request.POST.get('created_by')
        lead_name=request.POST.get('lead_name')
        contact_number=request.POST.get('contact_number')
        door_number=request.POST.get('door_number')
        street_name=request.POST.get('street_name')
        area=request.POST.get('area')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        enquiry_location=request.POST.get('enquiry_location')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        # photo=request.POST.get('photo')
        master_degree=request.POST.get('master_degree')
        master_specification=request.POST.get('master_specification')
        master_percentage=request.POST.get('master_percentage')
        bachelor_degree=request.POST.get('bachelor_degree')
        bachelor_specification=request.POST.get('bachelor_specification')
        bachelor_percentage=request.POST.get('bachelor_percentage')
        course_enquired=request.POST.get('course_enquired')
        source=request.POST.get('source')
        assigned_to=request.POST.get('assigned_to')
        #time_lead_created=request.POST.get('time_lead_created')
        technologies_known=request.POST.get('technologies_known')
        level_of_lead=request.POST.get('level_of_lead')
        print("customer=source is= ",source)
        create_record=CustomerLeads.objects.create(

        
        created_by=str(request.user),
        lead_name=lead_name,
        contact_number=contact_number,
        door_number=door_number,
        street_name=street_name,
        area=area,
        city=city,
        state=state,
        pincode=pincode,
        enquiry_location=enquiry_location,
        dob=dob,
        email=email,
        gender=gender,
        # photo=request.POST.get('photo')
        master_degree=master_degree,
        master_specification=master_specification,
        master_percentage=master_percentage,
        bachelor_degree=bachelor_degree,
        bachelor_specification=bachelor_specification,
        bachelor_percentage=bachelor_percentage,
        course_enquired=course_enquired,
        source=source,
        assigned_to=assigned_to,
        technologies_known=technologies_known,
        level_of_lead=level_of_lead,
        stage='newlead'
        )

        create_record.save()
        messages.success(request, 'Customer Record inserted successfully!')
        return redirect('manager-page-customerleads')
    else:
        return HttpResponse('record not posted')

def client_info(request,id):
    detail=ClientLeads.objects.get(lead_id=id)
    
    return render (request,'baseClientInfoPage.html',{'detail':detail})


def manager_activities(request):
    if request.method=='POST':

        desig=UserProfile.objects.get(user=request.user).designation


        call_count=EmployeeActivities.objects.create()
    
        manager_activities_data={
        'designation':desig,
        'user':request.user,
            }
    return render(request,'manager_templates/activities.html',)

def manager_activity_count(request):
    if request.method=='POST':
        employee_id = request.POST.get('employee_id')
        employee_name = request.POST.get('employee_name')
            
        call_count = request.POST.get('lead_count')
        return redirect('manager-activities')
    else:
        messages.warning(request, 'This is a warning message count didnt update.')
        return redirect('manager-activities')



from django.contrib import messages
def followup_record(request,stage):
    if request.method=='POST':
    
         remarks=request.POST.get('remarks')
         followup_date=request.POST.get('followup_date')
         walkin_date=request.POST.get('walkin_date')
         walkin_time=request.POST.get('walkin_time')
         need_supervisor_attention=request.POST.get('need_supervisor_attention')
         lead_id=request.POST.get('lead_id')
         user_id=request.POST.get('user_id')

         if not followup_date:
             followup_date= None
        
         if not walkin_date:
            walkin_date = None

         if not walkin_time:
             walkin_time = None

         if not need_supervisor_attention:
             need_supervisor_attention= None

         followup_object=FollowUp.objects.create(followup_date=followup_date,
                              remarks=remarks,
                               walkin_date=walkin_date,
                                walkin_time=walkin_time,
                                need_supervisor_attention=need_supervisor_attention,
                                lead_id=lead_id,
                                  )
         followup_object.save()
         content_type=ContentType.objects.get_for_model(FollowUp)
         activity_object=Activities.objects.create(lead_id=lead_id,employee_user_name=user_id,content_type=content_type,activity_id=followup_object.id)
         #activity_id=followup_object.id   shows integrity error
         activity_object.save()
        #  get_lead=CustomerLeads.objects.get(lead_id=lead_id)
        #  get_lead.level_of_lead="Follow up"  
         if stage=='client':
            get_lead=ClientLeads.objects.get(lead_id=lead_id)
            get_lead.stage="followup" 
            get_lead.save() 
            messages.success(request, 'Client Record Followed Up successfully!')
            return redirect("manager-page-clientleads")
         elif(stage=='customer'):
             get_lead=CustomerLeads.objects.get(lead_id=lead_id)
             get_lead.stage="followup" 
             get_lead.save() 
             print("done customer followup")
             messages.success(request, 'Customer Record Followed Up successfully!')
             return redirect("manager-page-customerleads")
    

def prospects_record(request,stage):
   if request.method=='POST':
      lead_id=request.POST.get('lead_id')
      remarks=request.POST.get('remarks')
      tentative_batch_start_date=request.POST.get('tentative_batch_start_time')
      preffered_batch_start_time=request.POST.get('preffered_batch_start_time')
      preffered_batch_end_time=request.POST.get('preffered_batch_end_time')
      preffered_batch_type=request.POST.get('preffered_batch_type')
      preffered_class_type=request.POST.get('preffered_class_type')
      preffered_course=request.POST.get('preffered_course')
      expected_registration_date=request.POST.get('expected_registration_date')
      billing_amount=request.POST.get('billing_amount')
      expected_collection=request.POST.get('expected_collection')
      mode_of_payment=request.POST.get('mode_of_payment')
      visiting_time=request.POST.get('visiting_time')
      user_id=request.POST.get('user_id')

      if not  billing_amount:
          billing_amount=None

      if not expected_collection:
          expected_collection=None
        
      if not mode_of_payment:
          mode_of_payment=None
          
      prospect_object=Prospects.objects.create(lead_id=lead_id,remarks=remarks,
                                               preffered_course=preffered_course,
                                               preffered_batch_start_time=preffered_batch_start_time,
                                               preffered_batch_end_time=preffered_batch_end_time,
                                               preffered_batch_type=preffered_batch_type,
                                               preffered_class_type=preffered_class_type,
                                               expected_registration_date=expected_registration_date,
                                               visiting_time=visiting_time,
                                               tentative_batch_start_date=tentative_batch_start_date,
                                               billing_amount=billing_amount,
                                               expected_collection=expected_collection,
                                               mode_of_payment=mode_of_payment
                                               )
      prospect_object.save()
      content_type=ContentType.objects.get_for_model(Prospects)
      activity_object=Activities.objects.create(lead_id=lead_id,employee_user_name=user_id,content_type=content_type,activity_id=prospect_object.id)
      #activity_id=prospect_object.id   shows integrity error  because id already exists
      activity_object.save()
      if stage=='client':
        get_lead=ClientLeads.objects.get(lead_id=lead_id)
        get_lead.stage="prospect"   
        get_lead.save() 
        messages.success(request, 'Client Record Successfully Moved To Prospect!')
        return redirect("manager-page-clientleads")
      elif(stage=='customer'):
          get_lead=CustomerLeads.objects.get(lead_id=lead_id)
          get_lead.stage="prospect"   
          get_lead.save() 
          messages.success(request, 'Customer Record Successfully Moved To Prospect!')
          return redirect("manager-page-customerleads")
   

def registered_record(request):
    if request.method=='POST':
       lead_id=request.POST.get('lead_id')
       course=request.POST.get('course')
       class_type=request.POST.get('class_type')
       batch_type=request.POST.get('batch_type')
       course_duration=request.POST.get('course_duration')
       tentative_start_date=request.POST.get('tentative_start_date')
       tentative_end_date=request.POST.get('tentative_end_date')
       start_time=request.POST.get('start_time')
       end_time=request.POST.get('end_time')
       trainer_name=request.POST.get('trainer_name')
       total_bill_amount=request.POST.get('total_bill_amount')
       advance_paid=request.POST.get('advance_paid')
       mode_of_payment=request.POST.get('mode_of_payment')
       alternative_address=request.POST.get('alternative_address')
       alternative_contact_number=request.POST.get('alternative_contact_number')
       alternative_email=request.POST.get('alternative_email')
       #invoice
       user_id=request.POST.get('user_id')
       registered_object=Registered.objects.create(lead_id=lead_id,
                                                   course=course,
                                                   class_type=class_type,
                                                   batch_type=batch_type,
                                                   course_duration=course_duration,
                                                   tentative_start_date=tentative_start_date,
                                                   tentative_end_date=tentative_end_date,
                                                   start_time=start_time,
                                                   end_time=end_time,
                                                   trainer_name=trainer_name,
                                                   total_bill_amount=total_bill_amount,
                                                   advance_paid=advance_paid,
                                                   mode_of_payment=mode_of_payment,
                                                   alternative_address=alternative_address,
                                                   alternative_contact_number=alternative_contact_number,
                                                   alternative_email=alternative_email
                                                    )
       registered_object.save()
       content_type=ContentType.objects.get_for_model(Registered)
       activity_object=Activities.objects.create(lead_id=lead_id,employee_user_name=user_id,content_type=content_type,activity_id=registered_object.id)
       #activity_id=registered_object.id   integrity error  becoz id might be same
       activity_object.save()
       get_lead=ClientLeads.objects.get(lead_id=lead_id)
       get_lead.stage="registered"  
       messages.success(request, 'Record successfully Moved To Registered!')
       return HttpResponse("Successfully Registered") 
    

def closed_record(request,stage):
  if request.method=='POST':
     lead_id=request.POST.get('lead_id')
     remarks=request.POST.get('remarks')
     reason_for_closure=request.POST.get('reason_for_closure')
     opportunities_in_future=request.POST.get('opportunities_in_future')
     user_id=request.POST.get('user_id')
     
     if (stage=='client'):
        get_lead=ClientLeads.objects.get(lead_id=lead_id)
        stage_of_closure=get_lead.stage
        closed_object=Closed.objects.create(lead_id=lead_id,
                                            remarks=remarks,
                                            reason_for_closure=reason_for_closure,
                                            stage_of_closure=stage_of_closure,
                                            opportunities_in_future=opportunities_in_future,
                                            )
        closed_object.save()
        get_lead.stage="closed" 
        get_lead.save()
        content_type=ContentType.objects.get_for_model(Closed)
        activity_object=Activities.objects.create(lead_id=lead_id,employee_user_name=user_id,content_type=content_type,activity_id=closed_object.id)
        activity_object.save()
        messages.success(request, 'Client Record successfully closed!')
        return redirect("manager-page-clientleads")
     elif(stage=='customer'):
         get_lead=CustomerLeads.objects.get(lead_id=lead_id)
         stage_of_closure=get_lead.stage
         closed_object=Closed.objects.create(lead_id=lead_id,
                                            remarks=remarks,
                                            reason_for_closure=reason_for_closure,
                                            stage_of_closure=stage_of_closure,
                                            opportunities_in_future=opportunities_in_future,
                                            )
         closed_object.save()
         get_lead.stage="closed" 
         get_lead.save()
         content_type=ContentType.objects.get_for_model(Closed)
         activity_object=Activities.objects.create(lead_id=lead_id,employee_user_name=user_id,content_type=content_type,activity_id=closed_object.id)
         activity_object.save()

         messages.success(request, 'Customer Record successfully closed!')
         return redirect("manager-page-customerleads")

     
def assign_to(request,lead,id,checks):
    print(type(id),type(checks))
    print(checks)
    checks_list = [int(check) for check in checks.split(',')]
    auth_user=User.objects.get(id=id)
    print(auth_user.username)
    if lead=='client':
        for i in checks_list:
            client=ClientLeads.objects.get(pk=i)
            client.assigned_to=auth_user.username
            client.save()
        return redirect('manager-page-clientleads')
    if lead=='customer':
        for i in checks_list:
            customer=CustomerLeads.objects.get(pk=i)
            customer.assigned_to=auth_user.username
            customer.save()
        return redirect('manager-page-clientleads')  
  