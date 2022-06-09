from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ScoutList(generics.ListCreateAPIView):
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer
    name = 'scout-list'

class ScoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer
    name = 'scout-detail'


class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    name = 'team-list'


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    name = 'team-detail'


class AllocationList(generics.ListCreateAPIView):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
    name = 'allocation-list'


class AllocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
    name = 'allocation-detail'


class DegreeList(generics.ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    name = 'degree-list'


class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    name = 'degree-detail'


class ScoutDegreeList(generics.ListCreateAPIView):
    queryset = Scout_degree.objects.all()
    serializer_class = ScoutDegreeSerializer
    name = 'scoutDegree-list'


class ScoutDegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scout_degree.objects.all()
    serializer_class = ScoutDegreeSerializer
    name = 'scoutDegree-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'scouts': reverse(ScoutList.name, request=request),
            'teams': reverse(TeamList.name, request=request),
            'Allocation': reverse(AllocationList.name, request=request),
            'Degree': reverse(DegreeList.name, request=request),
            'Scout_degrees': reverse(ScoutDegreeList.name, request=request),
        })