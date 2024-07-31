from django.urls import path
from .views import *


urlpatterns = [
    path('fra/',fra,name='fra'),
]
