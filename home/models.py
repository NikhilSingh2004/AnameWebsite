from django.db import models

class Candels(models.Model):
    product_price = models.IntegerField(default=0)
    product_image = models.FileField(upload_to="media/", max_length=100 , null=True, default= "")
    product_name = models.CharField(default="",max_length=50)
    product_title = models.CharField(default= "", max_length=100,null=True)
    product_dis =models.TextField(default="")

    def __str__(self):
        return self.product_name

class ResignArt(models.Model):
    product_price = models.IntegerField(default=0)
    product_image = models.FileField(upload_to="media/", max_length=100 , default= "")
    product_name = models.CharField(default="",max_length=50)
    product_title = models.CharField(default= "", max_length=50,null=True)
    product_dis =models.TextField(default="")

    def __str__(self):
        return self.product_name
    

class Order(models.Model):
    product_no = models.IntegerField(null=False,default=0)
    first_name = models.CharField(max_length=50,null=False,default="")
    last_name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=100,null=False,default="")
    phone_number = models.BigIntegerField(null=False,default="")
    address_1 = models.CharField(max_length=200,null=False,default="")
    address_2 = models.CharField(default="",max_length=200,null=True)
    country = models.CharField(max_length=50,null=False,default='India')
    state = models.CharField(max_length=50,null=False)
    district = models.CharField(max_length=50,null=False)
    town = models.CharField(max_length=50,null=False)
    quantity = models.IntegerField(null=False)
    zip_code = models.IntegerField(null=False)
    payment_done = models.BooleanField(default=False)

    def __str__(self):
        return self.product_no

