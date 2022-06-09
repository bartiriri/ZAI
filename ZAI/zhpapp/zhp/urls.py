from django.urls import path
from . import views

urlpatterns = [
    path('harcerze', views.HarcerzList.as_view(), name=views.HarcerzList.name),
    path('harcerze/<int:pk>', views.HarcerzDetail.as_view(), name=views.HarcerzDetail.name),
    path('druzyny', views.DruzynaList.as_view(), name=views.DruzynaList.name),
    path('druzyny/<int:pk>', views.DruzynaDetail.as_view(), name=views.DruzynaDetail.name),
    path('przydzialy', views.PrzydzialList.as_view(), name=views.PrzydzialList.name),
    path('przydzialy/<int:pk>', views.PrzydzialDetail.as_view(), name=views.PrzydzialDetail.name),
]