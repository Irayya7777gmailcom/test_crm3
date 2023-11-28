from django.contrib import admin
from .models import CustomerLeads,Courses,Prospects,ClientLeads,FollowUp,Registered,Closed,UserProfile,Activities,empexcel,EmployeeActivities,EmployeeActivitiesTarget
from import_export.admin import ImportExportModelAdmin

class NewLeadsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    admin.site.site_header = "Merida Adminstration"
    list_display = ('lead_id', 'lead_name', 'contact_number', 'email', 'assigned_to', 'time_lead_created')
admin.site.register(CustomerLeads, NewLeadsAdmin)
admin.site.register(ClientLeads , NewLeadsAdmin)
admin.site.register(FollowUp)
admin.site.register(Closed)
# admin.site.register(Courses , NewLeadsAdmin)
# admin.site.register(Registered , NewLeadsAdmin)
# admin.site.register(Prospects , NewLeadsAdmin)

admin.site.register(Courses)
admin.site.register(Registered)
admin.site.register(Prospects)
admin.site.register(Activities)
admin.site.register(UserProfile)
admin.site.register(EmployeeActivities)
admin.site.register(EmployeeActivitiesTarget)
admin.site.register(empexcel,ImportExportModelAdmin)

