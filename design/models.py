from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField


# Create your models here.
SIZES = (
        ('S' , 'Small'),
        ('M' , 'Medium'),
        ('L', 'Large'),
        ('XL', 'ExtraLarge'),
    )
COLOR = (
    ('R', 'Red'),        
    ('B', 'Blue'),
    ('W', 'White'),
    ('G', 'Green'),
    ('Gr', 'Gray'),

)
class User(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users", blank=True, null=True)

    def __str__(self):
        return self.user.username

class Design(models.Model):
    file = models.FileField(upload_to='design/', default='xyz.png')
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True , null=True)

    def __str__(self):
        return self.file.name

class ProductType(models.Model):
    Type = models.CharField(max_length=200)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.Type

class Product(models.Model):
    name = models.CharField(max_length=200)
    product_type = models.ForeignKey(ProductType, related_name="products", on_delete=models.CASCADE,default=None)
    created_date = models.DateTimeField(blank=True , null=True)
    updated_date = models.DateTimeField(blank=True , null=True)
    available_sizes = MultiSelectField(max_length=10 , choices=SIZES, default='M', max_choices=3)
    available_colors = MultiSelectField(max_length=10 , choices=COLOR, default='R', max_choices=3)
    design = models.ManyToManyField(Design)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('initial', 'Initial'),
        ('abondoned', 'Abondoned'),
        ('pending', 'Pending'),
        ('finished','Finished'),
    )
    ordered_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE, default=None)
    status = models.TextField(max_length=10, choices=STATUS ,default='initial')
    size = models.TextField(max_length=10)
    color = models.TextField(max_length=10)

    def __str__(self):
        return self.user.user.username

