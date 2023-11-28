from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#local_time = timezone.localtime(timezone.now())
#formatted_time = local_time.strftime("%d-%m-%Y %I:%M:%S %p")

def default_datetime():
    #return timezone.localtime(timezone.now()).strftime("%Y-%m-%D %I:%M:%S %p")
    return timezone.localtime(timezone.now())

DESIGNATION_CHOICES = (
        ('councellor', 'Councellor'),
        ('telecaller', 'Telecaller'),
        ('manager', 'Manager'),
        ('admin','Admin')
    )
supervisor_choices = [(user.username, user.username) for user in User.objects.all()]
assignedto_choices = [(user.username, user.username) for user in User.objects.all()] 



class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50,choices=DESIGNATION_CHOICES, blank=True)
    supervisor = models.CharField(max_length=50, blank=True,choices=supervisor_choices)  # Add supervisor field
    image = models.ImageField(upload_to='user_image/', blank=True, null=True)  # Add image field

    def __str__(self):
        return self.user.username




class Courses(models.Model):
    course_id=models.CharField(max_length=20)
    course_name=models.CharField(max_length=200)
    course_fees=models.BigIntegerField()
    course_duration=models.CharField(max_length=30)

stages_choices = [
        ('newlead', 'New Lead'),
        ('followup', 'Follow Up'),
        ('prospect', 'Prospect'),
        ('registered','Registered'),
        ('closed','Closed'),
    ]

class Activities(models.Model):
   activity_id=models.BigIntegerField(null=True,blank=True)
   lead_id=models.CharField(max_length=30)
   employee_user_name=models.CharField(max_length=30)
   date_and_time=models.DateTimeField(default=timezone.now)
   content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
   activity_related_to=GenericForeignKey('content_type', 'activity_id')

   def __str__(self):
      return str(self.date_and_time)

source_choices=[
   ('naukri','Naukri'),
   ('indeed','Indeed'),
   ('mail','Mail'),
   ('whatsapp','Whatsapp'),
   ('foundit','Foundit'),
   ('justdial','Justdial'),
   ('hirect','Hirect'),
]

class CustomerLeads(models.Model):
  lead_id=models.AutoField(primary_key=True)
  created_by=models.CharField(max_length=30)
  lead_name=models.CharField(max_length=30, null=False)
  contact_number=models.BigIntegerField(null=True, blank=True)
  door_number=models.CharField(max_length=10,null=True, blank=True)
  street_name=models.CharField(max_length=30,null=True, blank=True)
  area=models.CharField(max_length=30,null=True, blank=True)
  city=models.CharField(max_length=30,null=True, blank=True)
  state=models.CharField(max_length=30,null=True, blank=True)
  pincode=models.BigIntegerField(null=True, blank=True)
  enquiry_location=models.CharField(max_length=30,null=True, blank=True)
  dob=models.DateField(null=True, blank=True)
  email=models.EmailField(null=True, blank=True)
  gender=models.CharField(max_length=30,null=True, blank=True)
  master_degree=models.CharField(max_length=30,null=True, blank=True)
  master_specification=models.CharField(max_length=30,null=True, blank=True)
  master_percentage=models.FloatField(null=True, blank=True)
  bachelor_degree=models.CharField(max_length=30,null=True, blank=True)
  bachelor_specification=models.CharField(max_length=30,null=True, blank=True)
  bachelor_percentage=models.FloatField(null=True, blank=True)
  course_enquired=models.CharField(max_length=30,null=True, blank=True)
  source=models.CharField(max_length=30,choices=source_choices)
  assigned_to=models.CharField(max_length=30,null=True, blank=True,choices=assignedto_choices)
  time_lead_created=models.DateTimeField(default=default_datetime)
  #Extra Fields
  priority=models.SmallIntegerField(default=0)
  technologies_known=models.TextField(default="", blank=True)
  level_of_lead=models.CharField(max_length=30, default='', blank=True, null=True)
  stage=models.CharField(max_length=30,choices=stages_choices, null=True)



