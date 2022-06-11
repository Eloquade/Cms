from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landingpage, name="cms"),
    path('home', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('user/', views.userpage, name='user'),
    path('account/', views.account_settings, name='account'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.registration_page, name='register'),

    path('customers/<str:pk_test>/', views.customers, name="customers"),
    path('create_customers/<str:pk_test>/', views.create_customer, name="create_customers"),



    path('create_order/<str:pk>/', views.create_order, name="create_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/resetpassword.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/passwordsent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/passwordresetconfirm.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/passwordresetdone.html"), name="password_reset_complete"),

]
