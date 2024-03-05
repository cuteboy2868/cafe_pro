from django.contrib import admin
from models import *
from . import models
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy,  as _

@admin.register(models.User)
class EmployeeAdmin(User):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number', 'full_name', 'address')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Place)
admin.site.register(Chef)
admin.site.register(Deliver)
admin.site.register(Delivery)
admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Cassa)




# Register your models here.
