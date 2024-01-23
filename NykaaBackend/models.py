from django.db import models


# Create your models here.
class CategoryDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Category Images", null=True, blank=True)


class ProductDB(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Specification = models.CharField(max_length=500, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Image1 = models.ImageField(upload_to="Product Images", null=True, blank=True)
    Image2 = models.ImageField(upload_to="Product Images", null=True, blank=True)
    Image3 = models.ImageField(upload_to="Product Images", null=True, blank=True)
