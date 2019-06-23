
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TwitterCredentails(models.Model):
    user = models.ForeignKey(User,related_name="credentials",on_delete=models.CASCADE) #related_name paramater used for creating index on FK and reverse relationship
    access_token = models.CharField(max_length=100,null=True)
    access_secret = models.CharField(max_length=100,null=True)
    consumer_key = models.CharField(max_length=100,null=True)
    consumer_secret = models.CharField(max_length=100,null=True)