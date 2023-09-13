from typing import Any
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATE_CHOICES = (

    ('Abia','Abia'),
    ('Adamawa','Adamawa'),
    ('Akwa Ibom', 'Akwa Ibom'),
    ('Anambra','Anambra'),
    ('Bauchi','Bauchi'),
    ('Bayelsa','Bayelsa'),
    ('Benue','Benue'),
    ('Borno','Borno'),
    ('Cross River','Cross River'),
    ('Delta','Delta'),
    ('Ebonyi','Ebonyi'),
    ('Edo','Edo'),
    ('Ekiti','Ekiti'),
    ('Enugu','Enugu'),
    ('Gombe','Gombe'),
    ('Imo','Imo'),
    ('Jigawa','Jigawa'),
    ('Kaduna','Kaduna'),
    ('Kano','Kano'),
    ('Katsina','Katsina'),
    ('Kebbi','Kebbi'),
    ('Kogi','Kogi'),
    ('Kwara','Kwara'),
    ('Lagos','Lagos'),
    ('Nasarawa','Nasarawa'),
    ('Niger','Niger'),
    ('Ogun','Ogun'),
    ('Ondo','Ondo'),
    ('Osun','Osun'),
    ('Oyo','Oyo'),
    ('Plateau','Plateau'),
    ('Rivers','Rivers'),
    ('Sokoto','Sokoto'),
    ('Taraba','Taraba'),
    ('Yobe','Yobe'),
    ('Zamfara','Zamfara'),
    ('FCT','FCT'),
)



CATEGORY_CHOICES = (
    ('WT','Watches'),
    ('SH','Shoes'),
    ('SN','Sneakers'),
    ('EP','Earpod'),
    ('BT','Belt'),
    ('HP','Headphone'),
    ('TS','T-Shirt'),
    ('S','Suit'),
    
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
      return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Deliverd','Deliverd'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    flutterwave_order_id = models.CharField(max_length=100,blank=True,null=True)
    flutterwave_payment_status = models.CharField(max_length=100,blank=True,null=True)
    flutterwave_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default='')
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)