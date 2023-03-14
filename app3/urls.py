from app3.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
    path('third/',third,name='third'),
    path('forth/',forth,name='forth'),
    path('fifth/',fifth,name='fifth'),
]