class ClientLeads(models.Model):
  lead_id=models.AutoField(primary_key=True)
  created_by=models.CharField(max_length=30)
  lead_name=models.CharField(max_length=30, null=False)
  contact_number=models.BigIntegerField(null=True, blank=True)
  door_number=models.CharField(max_length=10,null=True, blank=True)
  street_name=models.CharField(max_length=30,null=True, blank=True)
  area=models.CharField(max_length=30,null=True, blank=True)
  city=models.CharField(max_length=30,null=True, blank=True)
  state=models.CharField(max_length=30,null=True, blank=True)
  pincode=models.BigIntegerField(null=True, blank=True)
  enquiry_location=models.CharField(max_length=30,null=True, blank=True)
  dob=models.DateField(null=True, blank=True)
  email=models.EmailField(null=True, blank=True)
  gender=models.CharField(max_length=30,null=True, blank=True)
  master_degree=models.CharField(max_length=30,null=True, blank=True)
  master_specification=models.CharField(max_length=30,null=True, blank=True)
  master_percentage=models.FloatField(null=True, blank=True)
  bachelor_degree=models.CharField(max_length=30,null=True, blank=True)
  bachelor_specification=models.CharField(max_length=30,null=True, blank=True)
  bachelor_percentage=models.FloatField(null=True, blank=True)
  course_enquired=models.CharField(max_length=30,null=True, blank=True)
  source=models.CharField(max_length=30,choices=source_choices)
  assigned_to=models.CharField(max_length=30,null=True, blank=True,choices=assignedto_choices)
  time_lead_created=models.DateTimeField(default=default_datetime)
  #Extra Fields
  priority=models.SmallIntegerField(default=0)
  technologies_known=models.TextField(default="")
  level_of_lead=models.TextField(default='')
  company_name=models.TextField(max_length=100)
  company_door_number=models.CharField(max_length=10,null=True, blank=True)
  company_street_name=models.CharField(max_length=30,null=True, blank=True)
  company_area=models.CharField(max_length=30,null=True,blank=True)
  company_city=models.CharField(max_length=30,null=True,blank=True)
  company_state=models.CharField(max_length=30,null=True,blank=True)
  company_pincode=models.BigIntegerField(null=True,blank=True)
  company_gstnumber=models.BigIntegerField(null=True,blank=True)
  company_field=models.CharField(max_length=100,null=True,blank=True)
  comapny_website=models.URLField(null=True,blank=True)
  company_contact_number=models.BigIntegerField(null=True,blank=True)
  stage=models.CharField(max_length=30,choices=stages_choices,null=True,blank=True)




class FollowUp(models.Model):
   lead_id=models.TextField()
   followup_date=models.DateField(null=True,blank=True)
   remarks=models.TextField()
   walkin_date=models.DateField(null=True,blank=True)
   walkin_time=models.TimeField(null=True,blank=True)
   priority=models.SmallIntegerField(null=True, blank=True)
   need_supervisor_attention=models.BooleanField(default=False)
   #Relating to the Activities model
   activity = GenericRelation(Activities)

   def __str__(self):
      return self.remarks+"\n Next follow up date is,"+str(self.followup_date)



class_type_choices = [
        ('offline', 'Offline'),
        ('online', 'Online'),
        ('hybrid', 'Hybrid'),
    ]

batch_type_choices=[
   ('weekdays','Weekdays'),
   ('weekend','Weekend')
]

mode_of_payment_choices=[
   ('cash','Cash'),
   ('cheque','Cheque'),
   ('upi','UPI'),
   ('bank transfer','Bank Transfer')

]
   
class Prospects(models.Model):
   lead_id=models.CharField(max_length=20)
   remarks=models.TextField(null=True,blank=True)
   
   preffered_course=models.CharField(max_length=200,null=True,blank=True)
   preffered_batch_type=models.CharField(max_length=50,choices=batch_type_choices,null=True,blank=True)#weekend/weekdays
   preffered_batch_start_time=models.TimeField(max_length=100,null=True,blank=True)
   preffered_batch_end_time=models.TimeField(max_length=100,null=True,blank=True)
   preffered_class_type=models.CharField(max_length=30,choices=class_type_choices,null=True,blank=True) #online/offline/hybrid
   expected_registration_date=models.DateField(null=True,blank=True)
   visiting_time=models.TimeField(null=True,blank=True) 
   tentative_batch_start_date=models.DateField(null=True,blank=True)
   billing_amount=models.PositiveBigIntegerField(null=True,blank=True) #Total Fees
   expected_collection=models.PositiveBigIntegerField(null=True,blank=True)
   mode_of_payment=models.CharField(max_length=30,choices=mode_of_payment_choices,null=True,blank=True)
   #Relating to the Activities model
   activity = GenericRelation(Activities)



