from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class jobseaker_login(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateTimeField()
    qualification = models.CharField(max_length=30)
    Experince = models.TextField(blank=True)
    contact_no = models.CharField(max_length=12)
    resume = models.ImageField(upload_to='user/%Y/%m/%d',blank=True)
    image = models.ImageField(upload_to='company/%Y/%m/%d',blank=True)
    about= models.TextField(blank=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=50)






   # male = models.BooleanField(blank=True)
    #female = models.BooleanField( blank=False)
   # class Meta:
        #ordering =('name', )
       # verbose_name= 'login'
    
    def __str__(self):
        return self.name
    def get_absolute_url1(self):
        return reverse('myapp:jobseeker_detail',args=[self.id, self.name])  

class company_login(models.Model):
    Company_name = models.CharField(max_length=50)
    years_of_stablish = models.DateTimeField()
    location= models.CharField(max_length=30)
    contact_no = models.CharField(max_length=12)
    upcomming_jobs = models.TextField(blank=True)
    description = models.TextField(blank=True)
    upload_logo = models.ImageField(upload_to='company/%Y/%m/%d',blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.Company_name

    def get_absolute_url(self):
        return reverse('myapp:company_detail',args=[self.id, self.Company_name])  

# class Students(models.Model):
#     student_number = models.IntegerField(primary_key=True)
#     f_name = models.CharField(max_length=20, blank=True, null=True)
#     l_name = models.CharField(max_length=20, blank=True, null=True)
#     dob = models.DateField(blank=True, null=True)
#     address = models.CharField(max_length=144, blank=True, null=True)
#     county = models.CharField(max_length=20, blank=True, null=True)
#     phone_number = models.CharField(max_length=45, blank=True, null=True)
#     email = models.CharField(max_length=45, blank=True, null=True)
#     gpa = models.IntegerField(blank=True, null=True)
#     # course_code = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course_code', blank=True, null=True)
#     # college = models.ForeignKey(Colleges, models.DO_NOTHING, blank=True, null=True)
#     passwords = models.CharField(max_length=60, blank=True, null=True)

#     class Meta:
#         db_table = 'students'
    
class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()
    
class logi(models.Model):
    username= models.CharField(max_length=300, unique=True)
    dob = models.DateField(blank=True, null=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username