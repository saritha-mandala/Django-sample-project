from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('',views.hello_geeks),
  path('form1/',views.home_view)
]