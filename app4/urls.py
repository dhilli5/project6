from app4.views import *
from django.urls import path
app_name="something"
urlpatterns=[
    path('first_app4/',first_app4,name='first_app4'),
    path('second_app4/',second_app4,name='second_app4'),
]