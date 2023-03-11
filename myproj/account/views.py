from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def customer_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            cust = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(cust)
            return Response(serializer.data)
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response({'msg': 'Customer Added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        cust = Customer.objects.get(pk=pk)
        cust.delete()
        return Response({'msg': 'Customer Removed'})