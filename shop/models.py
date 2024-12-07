from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'




class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default=1)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50, default='', blank=True, null=True)
    phone = models.CharField(max_length=15, default='', blank=True, null=True)
    date_ordered = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name} {self.quantity}'
