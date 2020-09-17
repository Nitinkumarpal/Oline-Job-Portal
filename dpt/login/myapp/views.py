from django.shortcuts import render,get_object_or_404
from django.http import *
from .forms import *
from myapp.templates import *
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django .contrib import messages
from django.http import HttpResponse
from django.views.generic import TemplateView

def home(request):
   return render(request,'index.html')

# Create your views here.
def google(request):
    return render(request,'google.html')#templataes se uthayega rander--uthana data 
# Create your views here.
def hcl(request):
    return render(request,'hcl.html')
# def log(request):
#     return render(request,'log.html')

def reg(request):
    return render(request,'reg.html')
def index2(request):
    return render(request,'index2.html')#templataes se uthayega rander--uthana data 
#templataes se uthayega rander--uthana data 


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            return redirect("/login")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

           # return render(request = request,
                        #  template_name = "register.html",
                      #    context={"form":form})
    else:
        form = NewUserForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})


def login_request(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/index2')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/login')
  


    

def list_view(request):
    return render(request,
    template_name='list_view.html',
    context={"company":company_login.objects.all})#t

    
def login_form(request):
   return render(request,'form.html')
from django.shortcuts import render
















def hom(request):
    return render(request, 'hom.html')
 
def new_page(request):
    data = request.POST.get('fulltextarea')
    return render(request, 'newpage.html', {'data':data})










# def stu(request):
#     next = request.GET.get('next', '/admin')
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)
   

#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             data = Students.objects.all()
#             stu = {
#                 "student_number": data
#                 }
#             return render(request,"stu.html", stu)
#         else:
#             HttpResponse("Inactive User.")
#     else:
#         print("User Not Found!")
#         return HttpResponseRedirect(settings.LOGIN_URL)

#     return render(request, 'login/home', {'redirect_to':next})



def company_data(request):
    return render(request,
    template_name='company.html',
    context={"company":company_login.objects.all})

def company_detail(request,id,Company_name):
    cmpy=get_object_or_404(company_login,id=id,Company_name=Company_name)
    context = {
        "cmpy":cmpy,
        
    }
        
    return render(request, 'detail.html',context)


def jobseaker_data(request):
    return render(request,
    template_name='jobseaker.html',
    context={"jobseaker":jobseaker_login.objects.all})#


def jobseeker_detail(request,id,name):
    jbs=get_object_or_404(jobseaker_login,id=id,name=name)
    context = {
        "jbs":jbs,
        
    }
        
    return render(request, 'detail1.html',context)


from django.shortcuts import render



def createpost1(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('dob'):
                jlogin=jobseaker_login()
                jlogin.title= request.POST.get('name')
                jlogin.content= request.POST.get('dob')
                jlogin.qualification= request.POST.get('qualification')
                jlogin.Experince= request.POST.get('Experince')
                jlogin.contact_no= request.POST.get('contact_no')

                jlogin.save()
                
                return render(request, 'jobseaker2.html')  

        else:    
            return HttpResponseRedirect("/newpage.html")

                #return render(request,'jobseaker2.html')




def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'newpage.html')  

        else: 
            message = 'You submitted an empty form.'
            return HttpResponse(message)
                #return render(request,'jobseaker2.html')

def add_jobseaker(request):#abhishek wala
    if request.method == 'POST':  # data sent by user
        form = jobdata(request.POST)
        if form.is_valid():
            form.save()  # this will save jobseaker info to database
            return HttpResponseRedirect("add_login")
    else:  # display empty form
        form = jobdata()

    return render(request, 'js.html', {'js_form': form})

def add_company(request):#abhishek wala
    if request.method == 'POST':  # data sent by user
        form = companydata(request.POST)
        if form.is_valid():
            form.save()  # this will save jobseaker info to database
            return HttpResponseRedirect("add_login")
    else:  # display empty form
        form = companydata()

    return render(request, 'cd.html', {'cd_form': form})


# def add_login(request):
#     if request.method == 'POST':
#        form = logidata(request.POST)
#        if form.is_valid(): 
#            if request.POST.get('name') and request.POST.get('dob'):
#                 form=logi()
#                 form.name= request.POST.get('name')
#                 form.dob= request.POST.get('dob')
#                 form.save()  
#                 return HttpResponseRedirect("/newpage")

#                # return render(request, 'newpage.html')  
#   # this will save jobseaker info to database
#             #return HttpResponseRedirect("index2")
#     else:  # display empty form
#         form = logidata()

#     return render(request, 'logi.html', {'logi_form': form})
def add_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        dob = request.POST['dob']

        user = authenticate(username=username, dob=dob)
   

        if user is not None:
            if user.is_active:
                login(request, user)
                data = logi.objects.all()

                return HttpResponseRedirect("login")
            else:
                HttpResponse("Inactive User.")
        else:
            print("User Not Found!")
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, 'login.html', {'redirect_to':next})



from django.shortcuts import render
from myapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def indexx(request):
    return render(request,'indexx.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
    
def register11(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def register1(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return redirect('/user_login')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)   
                return redirect('/index2')
               # return HttpResponse('welcome')

               # return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'loginn.html', {})