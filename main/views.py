from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from models import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import *


@api_view(['GET'])
def filter_employee_username(request):
    username_id = request.GET.get('username')
    users = Employee.objects.filter(user_id=username_id).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_address(request):
    address = request.GET.get('address')
    users = Employee.objects.filter(address=address).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_profession(request):
    profession = request.GET.get('profession')
    users = Employee.objects.filter(profession=profession).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_rating(request):
    employee = Employee.objects.all().order_by('-rating')[:1]
    ser = EmployeeSer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_customer_name(request):
    owner_name = request.GET.get('owner_name')
    users = Customer.objects.filter(owner_name=owner_name).order_by('-id')
    ser = CustomerSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_customer_address(request):
    address = request.GET.get('address')
    users = Customer.objects.filter(address=address).order_by('-id')
    ser = CustomerSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_admin(request):
    admin_id = request.GET.get('admin')
    users = Cassa.objects.filter(admin_id=admin_id).order_by('-id')
    ser = CassaSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_order(request):
    order_id = request.GET.get('order')
    users = Cassa.objects.filter(order_id=order_id).order_by('-id')
    ser = CassaSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_type(request):
    payment_type = request.GET.get('payment_type')
    users = Cassa.objects.filter(payment_type=payment_type).order_by('-id')
    ser = CassaSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_employee(request):
    employee_id = request.GET.get('employee')
    users = Employee.objects.filter(employee_id=employee_id).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_problem(request):
    problem = request.GET.get('problem')
    users = Employee.objects.filter(problem=problem).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_cost(request):
    users = Employee.objects.filter().order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)



