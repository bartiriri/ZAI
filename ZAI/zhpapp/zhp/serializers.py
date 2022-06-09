from rest_framework import serializers
from .models import *

class HarcerzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harcerz
        fields = ['pk', 'imie', 'nazwisko', 'telefon', 'plec', 'data_dolaczenia']


class DruzynaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Druzyna
        fields = ['pk', 'nazwa_druzyny', 'numer_druzyny', 'data_zalozenia']


class HarcerzWDruzynieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harcerz_w_druzynie
        fields = ['pk', 'id_harcerz', 'id_druzyna', 'data_dolaczenia']


class StopienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stopien
        fields = ['pk', 'nazwa_stopnia']


class StopienHarcerzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stopien_harcerza
        fields = ['pk', 'id_harcerz', 'id_stopien', 'data_zdobycia']

