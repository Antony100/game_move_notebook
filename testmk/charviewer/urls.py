from django.urls import path
from . import views


urlpatterns = [
    path('', views.Characters.as_view(), name='characters'),
    path('baraka', views.BarakaFrames.as_view(), name='baraka'),
    path('cassie', views.CassieFrames.as_view(), name='cassie'),
]
