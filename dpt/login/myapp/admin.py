from django.contrib import admin
from.models import *

from myapp.models import UserProfileInfo, User


class company(admin.ModelAdmin):
    fieldsets =[
    ("Company information",{"fields":["Company_name","years_of_stablish","location","contact_no","email"]}),
   ("upcomming opportunity",{"fields":["upcomming_jobs"]}),
   ("about company",{"fields":["upload_logo","description"]}),
   ]

class jobseeker(admin.ModelAdmin):
    fieldsets =[
    ("Jobseeker information",{"fields":["name","image","dob","gender","qualification","resume","email"]}),
   ("Experience",{"fields":["Experince"]}),
   ("Contact on",{"fields":["contact_no","about"]}),
   ]

admin.site.register(UserProfileInfo)

admin.site.register(jobseaker_login ,jobseeker)
admin.site.register(company_login, company)
