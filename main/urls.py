from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactme',views.contactme, name='contactme')
]