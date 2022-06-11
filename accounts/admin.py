from django.contrib import admin
from .models import Customer, Product, Order, Tag, Contact, Profile


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'date_created']
    search_fields = ['id', 'name', 'phone', 'email', 'date_created']
    # list_filter = ['id', 'name', 'phone', 'email', 'date_created']
    ordering = ('id', 'name', 'phone', 'email', 'date_created')


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'description', 'date_created']
    search_fields = ['id', 'name', 'price', 'category', 'description', 'date_created']
    # list_filter = ['id', 'name', 'price', 'category', 'description', 'date_created']
    ordering = ('id', 'name', 'price', 'category', 'description', 'date_created')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'date_created']
    search_fields = ['id', 'status', 'date_created']
    # list_filter = ['id', 'status', 'date_created']
    ordering = ('id', 'status', 'date_created')


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'email', 'phone_number', 'message']
    search_fields = ['id', 'firstname', 'lastname', 'email', 'phone_number', 'message']
    # list_filter = ['id', 'status', 'date_created']
    ordering = ('id', 'firstname', 'lastname', 'email', 'phone_number', 'message')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'firstname', 'lastname',  'phone']
    search_fields = ['id', 'user', 'firstname', 'lastname', 'phone']
    # list_filter = ['id', 'status', 'date_created']
    ordering = ('id', 'user', 'firstname', 'lastname', 'phone')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile, ProfileAdmin)
# Register your models here.
