"""
URL configuration for my_order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from order_list import views as order_list_views
from events import views as events_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', order_list_views.orders_list, name = 'order_list'),
    path('events/', events_views.events_list, name = 'events_list'),    
    path('add/', order_list_views.add_order, name='add_new'),
    path('<int:number>/edit/', order_list_views.order_edit, name='edit'),
    path('sorted_orders/', order_list_views.sorted_orders, name='sorted'),

]
