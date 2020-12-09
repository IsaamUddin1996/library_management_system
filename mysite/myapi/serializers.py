from rest_framework import serializers

from .models import Library

class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('book_name', 'author', 'no_of_pages')