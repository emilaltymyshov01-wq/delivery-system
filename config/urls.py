"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cargo.views import driver_list, dispatcher_detail, driver_detail, dispatcher_list
from cargo.views import client_list, client_detail
from cargo.views import order_list, order_detail, order_create, operators_page


urlpatterns = [
    path('admin/', admin.site.urls),

    path('drivers/', driver_list, name='driver_list'),
    path('drivers/<int:pk>/', driver_detail, name='driver_detail'),

    path('dispatchers/', dispatcher_list, name='dispatcher_list'),
    path('dispatchers/<int:pk>/', dispatcher_detail, name='dispatcher_detail'),

    path('clients/', client_list, name='client_list'),
    path('clients/<int:pk>/', client_detail, name='client_detail'),

    path('orders/', order_list, name='order_list'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
    path('orders/new/', order_create, name='order_create'),
    path('operators/', operators_page, name='operators_page'),
    
]
