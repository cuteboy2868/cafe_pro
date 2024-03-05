from rest_framework import serializers
from .models import *


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ChefSer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = "__all__"

class DeliverSer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = "__all__"



class DeliverySer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"

class CustomerSer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class PlaceSer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"

class FoodSer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"

class EmployeeSer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class CassaSer(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = "__all__"

