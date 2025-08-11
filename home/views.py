from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.db import DatabaseError
# Create your views here.
@api_view(['GET'])
def menu_items(request):
    items = [
        {"id":1, "name":"Cheese Corn Pizza", "price":"250"},
        {"id":2, "name":"Cheese Dosa", "price":"180"},
        {"id":3, "name":"Sizzling Brownie", "price":"220"}
    ]
    return Response(items)

def contact_us(request):
    contact_info:{
        "phone":"+91 1023456789",
        "email":"resto@gmail.com",
        "address":"151, Rose Building, Lili Road"
    }
    return render(request,"contact.html",{"contact_info": contact_info})

def reservation(request):
    return render(request, "reservation.html")

def rest_home(request):
    try:
        restaurant=RESTAURANT.objects.first()
        if not restaurant:
            return HttpResponse("No restaurant data available", status=404)
        return render(request, "home.html", {"restaurant": restaurant})
    except DatabaseError as e:
        return HttpResponse(f"Database error: {e}", status=500)