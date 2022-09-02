
from django.db import models
from datetime import  datetime

# Create your models here.


                              
#Table with FK (ForeignKey)
class Asset_location(models.Model):
   asset_location =models.CharField(max_length=50)
   def __str__(self) :
        return self.asset_location

ASSET_CHOICES = (
         ('Laptop','Laptop'),
        ('Desktop','Desktop'),
        ('UPS','UPS'),
        ('Printer','Printer'),
        ('Scanner','Scanner'),
)
 

class Inventory(models.Model):
    
    Asset_Type = models.CharField(max_length=10,null=True,choices=ASSET_CHOICES)
    Asset_Name = models.CharField(max_length=15)
    asset_location = models.ForeignKey(Asset_location,on_delete=models.CASCADE)
    Asset_Model = models.CharField(max_length=15)
    Serial_No =  models.CharField(max_length=15)
    Mac_address = models.CharField(max_length=15)
    RAM_Size = models.CharField(max_length=10)
    HDD_Size = models.CharField(max_length=10)
    Power_capacity = models.CharField(max_length=10)
    time_created = models.DateTimeField(default=datetime.now)

   







    

    




