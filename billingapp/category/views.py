from django.shortcuts import render
from .models import *
from rest_framework.views import APIView

# class CategoryList(APIView):
#     def post(request):
#         data=request.data

class Restaurant(APIView):
    def post(self,request):
        data=request.data
        restaurant_name=data.get("restaurant_name")
        description=data.get("description")
        total_table=data.get("total_table")
        obj=Restaurant.objects.create(restaurant_name=restaurant_name,description=description,total_table=total_table)
        obj.resaurant_name
        
        res={
            "message":"success",
            "id":obj.id,
            "resaurant_name":obj.resaurant_name
        }
        return res


        


