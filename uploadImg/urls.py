from django.urls import path
# from django.contrib import admin
from uploadImg.views import upload_file


urlpatterns = [
    path('upload/',upload_file,name='upload'),
]
