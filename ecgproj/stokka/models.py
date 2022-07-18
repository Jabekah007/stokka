from django.db import models
from django.contrib.auth import get_user_model
from datetime import  datetime
# Create your models here.
'''
 ASSET_CHOICES = (
         ('Laptop'),
        ('Desktop'),
        ('UPS'),
        ('Printer'),
        ('Scanner'),
)

'''                               


User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
   # Id_user =models.IntegerField()
    bio =models.TextField(blank=True)
    location = models.CharField(max_length=100,blank=True) 

    def __str__(self) :
        return self.user   



class Product(models.Model):

    Asset_Type = models.CharField( max_length=15)
    Asset_Name = models.CharField(max_length=15)
    Serial_No =  models.CharField(max_length=15)
    Mac_address = models.CharField(max_length=15)
    Memmory_Size = models.IntegerField(default=0)
    HHD_Size = models.IntegerField(default=0)
    Asset_Model= models.CharField(max_length=15)
    Asset_Location = models.CharField(max_length=15,blank=True)
    Power_capacity = models.IntegerField(default=0)
    time_created = models.DateTimeField(default=datetime.now)



    def __str__(self) :
        return self.Asset_Location







    

    




