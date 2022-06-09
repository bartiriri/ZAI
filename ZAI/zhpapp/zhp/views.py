from django.shortcuts import render
from rest_framework import generics
from  .models import *
from .serializers import *

class HarcerzList(generics.ListCreateAPIView):
    queryset = Harcerz.objects.all()
    serializer_class = HarcerzSerializer
    name = 'harcerz-list'


class HarcerzDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Harcerz.objects.all()
    serializer_class = HarcerzSerializer
    name = 'harcerz-detail'


class DruzynaList(generics.ListCreateAPIView):
    queryset = Druzyna.objects.all()
    serializer_class = DruzynaSerializer
    name = 'druzyna-list'

class DruzynaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Druzyna.objects.all()
    serializer_class = DruzynaSerializer
    name = 'druzyna-detail'

class PrzydzialList(generics.ListCreateAPIView):
    queryset = Harcerz_w_druzynie.objects.all()
    serializer_class = HarcerzWDruzynieSerializer
    name = 'przydzial-list'

class PrzydzialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Harcerz_w_druzynie.objects.all()
    serializer_class = HarcerzWDruzynieSerializer
    name = 'przydzial-detail'