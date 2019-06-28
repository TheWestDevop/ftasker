# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.db.models import Q
import hashlib

from django.utils import timezone 

# Create your models here.
class UserType(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=20)


class User(models.Model):
      id               = models.AutoField(primary_key=True)
      username         = models.CharField(max_length=10)
      password         = models.CharField(max_length=200)
      secret           = models.CharField(max_length=200)
      usertype         = models.IntegerField(default=1)
      isemailverified  = models.IntegerField(default=0)
      isphoneverified  = models.IntegerField(default=0)
      status           = models.IntegerField(default=0)
      createdate       = models.DateTimeField(default = timezone.now)


class Profile(models.Model):
      id         = models.AutoField(primary_key=True)
      uid        = models.IntegerField()
      firstname  = models.CharField(max_length=200,default="")
      lastname   = models.CharField(max_length=200,default="")
      email      = models.EmailField(max_length=100)
      telephone  = models.CharField(max_length=200)
      address    = models.CharField(max_length=200,default="")
      address2   = models.CharField(max_length=200,default="")
      city       = models.IntegerField(default=0)
      state      = models.IntegerField(default=0)
      country    = models.IntegerField(default=0)
      createdate = models.DateTimeField(default = timezone.now)

class Category(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=500)

class Subcategory(models.Model):
      id   = models.AutoField(primary_key=True)
      catid  = models.IntegerField()
      name = models.CharField(max_length=500)


class Country(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=500)


class  State(models.Model):
       id   = models.AutoField(primary_key=True)
       name = models.CharField(max_length=500)
       cid  = models.IntegerField()


class  City(models.Model):
       id   = models.AutoField(primary_key=True)
       name = models.CharField(max_length=500)
       sid  = models.IntegerField()      


class JobType(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=200)

class JobCategory(models.Model):
      id   = models.AutoField(primary_key=True)
      name = models.CharField(max_length=200)
      image = models.ImageField(upload_to='image/', blank=False)


class Job(models.Model):
       id            = models.AutoField(primary_key=True)
       uid           = models.IntegerField()
       jbtype        = models.IntegerField()
       jbcat         = models.IntegerField()
       title         = models.CharField(max_length=200)
       description   = models.CharField(max_length=500)
       budgetmin     = models.BigIntegerField() 
       budgetmax     = models.BigIntegerField()
       isawarded     = models.IntegerField()
       location      = models.CharField(max_length=500)
       duration      = models.IntegerField(default=1) 
       startdate     = models.DateTimeField(default = timezone.now)
       enddate       = models.DateTimeField(null=True,blank=True)
       awarddate     = models.DateTimeField(null=True,blank=True)


class JobApplication(models.Model):
      id      = models.AutoField(primary_key=True)
      jid     = models.IntegerField()
      uid     = models.IntegerField()
      awarded = models.IntegerField(default=0)


class Notification(models.Model):
      id            = models.AutoField(primary_key=True)
      senderid      = models.IntegerField(default=0)
      uid           = models.IntegerField()
      status        = models.IntegerField()
      title         = models.CharField(max_length=200)
      message       = models.TextField()
      isread        = models.IntegerField()
      createdate    = models.DateTimeField(default = timezone.now)

def createEmployer(username,password,secret,email,phone):
      passwordcat = str(password) + str(secret)
      passwordhash=hashlib.sha256(passwordcat.encode()).hexdigest()
      user= User.objects.create(username=username,password=passwordhash,secret=secret,usertype=2,isemailverified=0,isphoneverified=0,status=0)
      if user:
            print("Created user")
            profile = Profile.objects.create(uid=user.id,email=email,telephone=phone)
            if profile:
                  print("Created Profile")
                  return True
            else: 
                  User.objects.get(id=user.id).delete()
                  print("Unable to create profile")
                  return False


def createEmployee(username,password,secret,email,phone):
      passwordcat = str(password) + str(secret)
      passwordhash=hashlib.sha256(passwordcat.encode()).hexdigest()
      user= User.objects.create(username=username,password=passwordhash,secret=secret,usertype=1,isemailverified=0,isphoneverified=0,status=0)
      if user:
            print("Created user")
            profile = Profile.objects.create(uid=user.id,email=email,telephone=phone)
            if profile:
                  print("Created Profile")
                  return True
            else: 
                  User.objects.get(id=user.id).delete()
                  print("Unable to create profile")
                  return False

def doAuth(username,password):
      print("Do auth")
      userobj= User.objects.filter(username=username)
      if len(userobj)>0:
            user = userobj[0]
            secret = user.secret
            savedpassword = user.password
            passwordcat = str(password) + str(secret)
            print(secret)
            print(savedpassword)
            print(passwordcat)
            passwordhash=hashlib.sha256(passwordcat.encode()).hexdigest()
            print(passwordhash)
            if passwordhash == savedpassword:
                  return True
            else:
                  return False
      else: 
            return False

def userExists(username,email,phone):
      user = User.objects.filter(username=username)
      profile = Profile.objects.filter(Q(email=email) | Q(telephone=phone))
      if len(user)>1:
            return True
      if len(profile)>1:
            return True
      return False
      
def postJob(uid,location,jbtype,jbcat,title,description,budgetmin,budgetmax,duration,enddate):
      job = Job.objects.create(uid=uid,location=location,jbtype = jbtype,jbcat = jbcat,title = title,description = description,budgetmin = budgetmin,budgetmax = budgetmax,isawarded = 0,duration = duration,enddate = enddate)
      if job:
            return True
      else:
            return False

def applyForJob(jid,uid):
      jobapp = JobApplication.objects.create(jid=jid,uid=uid,awarded=0)
      if jobapp:
            return True
      else:
            return False

def requestForPayment():
      pass

def approvePayment():
      pass


