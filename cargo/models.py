from django.db import models

class Driver(models.Model):
    name_driver = models.CharField()
    def __str__(self):
        return self.name_driver


class Dispatcher(models.Model):
    name_dispatcher = models.CharField()


class Client(models.Model):
    name_client = models.CharField()        



class Order(models.Model):
    name_order = models.CharField()
    price = models.IntegerField()
    delivery_address = models.CharField()
    creation_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    driver = models.ForeignKey(Driver, related_name= 'Orders', on_delete= models.SET_NULL, null= True, blank=True)
    dispatcher = models.ForeignKey(Dispatcher, related_name= 'Orders', on_delete= models.SET_NULL, null= True, blank=True)
    client = models.ForeignKey(Client, related_name= "Orders", on_delete= models.SET_NULL, null= True, blank=True)
     

# Create your models here.
