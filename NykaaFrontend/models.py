from django.db import models


# Create your models here.
class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)


class RegisterDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    ConfirmPassword = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Reg Images", null=True, blank=True)


class CartDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Pro_Name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)


class CheckoutDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
