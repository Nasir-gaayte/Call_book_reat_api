from django.db import models
from phone_field import PhoneField

class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class CityModel(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name    
    
class UserInfoModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True,null=True)
    job = models.CharField(max_length=50,blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    note = models.TextField(null=True, blank=True)
    city = models.ForeignKey(CityModel,on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
        
        
    def __str__(self):
        return self.name
        