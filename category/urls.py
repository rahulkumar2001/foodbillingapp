from django.urls import path

# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path("add_restaurant",views.Restaurantlist.as_view(),name="add_restaurant"),
    path("get_resto_data",views.RestaurantGetData.as_view(),name="get_resto_data"),
    path("add_category/",views.Categorylist.as_view(),name="add_Category"),
    path("Category_Get_Data",views.CategoryGetData.as_view(),name="Category_Get_Data")
]
