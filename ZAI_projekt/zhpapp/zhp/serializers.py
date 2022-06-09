from rest_framework import serializers
from .models import Scout, Team, Allocation, Degree, Scout_degree


class ScoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scout
        fields = ['pk', 'url', 'first_name', 'last_name', 'phone']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['pk', 'url', 'team_number', 'team_name', 'email']


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = ['pk', 'url', 'team', 'scout']


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['pk', 'url', 'name']


class ScoutDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scout_degree
        fields = ['pk', 'url', 'degree', 'scout']