from . import views
from django.urls import path
urlpatterns = [
    path('', views.first, name='mobile'),
    path('footwear/', views.shoo, name='footwear'),
    path('baby/', views.baby, name='baby'),
]