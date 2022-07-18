from django.db import models
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


       

class Product(models.Model):

    Asset_Type = models.CharField( max_length=15)
    Asset_Name = models.CharField(max_length=15)
    Serial_No =  models.CharField(max_length=15)
    Mac_address = models.CharField(max_length=15)
    Memmory_Size = models.IntegerField()
    HHD_Size = models.IntegerField()
    Asset_Model= models.CharField(max_length=15)
    Power_capacity = models.IntegerField(default=0)
    time_created = models.DateTimeField(default=datetime.now)

    def __str__(self) :
        return self.Asset_Name                    





    

    




