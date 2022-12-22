from django.urls import path
from . import views


app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('package', views.package,name="package"),
    path('uiux', views.uiux,name="uiux"),
]