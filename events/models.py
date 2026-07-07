from django.db import models


from order_list.models import Order
# Create your models here.
class Event(models.Model):


    CLASS_EVENT = (
        ('critical_error', 'Кртитическая ошибка ПО'),
        ('rework', 'Доработка ПО'),
        ('mp_release', 'Продакшн релиз'),   
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name = 'events')
    type = models.CharField(max_length=15, choices=CLASS_EVENT, default='critical_error', verbose_name='Тип') 
    description = models.CharField(max_length=150,verbose_name='Описание')  
    date = models.DateField(verbose_name='Дата получения обнаружения')       


    def __str__(self):
        return f"{self.type} - {self.order}"     

    class Meta:
        verbose_name = 'События'
        ordering = ['order', 'date']    
