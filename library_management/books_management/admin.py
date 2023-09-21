from django.contrib import admin
from .models import Book, publishing_house
# Register your models here.
admin.site.register(Book)
admin.site.register(publishing_house)