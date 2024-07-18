from django.urls import path
from .views import *


urlpatterns = [
    path('getFace',getFace,name='getFace'),
]
