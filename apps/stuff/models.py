from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['Firstname']) < 1:
            errors["Firstname"] = "Blog name should be more than 1 characters"
        if len(postData['Lastname']) < 1:
            errors["Lastname"] = "Blog desc should be more than 1 characters"
        if len(postData['Email']) < 1:
            errors["Email"] = "Blog name should be more than 1 characters"
        return errors

class User(models.Model):
      Firstname = models.CharField(max_length=255)
      Lastname = models.CharField(max_length=255)
      Email = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

      objects = BlogManager()
