from django.contrib import admin
from .models import Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ['name', 'industry',]
    list_display = ['id', 'name', 'industry',]
