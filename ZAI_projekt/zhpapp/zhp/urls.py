from django.urls import path
from . import views

urlpatterns = [
    path('scouts', views.ScoutList.as_view(), name=views.ScoutList.name),
    path('scouts/<int:pk>', views.ScoutDetail.as_view(), name=views.ScoutDetail.name),
    path('teams', views.TeamList.as_view(), name=views.TeamList.name),
    path('teams/<int:pk>', views.TeamDetail.as_view(), name=views.TeamDetail.name),
    path('allocations', views.AllocationList.as_view(), name=views.AllocationList.name),
    path('allocations/<int:pk>', views.AllocationDetail.as_view(), name=views.AllocationDetail.name),
    path('degrees', views.DegreeList.as_view(), name=views.DegreeList.name),
    path('degrees/<int:pk>', views.DegreeDetail.as_view(), name=views.DegreeDetail.name),
    path('scout_degrees', views.ScoutDegreeList.as_view(), name=views.ScoutDegreeList.name),
    path('scout_degrees/<int:pk>', views.ScoutDegreeDetail.as_view(), name=views.ScoutDegreeDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]