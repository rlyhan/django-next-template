from django.shortcuts import render
from rest_framework import generics

from .models import TestModel
from .serializers import TestModelSerializer

class TestModelListView(generics.ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer


class TestModel(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
