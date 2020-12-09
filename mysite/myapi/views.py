from django.shortcuts import render
from rest_framework import viewsets

from .serializers import LibrarySerializer
from .models import Library


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('no_of_pages')
    serializer_class = LibrarySerializer
