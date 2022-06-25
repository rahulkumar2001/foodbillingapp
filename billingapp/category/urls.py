from django.urls import path
from .views import Restaurant

urlpatterns = [
    
    path("add_restaurant",Restaurant.as_view(),name="restaurant")
]
