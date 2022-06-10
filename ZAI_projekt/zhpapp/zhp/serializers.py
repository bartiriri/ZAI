from rest_framework import serializers
from .models import Scout, Team, Allocation, Degree, Scout_degree


class ScoutSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Scout
        fields = ['pk', 'url', 'first_name', 'last_name', 'phone']

    def validate_phone(self,value):
        if len(value) < 9 or len(value) > 9:
            raise serializers.ValidationError('Numer musi mieć dokładnie 9 cyfr')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='allocation-detail')
    class Meta:
        model = Team
        fields = ['pk', 'url', 'team_number', 'team_name', 'email', 'team']


class AllocationSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field='team_name')
    scout = serializers.SlugRelatedField(queryset=Scout.objects.all(), slug_field='last_name')
    class Meta:
        model = Allocation
        fields = ['pk', 'url', 'team', 'scout']


class DegreeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Degree
        fields = ['pk', 'url', 'name']


class ScoutDegreeSerializer(serializers.HyperlinkedModelSerializer):
    degree = serializers.SlugRelatedField(queryset=Degree.objects.all(), slug_field='name')
    scout = serializers.SlugRelatedField(queryset=Scout.objects.all(), slug_field='last_name')
    class Meta:
        model = Scout_degree
        fields = ['pk', 'url', 'degree', 'scout']