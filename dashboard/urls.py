from django.urls import path
from .views import *


urlpatterns = [
    # >>>>>>>>>>>>>>>>> CRUD urls for Employee models <<<<<<<<<<<<<<<<< #
    path('get-employee-items/', GetAllEmployeeItems.as_view()),
    path('create-employee/', CreateEmployeeApiView.as_view()),
    path('update-employee/<int:pk>/', UpdateEmployeeItems.as_view()),
    path('delete-employee/<int:pk>/', DeleteEmployeeApiView.as_view()),


    # >>>>>>>>>>>>>>>>> CRUD urls for Chef models <<<<<<<<<<<<<<<<< #
    path('get-chef-items/', GetAllChefItems.as_view),
    path('create-chef-items/', CreateChefApiView.as_view),
    path('update-chef-items/<int:pk>/', UpdateChefItems.as_view),
    path('delete-chef-items/<int:pk>/', DeleteChefApiView.as_view),

    # >>>>>>>>>>>>>>>>> CRUD urls for Delivery models <<<<<<<<<<<<<<<<< #
    path('get-delivery-items/', GetAllDeliveryItems.as_view),
    path('create-delivery-items/', CreateDeliveryApiView.as_view),
    path('update-delivery-items/<int:pk>/', UpdateDeliveryItems.as_view),
    path('delete-delivery-items/<int:pk>/', DeleteDeliveryApiView.as_view),


    # >>>>>>>>>>>>>>>>> CRUD urls for Deliver models <<<<<<<<<<<<<<<<< #
    path('get-deliver-items/', GetAllDeliverItems.as_view),
    path('create-deliver-items/', CreateDeliverApiView.as_view),
    path('update-deliver-items/<int:pk>/', UpdateDeliverItems.as_view),
    path('delete-deliver-items/<int:pk>/', DeleteDeliverApiView.as_view),

    # >>>>>>>>>>>>>>>>> CRUD urls for Cassa models <<<<<<<<<<<<<<<<< #
    path('get-cassa-items/', GetCassaFoodItems.as_view),
    path('create-cassa-items/', CreateCassaApiView.as_view),
    path('update-cassa-items/<int:pk>/', UpdateCassaItems.as_view),
    path('delete-cassa-items/<int:pk>/', DeleteCassaApiView.as_view),

    # >>>>>>>>>>>>>>>>> CRUD urls for Customer models <<<<<<<<<<<<<<<<< #
    path('get-customer-items/', GetAllCustomerItems.as_view),
    path('create-customer-items/', CreateCustomerApiView.as_view),
    path('update-customer-items/<int:pk>/', UpdateCustomerItems.as_view),
    path('delete-customer-items/<int:pk>/', DeleteCustomerApiView.as_view),

    # >>>>>>>>>>>>>>>>> CRUD urls for Food models <<<<<<<<<<<<<<<<< #
    path('get-food-items/', GetAllFoodItems.as_view),
    path('create-food-items/', CreateFoodApiView.as_view),
    path('update-food-items/<int:pk>/', UpdateFoodItems.as_view),
    path('delete-food-items/<int:pk>/', DeleteFoodApiView.as_view),

    # >>>>>>>>>>>>>>>>> CRUD urls for Place models <<<<<<<<<<<<<<<<< #
    path('get-place-items/', GetAllPlaceItems.as_view),
    path('create-place-items/', CreatePlaceApiView.as_view),
    path('update-place-items/<int:pk>/', UpdatePlaceItems.as_view),
    path('delete-place-items/<int:pk>/', DeletePlaceApiView.as_view),
]
