from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    UID = models.CharField(max_length=16)
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
        ('O', '其他'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    birthday = models.DateField()
    more = models.TextField()
class Site(models.Model):
    site_name = models.CharField(max_length=32,default=None)
    site_address = models.CharField(max_length=128, default=None)
    site_open_time = models.DateTimeField(default=None)
    site_close_time = models.DateTimeField(default=None)
    location = models.CharField(max_length=128, default=None)
    more = models.TextField(default=None)
    score = models.DecimalField(max_digits=2, decimal_places=1,default=None)

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=32,default=None)
    restaurant_address = models.CharField(max_length=128, default=None)
    restaurant_open_time = models.DateTimeField(default=None)
    restaurant_close_time = models.DateTimeField(default=None)
    location = models.CharField(max_length=128,default=None)
    #简历
    more = models.TextField(default=None)
    #评分
    score = models.DecimalField(max_digits=2, decimal_places=1,default=None)
class City(models.Model):
    #省级
    Province = models.CharField(max_length=8,default=None)
    #地级
    PLAD = models.CharField(max_length=32,default=None)
    #县级
    CLAD = models.CharField(max_length=32,default=None)
    #乡级
    TLAD = models.CharField(max_length=32,default=None)
