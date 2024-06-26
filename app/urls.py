from django.urls import path
from app.views import *

app_name="anything"

urlpatterns=[
    path("fire/",fire,name='fire'),
    path('sky/',sky,name='sky')
]