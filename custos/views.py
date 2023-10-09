from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from django.http import JsonResponse
from rest_framework import viewsets


# Create your views here.
# def customers(request):
#     data = Customer.objects.all()
#     serializer = CustomerSerializer(data, many=True)
#     return JsonResponse({'customers': serializer.data})


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()



