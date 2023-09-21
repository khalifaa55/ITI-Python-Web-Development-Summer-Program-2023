from rest_framework import serializers
from .models import Book, publishing_house

class publishing_houseSerializer(serializers.ModelSerializer):
    class Meta:
        model = publishing_house
        fields = ('id','name')

class BookSerializer(serializers.ModelSerializer):
    publishing_house = publishing_houseSerializer(read_only=True)
    publishing_house_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Book
        fields = ('isbn','name', 'publish_date', 'image', 'publishing_house', 'publishing_house_id')
