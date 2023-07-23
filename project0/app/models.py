from django.db import models
# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=50) 
    description= models.TextField(null=True, max_length=50)
    is_active =  models.IntegerField(null=True)
    created_on  = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    def __str__(self):
       return self.category_id