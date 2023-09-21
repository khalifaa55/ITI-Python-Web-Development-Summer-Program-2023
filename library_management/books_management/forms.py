from django import forms
from .models import Book, publishing_house
from django.forms import DateTimeInput

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {'isbn', 'name', 'publish_date','publishing_house','image'}
        widgets = {
            'isbn': forms.TextInput(attrs = {'class':'form-control'}),
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'publish_date': forms.DateInput(attrs = {'class':'form-control'}),
            'publishing_house': forms.Select(attrs = {'class':'form-control'}, choices=publishing_house.objects.values_list('id','name')),
            'image': forms.FileInput(attrs = {'class':'form-control-file'}),
        }