class Registered(models.Model):
   lead_id=models.CharField(max_length=30)
   registration_no=models.CharField(primary_key=True, max_length=10)
   registration_date=models.DateTimeField(default=default_datetime)
   course=models.CharField(max_length=30,null=True,blank=True)
   class_type=models.CharField(max_length=30,choices=class_type_choices) #online/offlin/hybrid
   batch_type=models.CharField(max_length=30,choices=batch_type_choices) #weekdays/weekend
   course_duration=models.TextField(max_length=30,null=True,blank=True)
   tentative_start_date=models.DateField(null=True,blank=True)
   tentative_end_date=models.DateField(null=True,blank=True)
   start_time=models.TimeField(null=True,blank=True)
   end_time=models.TimeField(null=True,blank=True)
   trainer_name=models.TextField(max_length=30,null=True,blank=True)
   #invoice details
   total_bill_amount=models.BigIntegerField(null=True,blank=True)
   invoice_number=models.CharField(max_length=10)
   advance_paid=models.BigIntegerField(null=True,blank=True)
   mode_of_payment=models.CharField(max_length=20,choices=mode_of_payment_choices)
   
   #extra details to capture at the time of registration
   alternative_address=models.TextField(null=True,blank=True)
   alternative_contact_number=models.BigIntegerField(null=True,blank=True)
   alternative_email=models.EmailField(null=True,blank=True)
   #Relating to the Activities model
   activity = GenericRelation(Activities)







   

class Closed(models.Model):
   lead_id=models.CharField(max_length=10)
   remarks=models.TextField(null=True,blank=True)
   reason_for_closure=models.TextField(null=True,blank=True)
   stage_of_closure=models.CharField(max_length=30,choices=stages_choices)
   opportunities_in_future=models.BooleanField(default=False)
   #Relating to the activities model 
   activity = GenericRelation(Activities)


class assign_to(models.Model):
   previously_assigned_to=models.CharField(max_length=30)
   currently_assigned_to=models.CharField(max_length=30)
    #Relating to the activities model 
   activity = GenericRelation(Activities)
print(default_datetime)

class EmployeeActivities(models.Model):
    employee_id = models.CharField(max_length=30)
    employee_name = models.CharField(max_length=30)
    date_time = models.DateTimeField(default=default_datetime)    
    call_count = models.PositiveIntegerField(default=0)
    messages_count = models.PositiveIntegerField(default=0)
    mail_count = models.PositiveIntegerField(default=0)
    whatsapp_count = models.PositiveIntegerField(default=0)
    counseling_count = models.PositiveIntegerField(default=0)
    college_visit_count = models.PositiveIntegerField(default=0)
    corporate_visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
       return self.employee_name
   

class EmployeeActivitiesTarget(models.Model):
    date_time = models.DateTimeField(default=default_datetime)    
    call_count_target = models.PositiveIntegerField(default=0)
    messages_count_target = models.PositiveIntegerField(default=0)
    mail_count_target = models.PositiveIntegerField(default=0)
    whatsapp_count_target = models.PositiveIntegerField(default=0)
    counseling_count_target = models.PositiveIntegerField(default=0)
    college_visit_count_target = models.PositiveIntegerField(default=0)
    corporate_visit_count_target = models.PositiveIntegerField(default=0)
print("hghgkh",default_datetime)
class empexcel(models.Model):
   first_name=models.CharField(max_length=30)
   last_name=models.CharField(max_length=30)
   age=models.CharField(max_length=30)
   monthly_salary=models.CharField(max_length=30)





   


