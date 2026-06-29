from django.db import models

# Create your models here.
class Order(models.Model):

    STATUS_ORDER = (
        ('work', 'В работе'),
        ('not_run', 'Выполнен, но не запущен'),
        ('done', 'Запущен'),                
    )

    STATUS_ROM = (
        ('NOT', 'Не сделаны'),
        ('YES', 'Сделаны'),             
    )

    number = models.PositiveSmallIntegerField(verbose_name='Номер заказ-наряда')
    equipment = models.CharField(max_length=45, verbose_name='Наименование')
    plc_name = models.CharField(max_length=15, verbose_name='ПЛК')
    hmi_name = models.CharField(max_length=15, verbose_name='Панель')
    regul_name = models.CharField(max_length=15,verbose_name='Измеритель')
    date = models.DateField(verbose_name='Дата получения заказа')   
    status = models.CharField(max_length=15, choices=STATUS_ORDER, default='work', verbose_name='Статус')
    pid_regul = models.CharField(max_length=15, verbose_name='ПИД регулятор') 
    scada = models.CharField(max_length=25, verbose_name='SCADA')
    opc = models.CharField(max_length=25,verbose_name='OPC')
    comments = models.TextField(max_length=250, verbose_name='Комментарий')
    status_rom = models.CharField(max_length=15, choices=STATUS_ROM, default='NOT', verbose_name='Статус заявок')
    date_rom  = models.DateField(verbose_name='Дата заявки')

    def __str__(self):
        return f"{self.number} - {self.equipment}"     

    class Meta:
        verbose_name = 'Заказы'
        ordering = ['number', 'date']




