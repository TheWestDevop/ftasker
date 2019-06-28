from django.shortcuts import render, redirect


from models.models import *
from django.db.models import Sum, Count, Case, When
from django.contrib.auth import logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import random
import string
import hashlib

# Create your views here.
def gen(request):
        User.objects.create(
              username="admin",
              password="cfa44e98e50114bac02bf1e465dcc687ba72467fc7bacb36898e59a1321166e6",
              secret="49'nv?42><",
              usertype=1,
              isemailverified =0,
              isphoneverified=0,
              status=0
              )
        return redirect(login)
      
    
def home(request):
    if request.session.has_key('token'):
        return redirect(listUser)
    else:
       return redirect(login)

#user 
def createUser(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            username = request.POST.get('username')
            plainpassword= request.POST.get('password')
            secret = secretGenerator()
            usertype = request.POST.get('usertype') 
            
            password = hashPassword(plainpassword+secret)
            
            User.objects.create(
              username=username,
              password=password,
              secret=secret,
              usertype=usertype,
              isemailverified =0,
              isphoneverified=0,
              status=0
              )
           
           
            return redirect(listUser)
        return redirect(listUser)
            
      else:
       return redirect(login)

def listUser(request):
    if request.session.has_key('token'):
       users = User.objects.all().order_by("-id")
       usertypes = UserType.objects.all().order_by("-id")
       return render(request,'manager/main.html',{'users': users,'usertypes': usertypes}) 
    else:
       return redirect(login)

def editUser(request,id):
    if request.session.has_key('token'):
        user = User.objects.get(id=id)
        if request.method == "POST":
            plainpassword= request.POST.get('password')
            password = hashPassword(plainpassword+user.secret)
            user.username = request.POST.get('username')
            user.password = password
            user.usertype = request.POST.get('usertype')
            user.isemailverified = int(request.POST.get('isemailverified'))
            user.isphoneverified= int(request.POST.get('isphoneverified'))
            user.status= int(request.POST.get('status'))
            user.save()
            return redirect(listUser)

        return render(request, 'manager/edit_user.html', {"user":user})
     
    else:     
       return redirect('login')

def deleteUser(request,id):
     if request.session.has_key('token'):
          user =User.objects.get(id=id)
          user.delete()
          return redirect(listUser)  
     else:
            return redirect(login)


#profile 
def listProfile(request):
    if request.session.has_key('token'):
       profiles = Profile.objects.all().order_by("-id")
       return render(request,'manager/profiles.html',{'profiles': profiles}) 
    else:
       return redirect(login)

  
  
  
  
  
  
  
  
  #Authentication and Login

def createProfile(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            telephone = request.POST.get('telephone')
            address = request.POST.get('address')
            address2= request.POST.get('address2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country  = request.POST.get('country')
            uid =  request.POST.get('uid')
            
            Profile.objects.create(
               uid=uid,
               firstname=firstname,
               lastname=lastname,
               email=email,
               telephone=telephone,
               address=address,
               address2=address2,
               city=city,
               state=state,
               country=country,
            )
            return redirect(listProfile)
        return redirect(listProfile)
            
      else:
       return redirect(login)
    
def editProfile(request,id):
    if request.session.has_key('token'):
        profile = Profile.objects.get(id=id)
        if request.method == "POST":
            profile.firstname = request.POST.get('firstname')
            profile.lastname = request.POST.get('lastname')
            profile.email = request.POST.get('email')
            profile.telephone = request.POST.get('telephone')
            profile.address = request.POST.get('address')
            profile.address2= request.POST.get('address2')
            profile.city = request.POST.get('city')
            profile.state = request.POST.get('state')
            profile.country  = request.POST.get('country')
            profile.save()
            return redirect(listProfile)

        return render(request, 'manager/edit_profile.html', {"profile":profile})
     
    else:     
       return redirect('login')

def deleteProfile(request,id):
     if request.session.has_key('token'):
          profile =Profile.objects.get(id=id)
          profile.delete()
          return redirect(listProfile)  
     else:
            return redirect(login) 

#usertype
def listUserType(request):
    if request.session.has_key('token'):
       usertypes = UserType.objects.all().order_by("-id")
       return render(request,'manager/usertypes.html',{'usertypes': usertypes}) 
    else:
       return redirect(login)

def createUserType(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            name = request.POST.get('name')
            
            
            UserType.objects.create(
               name=name
            )
            return redirect(listUserType)
        return redirect(listUserType)
            
      else:
       return redirect(login)
    
def editUserType(request,id):
    if request.session.has_key('token'):
        usertype = UserType.objects.get(id=id)
        if request.method == "POST":
            usertype.name = request.POST.get('name')
            usertype.save()
            return redirect(listUserType)

        return render(request, 'manager/edit_usertype.html', {"usertype":usertype})
     
    else:     
       return redirect('login')

def deleteUserType(request,id):
     if request.session.has_key('token'):
          usertype =UserType.objects.get(id=id)
          usertype.delete()
          return redirect(listUserType) 
     else:
            return redirect(login) 



#category
def listCategory(request):
    if request.session.has_key('token'):
       categories = Category.objects.all().order_by("-id")
       return render(request,'manager/categories.html',{'categories': categories}) 
    else:
       return redirect(login)

def createCategory(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            name = request.POST.get('name')
            
            
            Category.objects.create(
               name=name
            )
            return redirect(listCategory)
        return redirect(listCategory)
            
      else:
       return redirect(login)
    
def editCategory(request,id):
    if request.session.has_key('token'):
        category = Category.objects.get(id=id)
        if request.method == "POST":
            category.name = request.POST.get('name')
            category.save()
            return redirect(listCategory)

        return render(request, 'manager/edit_category.html', {"category":category})
     
    else:     
       return redirect('login')

def deleteCategory(request,id):
     if request.session.has_key('token'):
          category =Category.objects.get(id=id)
          category.delete()
          return redirect(listCategory) 
     else:
            return redirect(login) 

# subcategory
def listSubcategory(request):
    if request.session.has_key('token'):
       Subcategories = Subcategory.objects.all().order_by("-id")
       return render(request,'manager/subcategories.html',{'Subcategories': Subcategories}) 
    else:
       return redirect(login)

def createSubcategory(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            name = request.POST.get('name')
            catid =  request.POST.get('catid')
            
            Subcategory.objects.create(
               name=name,
               catid=catid
            )
            return redirect(listSubcategory)
        return redirect(listSubcategory)
            
      else:
       return redirect(login)
    
def editSubcategory(request,id):
    if request.session.has_key('token'):
        subcategory = Subcategory.objects.get(id=id)
        if request.method == "POST":
            subcategory.name = request.POST.get('name')
            subcategory.catid = request.POST.get('catid')
            subcategory.save()
            return redirect(listSubcategory)

        return render(request, 'manager/edit_subcategory.html', {"subcategory":subcategory})
     
    else:     
       return redirect('login')

def deleteSubcategory(request,id):
     if request.session.has_key('token'):
          subcategory = Subcategory.objects.get(id=id)
          subcategory.delete()
          return redirect(listSubcategory) 
     else:
            return redirect(login) 

#country
def listCountry(request):
    if request.session.has_key('token'):
       countries = Country.objects.all().order_by("-id")
       return render(request,'manager/countries.html',{'countries': countries}) 
    else:
       return redirect(login)

def createCountry(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            name = request.POST.get('name')
            Country.objects.create(
               name=name
            )
            return redirect(listCountry)
        return redirect(listCountry)
            
      else:
       return redirect(login)
    
def editCountry(request,id):
    if request.session.has_key('token'):
        country = Country.objects.get(id=id)
        if request.method == "POST":
            country.name = request.POST.get('name')
            country.save()
            return redirect(listCountry)

        return render(request, 'manager/edit_country.html', {"country":country})
     
    else:     
       return redirect('login')

def deleteCountry(request,id):
     if request.session.has_key('token'):
          country =Country.objects.get(id=id)
          country.delete()
          return redirect(listCountry) 
     else:
            return redirect(login) 

#state
def listState(request):
    if request.session.has_key('token'):
       states = State.objects.all().order_by("-id")
       return render(request,'manager/states.html',{'states': states}) 
    else:
       return redirect(login)

def createState(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            name = request.POST.get('name')
            cid =  request.POST.get('cid')
            
            State.objects.create(
               name=name,
               cid=cid
            )
            return redirect(listState)
        return redirect(listState)
            
      else:
       return redirect(login)
    
def editState(request,id):
    if request.session.has_key('token'):
        state = State.objects.get(id=id)
        if request.method == "POST":
            state.name = request.POST.get('name')
            state.cid = request.POST.get('cid')
            state.save()
            return redirect(listState)

        return render(request, 'manager/edit_state.html', {"state":state})
     
    else:     
       return redirect('login')

def deleteState(request,id):
     if request.session.has_key('token'):
          state = State.objects.get(id=id)
          state.delete()
          return redirect(listState) 
     else:
            return redirect(login) 


#city
def listCity(request):
    if request.session.has_key('token'):
       cities = City.objects.all().order_by("-id")
       return render(request,'manager/cities.html',{'cities': cities}) 
    else:
       return redirect(login)

def createCity(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            name = request.POST.get('name')
            sid =  request.POST.get('sid')
            
            City.objects.create(
               name=name,
               sid=sid
            )
            return redirect(listCity)
        return redirect(listCity)
            
      else:
       return redirect(login)
    
def editCity(request,id):
    if request.session.has_key('token'):
        city = City.objects.get(id=id)
        if request.method == "POST":
            city.name = request.POST.get('name')
            city.sid = request.POST.get('sid')
            city.save()
            return redirect(listCity)

        return render(request, 'manager/edit_city.html', {"city":city})
     
    else:     
       return redirect('login')

def deleteCity(request,id):
     if request.session.has_key('token'):
          city = City.objects.get(id=id)
          city.delete()
          return redirect(listCity) 
     else:
            return redirect(login) 

#jobtype
def listJobType(request):
    if request.session.has_key('token'):
       jobtypes = JobType.objects.all().order_by("-id")
       return render(request,'manager/jobtypes.html',{'jobtypes': jobtypes}) 
    else:
       return redirect(login)

def createJobType(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            name = request.POST.get('name')
            
            
            JobType.objects.create(
               name=name
            )
            return redirect(listJobType)
        return redirect(listJobType)
            
      else:
       return redirect(login)
    
def editJobType(request,id):
    if request.session.has_key('token'):
        jobtype = JobType.objects.get(id=id)
        if request.method == "POST":
            jobtype.name = request.POST.get('name')
            jobtype.save()
            return redirect(listJobType)

        return render(request, 'manager/edit_jobtype.html', {"jobtype":jobtype})
     
    else:     
       return redirect('login')

def deleteJobType(request,id):
     if request.session.has_key('token'):
          usertype =UserType.objects.get(id=id)
          usertype.delete()
          return redirect(listUserType) 
     else:
            return redirect(login) 


#jobcategory
def listJobCategory(request):
    if request.session.has_key('token'):
       jobcategories = JobCategory.objects.all().order_by("-id")
       return render(request,'manager/jobcategories.html',{'jobcategories': jobcategories}) 
    else:
       return redirect(login)

def createJobCategory(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            name = request.POST.get('name')
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name.strip(), image)
            
            
            JobCategory.objects.create(
               name=name,
               image=filename
            )
            return redirect(listJobCategory)
        return redirect(listJobCategory)
            
      else:
       return redirect(login)
    
def editJobCategory(request,id):
    if request.session.has_key('token'):
        jobcategory = JobCategory.objects.get(id=id)
        if request.method == "POST":
            jobcategory.name = request.POST.get('name')
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name.strip(), image)
            jobcategory.image = filename
            jobcategory.save()
            return redirect(listJobCategory)

        return render(request, 'manager/edit_jobcategory.html', {"jobcategory":jobcategory})
     
    else:     
       return redirect('login')

def deleteJobCategory(request,id):
     if request.session.has_key('token'):
          jobcategory = JobCategory.objects.get(id=id)
          jobcategory.delete()
          return redirect(listJobCategory) 
     else:
            return redirect(login) 

#job
def listJob(request):
    if request.session.has_key('token'):
       jobs = Job.objects.all().order_by("-id")
       return render(request,'manager/jobs.html',{'jobs':jobs}) 
    else:
       return redirect(login)

def createJob(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            uid = request.POST.get('uid')
            jbtype = request.POST.get('jbtype')
            jbcat = request.POST.get('jbcat')
            title = request.POST.get('title')
            description = request.POST.get('description')
            budgetmin = request.POST.get('budgetmin')
            budgetmax = request.POST.get('budgetmax')
            isawarded = request.POST.get('isawarded')
            location = request.POST.get('location')
            duration = request.POST.get('duration')
            startdate = request.POST.get('startdate')
            enddate = request.POST.get('enddate')
            awarddate = request.POST.get('awarddate')
            
            
            Job.objects.create(
               uid=uid,
               jbtype=jbtype,
               jbcat=jbcat,
               title=title,
               description=description,
               budgetmin=budgetmin,
               budgetmax=budgetmax,
               isawarded=isawarded,
               location=location,
               duration=duration,
               startdate=startdate,
               enddate=enddate,
               awarddate=awarddate
            )
            return redirect(listJob)
        return redirect(listJob)
            
      else:
       return redirect(login)
    
def editJob(request,id):
    if request.session.has_key('token'):
        job = Job.objects.get(id=id)
        if request.method == "POST":
            job.uid = request.POST.get('uid')
            job.jbtype = request.POST.get('jbtype')
            job.jbcat = request.POST.get('jbcat')
            job.title = request.POST.get('title')
            job.description = request.POST.get('description')
            job.budgetmin = request.POST.get('budgetmin')
            job.budgetmax = request.POST.get('budgetmax')
            job.isawarded = request.POST.get('isawarded')
            job.location = request.POST.get('location')
            job.duration = request.POST.get('duration')
            job.startdate = request.POST.get('startdate')
            job.enddate = request.POST.get('enddate')
            job.awarddate = request.POST.get('awarddate')
            job.save()
            return redirect(listJob)

        return render(request, 'manager/edit_job.html', {"job":job})
     
    else:     
       return redirect('login')

def deleteJob(request,id):
     if request.session.has_key('token'):
          job =Job.objects.get(id=id)
          job.delete()
          return redirect(listJob) 
     else:
            return redirect(login) 

#job application
def listJobApplication(request):
    if request.session.has_key('token'):
       jobApplications = JobApplication.objects.all().order_by("-id")
       return render(request,'manager/jobapplications.html',{'jobApplications': jobApplications}) 
    else:
       return redirect(login)

def createJobApplication(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            jid = request.POST.get('jid')
            uid = request.POST.get('uid')
            awarded = request.POST.get('awarded')
            
            JobApplication.objects.create(
               jid=jid,
               uid=uid,
               awarded=awarded        
              )
            return redirect(listJobApplication)
        return redirect(listJobApplication)
            
      else:
       return redirect(login)
    
def editJobApplication(request,id):
    if request.session.has_key('token'):
        jobApplication = JobApplication.objects.get(id=id)
        if request.method == "POST":
            jobApplication.jid = request.POST.get('jid')
            jobApplication.uid = request.POST.get('uid')
            jobApplication.awarded = request.POST.get('awarded')
            jobApplication.save()
            return redirect(listJobApplication)

        return render(request, 'manager/edit_jobapplication.html', {"jobApplication":jobApplication})
     
    else:     
       return redirect('login')

def deleteJobApplication(request,id):
     if request.session.has_key('token'):
          jobapplication =JobApplication.objects.get(id=id)
          jobapplication.delete()
          return redirect(listJobApplication) 
     else:
            return redirect(login) 

#Notification
        
def listNotification(request):
    if request.session.has_key('token'):
       notifications = Notification.objects.all().order_by("-id")
       return render(request,'manager/notifications.html',{'notifications': notifications}) 
    else:
       return redirect(login)

def createNotification(request):
      if request.session.has_key('token'):
        
        if request.method == "POST":
            senderid      = request.POST.get('senderid')
            uid           = request.POST.get('uid')
            status        = request.POST.get('status')
            title         = request.POST.get('title')
            message       = request.POST.get('message')
            isread        = request.POST.get('isread')
           
            
            Notification.objects.create(
               senderid=senderid,
               uid=uid,
               status=status,
               title=title,
               message=message,
               isread=isread
               
            )
            return redirect(listNotification)
        return redirect(listNotification)
            
      else:
       return redirect(login)
    
def editNotification(request,id):
    if request.session.has_key('token'):
        notification = Notification.objects.get(id=id)
        if request.method == "POST":
            notification.senderid      = request.POST.get('senderid')
            notification.uid           = request.POST.get('uid')
            notification.status        = request.POST.get('status')
            notification.title         = request.POST.get('title')
            notification.message       = request.POST.get('message')
            notification.isread        = request.POST.get('isread')
            notification.save()
            return redirect(listNotification)

        return render(request, 'manager/edit_notification.html', {"notification":notification})
     
    else:     
       return redirect('login')

def deleteNotification(request,id):
     if request.session.has_key('token'):
          notification =Notification.objects.get(id=id)
          notification.delete()
          return redirect(listNotification) 
     else:
            return redirect(login) 

  
#Authentication and Login

def Auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        plainpassword = request.POST.get('password')
        
        
    try:
            user = User.objects.get(username=username)

            secret = user.secret
            
            passwordConfirm = hashPassword(plainpassword+secret)
            
            if User.objects.filter(username=username).count() > 1:
               errormsg = "Mulitple User Found contact admin"
               messages.error(request,errormsg)
               return redirect('login')
              

            if passwordConfirm == user.password :
              request.session['token'] = user.secret
              
              return redirect('home')
              pass
        
            else:
               errormsg = "Invalid Username or Password"
               messages.error(request,errormsg)
               return redirect('login')
               pass
    except ObjectDoesNotExist:

        errormsg = "User Doesn't Exist"
        messages.error(request, errormsg)
        return redirect('login')
        pass

    else:
        return redirect('login')
	

def login(request):
    return render(request, 'manager/sign_in.html')


def logout(request):
    logout(request)
    return redirect(login)


def secretGenerator():
    letters = string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(10))


def hashPassword(word):
    password = hashlib.sha256(word.encode()).hexdigest()
    return password
