from django.urls import path
from app2.views import *

app_name='anything'

urlpatterns=[
    path('heart/',heart,name='heart'),
    path('smile/',smile,name='smile'),
]