from django.urls import path

from .views import index, add_order

urlpatterns = [
    path('', index, name='order_list'), 
]