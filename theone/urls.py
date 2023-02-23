from django.urls import path
from views import base_views

app_name = 'theone'

urlpatterns = [
    #base_views.py
    path('',base_views.index, name='index'),
    path('theone/<int:gu_id>/', base_views.detail, name='detail'),
]