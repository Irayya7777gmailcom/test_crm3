from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as dj_login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from Administrator.models import CustomerLeads,UserProfile,ClientLeads,Closed,Prospects,Registered,FollowUp,Activities,EmployeeActivities,EmployeeActivitiesTarget
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.http import Http404

def home(request):
    if request.user.is_authenticated:
        leads = CustomerLeads.objects.filter(assigned_to=request.user)
        desig = UserProfile.objects.get(user=request.user).designation
        
        #CLIENTS
        client_leads= ClientLeads.objects.filter(stage='newlead',assigned_to=request.user)
        client_followup_leads= ClientLeads.objects.filter(stage='followup',assigned_to=request.user)
        client_closed_leads=ClientLeads.objects.filter(stage='closed',assigned_to=request.user)
        client_prospect_leads=ClientLeads.objects.filter(stage='prospect',assigned_to=request.user)
        client_registered_leads=ClientLeads.objects.filter(stage='registered',assigned_to=request.user)
        #CUSTOMERS
        customer_leads= CustomerLeads.objects.filter(stage='newlead',assigned_to=request.user)
        customer_followup_leads= CustomerLeads.objects.filter(stage='followup',assigned_to=request.user)
        customer_closed_leads=CustomerLeads.objects.filter(stage='closed',assigned_to=request.user)
        customer_prospect_leads=CustomerLeads.objects.filter(stage='prospect',assigned_to=request.user)
        customer_registered_leads=CustomerLeads.objects.filter(stage='registered',assigned_to=request.user)
        data_labels = ["New Leads", "FollowUp", "Prospect","Closed","Registered",]
        data_values = [customer_leads.count()+client_leads.count(),
                       client_followup_leads.count()+customer_followup_leads.count(),
                       client_prospect_leads.count()+customer_prospect_leads.count(),
                       client_closed_leads.count()+customer_closed_leads.count(),
                       client_registered_leads.count()+customer_registered_leads.count()
                       ]
        naukri_source= ClientLeads.objects.filter(source='naukri').count()+CustomerLeads.objects.filter(source='naukri').count()

        indeed_source= ClientLeads.objects.filter(source='indeed',assigned_to=request.user).count()+CustomerLeads.objects.filter(source='indeed',assigned_to=request.user).count()

        foundit_source= ClientLeads.objects.filter(source='foundit',assigned_to=request.user).count()+CustomerLeads.objects.filter(source='foundit',assigned_to=request.user).count()

        mail_source= ClientLeads.objects.filter(source='mail',assigned_to=request.user).count()+CustomerLeads.objects.filter(source='mail',assigned_to=request.user).count()

        whatsapp_source= ClientLeads.objects.filter(source='whatsapp',assigned_to=request.user).count()+CustomerLeads.objects.filter(source='whatsapp',assigned_to=request.user).count()

        justdial_source= ClientLeads.objects.filter(source='justdial',assigned_to=request.user).count()+CustomerLeads.objects.filter(source='justdial',assigned_to=request.user).count()

        counsellor_data={
            'leads': leads,
            'user': request.user,
            'viewleads':'New Leads',
            'designation':desig,
            
            'new_leads_count':customer_leads.count()+client_leads.count(),
            'followup_count':client_followup_leads.count()+customer_followup_leads.count(),

            
            'closed_count':client_closed_leads.count()+customer_closed_leads.count(),
                  
            'prospect_count':client_prospect_leads.count()+customer_prospect_leads.count(),
            
            'registered_count':client_registered_leads.count()+customer_registered_leads.count(),

                        
            'labels': data_labels,
            'values': data_values,
            'naukri_source':naukri_source, 
            'indeed_source': indeed_source,
            'foundit_source':foundit_source,
            'mail_source':  mail_source,
            'whatsapp_source': whatsapp_source,
            'justdial_source':justdial_source,
            'source_data': [naukri_source, indeed_source, mail_source, whatsapp_source, foundit_source, justdial_source],
            
            
            
        }
        return render(request, 'Counsellor_templates/councellor-dashboard.html',counsellor_data)
    else:
        return HttpResponse("User is not logged in. Please log in first.")

def councellor_page_clientleads(request):
    if request.user.is_authenticated:
        desig = UserProfile.objects.get(user=request.user).designation
        customer_leads = CustomerLeads.objects.all()
        client_leads= ClientLeads.objects.filter(stage='newlead',assigned_to=request.user)

        followup_leads= ClientLeads.objects.filter(stage='followup',assigned_to=request.user)
        closed_leads=ClientLeads.objects.filter(stage='closed',assigned_to=request.user)
        prospect_leads=ClientLeads.objects.filter(stage='prospect',assigned_to=request.user)
        registered_leads=ClientLeads.objects.filter(stage='registered',assigned_to=request.user)

        auth_users=User.objects.all()
        client_data={
            
            'leads': customer_leads, 
            'user': request.user,
            'user_id':request.user.id,
            'designation':desig,
            
            'client_leads':client_leads,
            
            'followup':followup_leads,
            'closed':closed_leads,
            'prospect':prospect_leads,
            
            
            'registered':registered_leads,
            
            'client':'client',
            'auth_users':auth_users,
            'array':'array'
        }
        return render(request, 'Counsellor_templates/councellor-page-clientleads.html',client_data)
    else:
        return HttpResponse("User is not logged in. Please log in first.")


