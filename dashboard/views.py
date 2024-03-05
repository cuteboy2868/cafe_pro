from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from models import *
from main.serializers import *


"""  CRUD Chef model  """


class GetAllChefItems(ListAPIView):
    queryset = Chef.objects.all().order_by('-id')
    serializer_class = ChefSer


class UpdateChefItems(CreateAPIView):
    queryset = Chef.objects.all().order_by('-id')
    serializer_class = ChefSer


class CreateChefApiView(CreateAPIView):
    queryset = Chef.objects.all().order_by('-id')
    serializer_class = ChefSer


class DeleteChefApiView(DestroyAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSer


"""  CRUD Deliver model  """


class GetAllDeliverItems(ListAPIView):
    queryset = Deliver.objects.all().order_by('-id')
    serializer_class = DeliverSer


class UpdateDeliverItems(CreateAPIView):
    queryset = Deliver.objects.all().order_by('-id')
    serializer_class = DeliverSer


class CreateDeliverApiView(CreateAPIView):
    queryset = Deliver.objects.all().order_by('-id')
    serializer_class = DeliverSer


class DeleteDeliverApiView(DestroyAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSer



"""  CRUD Delivery model  """


class GetAllDeliveryItems(ListAPIView):
    queryset = Delivery.objects.all().order_by('-id')
    serializer_class = DeliverySer


class UpdateDeliveryItems(CreateAPIView):
    queryset = Delivery.objects.all().order_by('-id')
    serializer_class = DeliverySer


class CreateDeliveryApiView(CreateAPIView):
    queryset = Delivery.objects.all().order_by('-id')
    serializer_class = DeliverySer


class DeleteDeliveryApiView(DestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySer


"""  CRUD Customer model  """


class GetAllCustomerItems(ListAPIView):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSer


class UpdateCustomerItems(CreateAPIView):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSer


class CreateCustomerApiView(CreateAPIView):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSer


class DeleteCustomerApiView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSer


"""  CRUD Place model  """


class GetAllPlaceItems(ListAPIView):
    queryset = Place.objects.all().order_by('-id')
    serializer_class = PlaceSer


class UpdatePlaceItems(CreateAPIView):
    queryset = Place.objects.all().order_by('-id')
    serializer_class = PlaceSer


class CreatePlaceApiView(CreateAPIView):
    queryset = Place.objects.all().order_by('-id')
    serializer_class = PlaceSer


class DeletePlaceApiView(DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSer


"""  CRUD Food model  """


class GetAllFoodItems(ListAPIView):
    queryset = Food.objects.all().order_by('-id')
    serializer_class = FoodSer


class UpdateFoodItems(CreateAPIView):
    queryset = Food.objects.all().order_by('-id')
    serializer_class = FoodSer


class CreateFoodApiView(CreateAPIView):
    queryset = Food.objects.all().order_by('-id')
    serializer_class = FoodSer


class DeleteFoodApiView(DestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSer


"""  CRUD Employee model  """


class GetAllEmployeeItems(ListAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer


class UpdateEmployeeItems(CreateAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer


class CreateEmployeeApiView(CreateAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer


class DeleteEmployeeApiView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


"""  CRUD Cassa model  """


class GetCassaFoodItems(ListAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializer_class = CassaSer


class UpdateCassaItems(CreateAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializer_class = CassaSer


class CreateCassaApiView(CreateAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializer_class = CassaSer


class DeleteCassaApiView(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer

