from __future__ import unicode_literals
import bcrypt
from django.db import models

class validate(models.Manager):
    def login(self, postData):
           errors = []
           response = {}
           admin = Admin.objects.filter(username = postData['username'])
           if not admin:
               errors.append('**Username not found. Username is case sensitive. **')
               response['status'] = False
               response['errors'] = errors
               return response
           hashed = admin[0].password
           check_password = bcrypt.hashpw(postData['password'].encode('utf-8'), hashed.encode('utf-8'))
           if not hashed == check_password:
               errors.append('**Incorrect password**')
               response['status'] = False
               response['errors'] = errors
           else:
               response['status'] = True
           return response



# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length = 255)
    total_score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Camper(models.Model):
    username = models.CharField(max_length = 255)
    team = models.ForeignKey(Team)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Admin(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=validate()

class Mission(models.Model):
    name= models.CharField(max_length = 255)
    description= models.TextField()
    rating = models.IntegerField()
    admin = models.ForeignKey(Admin)
    teams = models.ManyToManyField(Team, related_name = "current_missions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
