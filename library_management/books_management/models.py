from django.db import models

# Create your models here.
class publishing_house(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    isbn = models.BigIntegerField()
    name = models.CharField(max_length=200)
    publish_date = models.DateField()
    publishing_house = models.ForeignKey(publishing_house, on_delete=models.CASCADE,null=True ,blank=True)
    image = models.ImageField(upload_to='book_images/',null=True, blank=True)
    