def councellor_page_customerleads(request):
    if request.user.is_authenticated:
        
        desig = UserProfile.objects.get(user=request.user).designation
        customer_leads= CustomerLeads.objects.filter(stage='newlead',assigned_to=request.user)

        followup_leads= CustomerLeads.objects.filter(stage='followup',assigned_to=request.user)
        closed_leads=CustomerLeads.objects.filter(stage='closed',assigned_to=request.user)
        prospect_leads=CustomerLeads.objects.filter(stage='prospect',assigned_to=request.user)
        registered_leads=CustomerLeads.objects.filter(stage='registered',assigned_to=request.user)
        auth_users=User.objects.all()
        customer_data={
            
            'user': request.user,
            'user_id':request.user.id,
            'designation':desig,
            'customer_leads':customer_leads,
            
            'customer_followup':followup_leads,
            'customer_closed':closed_leads,
            'customer_prospect':prospect_leads,
            
            
            'customer_registered':registered_leads,
            
            'client':'client',
            'auth_users':auth_users,
            'array':'array',
            'customer':'customer'
        }
        return render(request, 'Counsellor_templates/councellor-page-customerleads.html',customer_data)
    else:
        return HttpResponse("User is not logged in. Please log in first.")
    

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
            return redirect("councellor-page-clientleads")
         elif(stage=='customer'):
             get_lead=CustomerLeads.objects.get(lead_id=lead_id)
             get_lead.stage="followup" 
             get_lead.save() 
             print("done customer followup")
             messages.success(request, 'Customer Record Followed Up successfully!')
             return redirect("councellor-page-customerleads")
         

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
        return redirect("councellor-page-clientleads")
      elif(stage=='customer'):
          get_lead=CustomerLeads.objects.get(lead_id=lead_id)
          get_lead.stage="prospect"   
          get_lead.save() 
          messages.success(request, 'Customer Record Successfully Moved To Prospect!')
          return redirect("councellor-page-customerleads")
   

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
        return redirect("councellor-page-clientleads")
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
         return redirect("councellor-page-customerleads")
  
# GETTING CURRENT DATE 
current_date = timezone.localtime(timezone.now()).date()
current_time= timezone.localtime(timezone.now()).time()
current_date_time=timezone.localtime(timezone.now())
# ----------------------
def councellor_activities(request):
        

        desig = UserProfile.objects.get(user=request.user).designation
        

        activity = EmployeeActivities.objects.get(employee_name=request.user, date_time__date=current_date)

        councellor_activity_data = {
            'designation': desig,
            'user': request.user,
            'call': 'call',
            'message': 'message',
            'mail': 'mail',
            'whatsapp': 'whatsapp',
            'councelling': 'councelling',
            'college_visit': 'college_visit',
            'corporate_visit': 'corporate_visit',
            'date': current_date_time,
            'call_count': activity.call_count,
            'message_count':activity.messages_count,
            'mail_count':activity.mail_count,
            'whatsapp_count':activity.whatsapp_count,
            'councelling_count':activity.counseling_count,
            'college_visit_count': activity.college_visit_count,
            'corporate_visit_count': activity.corporate_visit_count,
        }

        return render(request, 'Counsellor_templates/activities.html', councellor_activity_data)

    


# def councellor_activities(request):
#     try:
#         desig = UserProfile.objects.get(user=request.user).designation
#         if EmployeeActivities.objects.get(employee_name=request.user, date_time__date=current_date) is None:

#         activity = EmployeeActivities.objects.get(employee_name=request.user, date_time__date=current_date)

#         councellor_activity_data = {
#             'designation': desig,
#             'user': request.user,
#             'call': 'call',
#             'message': 'message',
#             'mail': 'mail',
#             'whatsapp': 'whatsapp',
#             'councelling': 'councelling',
#             'college_visit': 'college_visit',
#             'corporate_visit': 'corporate_visit',
#             'date': current_date,
#             'call_count': activity.call_count,
#         }

#         return render(request, 'Counsellor_templates/activities.html', councellor_activity_data)

#     except EmployeeActivities.DoesNotExist:
#         # Handle the case when EmployeeActivities does not exist
#         #raise Http404("EmployeeActivities does not exist for the given user and date.")
#         return redirect("councellor-activities")
    
#print("acticity call count= ",activity.call_count, activity.employee_name, current_time)
def councellor_activity_count(request,stage):
    if request.user.is_authenticated:
        check=EmployeeActivities.objects.get()
        
        if request.method=='POST':
            if stage=='call':
               update_count = EmployeeActivities.objects.get(employee_name=request.user, date_time__date=current_date)
        return redirect('councellor-activities')


                
           
            

                


