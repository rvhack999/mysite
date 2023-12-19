from django.contrib import admin
from .models import User, Worker, Order


# class UserAdmin(User):


admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Order)