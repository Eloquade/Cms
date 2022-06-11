from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import pyrebase
from django.contrib.auth import authenticate, login, logout
# create your view here
from .models import *
from .forms import orderform, CreateUserForm, ContactForm, customerform
from .filters import OrderFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only


config={
      "apiKey": "AIzaSyAOpCcgGhPYLzZhmFkuebrm8MIiI2GtNlM",
      "authDomain": "dcms-c7f9f.firebaseapp.com",
      "projectId": "dcms-c7f9f",
      "storageBucket": "dcms-c7f9f.appspot.com",
      "messagingSenderId": "646854789578",
      "appId": "1:646854789578:web:cbe9919a60e445c3376733",
      "databaseURL": "https://dcms-c7f9f-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()



@unauthenticated_user
def registration_page(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def landingpage(request):

    pass
    # form = ContactForm()
    # if request.method == 'POST':
    #     form = customerform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # context = {'form': form}

    return render(request, 'accounts/landingpage.html')


def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()

    total_customer = customer.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customer': customer, 'total_customer': total_customer, 'delivered': delivered,
                  'pending': pending, 'total_orders': total_orders}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    all_products = Product.objects.all()
    return render(request, 'accounts/Products.html', {'products': all_products})


def customers(request, pk_test):
    customers_info = Customer.objects.get(id=pk_test)
    orders = customers_info.order_set.all()
    total_orders = orders.count()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs
    context = {'customer_info': customers_info, 'order': orders, 'total_orders': total_orders, 'my_filter': my_filter}
    return render(request, 'accounts/customers.html', context)


def create_customer(request, pk_test):
    form = customerform()
    if request.method == 'POST':
        form = customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/create_customer.html', context)


def create_order(request, pk):
    form = orderform()
    # form = orderform(initial={'customer': customer_info})
    if request.method == 'POST':
        # print('printing post:', request.POST)
        form = orderform(request.POST)
        # form = OrderFormsSet(request.POST, instance=customer_info)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = orderform(instance=order)
    if request.method == 'POST':
        # print('printing post:', request.POST)
        form = orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/update.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


def userpage(request):
    orders = request.user.customer.order_set.all()
    customer = Customer.objects.all()
    total_customer = customer.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    # print('ORDERS', orders)

    context = {'orders': orders, 'total_customer': total_customer, 'delivered': delivered,
               'pending': pending, 'total_orders': total_orders}
    return render(request, 'accounts/user.html', context)


def account_settings(request):
    customer = request.user.customer
    form = customerform(instance=customer)

    if request.method == 'POST':
        form = customerform(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/account.html', context)
# Create your views here.
