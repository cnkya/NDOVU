from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.



class Project(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="static/img")
    tasks = models.CharField(max_length=200)
    vendor = models.CharField(max_length=50)
    total_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    comments = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    complete_date = models.DateField(null=True, blank=True)
    
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[self.id]) #redirects users 


