from django.urls import path,include
from .views import home_view
from django.urls import path,include

urlpatterns = [
    path('home', home_view)
]