from django.urls import path
from . import views
app_name='custom'
urlpatterns = [
    path("",views.Home.as_view(),name='main'),
]