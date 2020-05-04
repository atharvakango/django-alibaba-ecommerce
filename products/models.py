from django.db import models
from django.utils.text import slugify
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')


    # def save(self):
    # 	self.slug = slugify(self.title)
    # 	super(Product, self).save()


    def __str__(self):
        return self.name
        
