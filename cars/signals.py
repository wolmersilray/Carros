from venv import create
from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openia_api.client import get_car_ai_bio

#Função para calcular Iventário
def car_inventory_update():
    cars_count= Car.objects.all().count()
    cars_value= Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    if cars_count!= 0:
        CarInventory.objects.create(
            cars_count= cars_count,
            cars_value= cars_value
    )
#Instancia criara para preencher a bio automaticamente do novo veículo pré-cadastrada 
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ia_bio= get_car_ai_bio(
            instance.model, instance.brand, instance.model_year
        )
        instance.bio= ia_bio

#@receiver(pre_save, sender=Car) #Esta função capta informações no model Car sendo pré-save.
#def car_pre_save(sender, instance, **kwargs):
#    print('### PRE SAVE ###')
#    print(instance)

@receiver(post_save, sender=Car) 
def car_post_save(sender, instance, **kwargs):
    if create:
        car_inventory_update()

#@receiver(pre_delete, sender=Car) 
#def car_pre_delete(sender, instance, **kwargs):
#    print('### PRE DELETE ###')
#    print(instance)

@receiver(post_delete, sender=Car) 
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
    print('### PRE DELETE ###')
#    print(instance)