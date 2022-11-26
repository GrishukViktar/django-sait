from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('communications', views.communications, name='communications'),
    path('homework', views.homework, name='homework'),

]
