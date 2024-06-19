from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class FoodReceipe(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    ingredients = models.CharField(max_length=250)
    method = models.CharField(max_length=250)
    category = models.CharField(max_length=100,default="nocategory")
    category = models.ForeignKey(Category,on_delete = models.CASCADE)

    class Meta:
        verbose_name=('Categories')

    def __str__(self):
        return self.name
    

