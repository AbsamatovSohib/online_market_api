from django.db import models
# from django.db.models import fields
import uuid
# Create your models here.

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    location = models.TextField()
    email = models.EmailField()
    number = models.BigIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


payment_method = (
    ("CH","Cash"),
    ("CD","Card"),
)

class Shopcard(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.CharField(max_length=10,null=True, blank=True)
    payment = models.CharField(choices=payment_method, default='CD', max_length=20)

    def __str__(self):
        return self.owner.name


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    name = models.CharField(max_length=200)
    # total = models.IntegerField()

    def __str__(self):
        return  self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopcard_id = models.ForeignKey(Shopcard, on_delete=models.CASCADE)
    sell_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name

