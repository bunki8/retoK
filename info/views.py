from django.shortcuts import render
from .models import info
from rest_framework import generics
from .serializers import infoSerializer


class infoCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = info.objects.all()
    serializer_class = infoSerializer
class infoList(generics.ListCreateAPIView):
    serializer_class = infoSerializer
    queryset = info.objects.all()

class infoDetail(generics.RetrieveAPIView):
    queryset = info.objects.all()
    serializer_class = infoSerializer

class infoUpdate(generics.RetrieveUpdateAPIView):
    queryset = info.objects.all()
    serializer_class = infoSerializer
    

class infoDelete(generics.RetrieveDestroyAPIView):
    queryset = info.objects.all()
    serializer_class = infoSerializer
    