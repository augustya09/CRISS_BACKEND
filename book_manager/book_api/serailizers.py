from .models import Book

from rest_framework import serializers

#JSON conversion and back 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


