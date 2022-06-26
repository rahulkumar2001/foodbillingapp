from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

# class CategoryList(APIView):
#     def post(request):
#         data=request.data

class Restaurantlist(APIView):
    def post(self,request):
        data=request.data
        restaurant_name=data.get("restaurant_name")
        description=data.get("description")
        total_table=data.get("total_table")
        obj=Restaurant.objects.create(restaurant_name=restaurant_name,description=description,total_table=total_table)
        obj.restaurant_name
        
        res={
            "message":"success",
            "id":obj.id,
            "restaurant_name":obj.restaurant_name
        }
        return res

class RestaurantGetData(APIView):
    def get(self,request):
        data=Restaurant.objects.all() 
        list1=[]
        for i in data:
            dic={"Restaurant_name":i.restaurant_name,
            "Description":i.description,
            "total_table":i.total_table

            }
            list1.append(dic)
        print (data)   
        return Response({"Data":list1,"status":True})    


class Categorylist(APIView):
    def post(self,request):
        data=request.data  
        restaurant=data.get('restaurant')
        items=data.get('items')
        food_name=data.get('food_name')   
        obj1=Category.objects.create(restaurant=restaurant,items=items,food_name=food_name) 
        res={
            "message":"Success",
            "id":obj1.id,
            "Restaurant":restaurant
        }    
        return res 

class CategoryGetData(APIView):
    def get(self,request):
        data=Category.objects.all()
        list2=[]
        for i in data:
            dic1={"Restaurant":i.restaurant,
                    "items":i.items,
                    "food_name":i.food_name
                    
                    }
            list2.append(dic1)
        print (data)  
        return Response({"data":list2,"status":True})  


class OrderDetails(APIView):
    def post(self,request):
        data=request.data
        order_id=data.get('order_id')
        food_name=data.get('food_name')
        total_num=data.get('total_num')
        obj=Order.objects.create(order_id=order_id,food_name=food_name,total_table=total_table)  
        res={
            "message":"success",
            "id":obj.id,
            "Table_num":obj.table_num

        }
        return res

class OrderGetData(APIView):
    def get(self,request):
        data=Order.objects.all()
        list1=[]
        for i in data:
            dic={
                "order_id":i.order_id,
                "food_name":i.food_name,
                "table_num":i.table_num


            }
            list1.append(dic)
            print (data)
            return Response({"data":list1,"status":True})
    


        


