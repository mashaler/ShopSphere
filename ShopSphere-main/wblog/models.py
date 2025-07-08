from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.

class Allproducts(models.Model):
    prod_id = models.AutoField(primary_key=True, unique= True, null= False)
    prod_name = models.CharField(max_length= 50)
    prod_desc = models.CharField(max_length= 500)
    prod_category = models.CharField(max_length= 50)
    prod_sub_category = models.CharField(max_length= 50)
    prod_price = models.IntegerField()
    prod_orig_price = models.IntegerField()
    prod_view = models.IntegerField()
    prod_slug = AutoSlugField(populate_from= "prod_name", unique= True)
    prod_image = models.ImageField(upload_to= "shop")

    def __str__(self):
        return self.prod_name
    
class profile(models.Model):
    user_id = models.AutoField(primary_key=True, unique= True, null=False)
    user_detail = models.ForeignKey(User, on_delete=models.CASCADE)
    user_addres = models.CharField(max_length= 500)
    user_landnark = models.CharField(max_length=50)
    user_phone = models.IntegerField()
    user_pincode =models.CharField(max_length=50)

    def __str__(self):
        return self.user_detail.first_name
    
class Comment(models.Model):
    Comment_id = models.AutoField(primary_key=True, unique= True, null= False)
    prod_rating = models.IntegerField(null= True)
    comment_post = models.ForeignKey(Allproducts, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length= 500)
    comment_user = models.ForeignKey(User, on_delete= models.CASCADE)
    comment_date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.comment_content[0:15] + "..."
    

class Order(models.Model):
    status_choice = [
        ("PENDING", "Pending"),
        ("DISPATCHED", "Dispatched"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]
    order_id = models.AutoField(primary_key=True, unique=True, null=False)
    order_status = models.CharField(choices=status_choice, max_length=10, default="PENDING")
    orderUser = models.ForeignKey(User, on_delete=models.CASCADE)
    order_prod = models.ForeignKey(Allproducts, on_delete=models.CASCADE)
    prod_quantity = models.IntegerField(default=1, null=False)
    prod_color = models.CharField(max_length=50, null=False)
    prod_size = models.CharField(max_length=3, null=False)
    order_amount = models.IntegerField(default=1)
