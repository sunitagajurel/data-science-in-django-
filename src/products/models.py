from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Product(models.Model): 
    name = models.CharField(max_length =220)
    date = models.DateTimeField(auto_now_add=True)
    
    #string representation of the object
    def __str__(self):
        return str(self.name)

class Purchase(models.Model):
    product= models.ForeignKey(Product,on_delete = models.CASCADE)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()
    total_price = models.PositiveIntegerField(blank = True)
    salesman = models.ForeignKey(User,on_delete = models.CASCADE)
    date = models.DateTimeField(default = timezone.now)


    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args,**kwargs)

    def __str__(self):
        return "{} {}s sold for {}".format(self.quantity, self.product.name,self.total_price)
