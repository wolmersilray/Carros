from cars.models import Car
from cars.forms import CarModelForm 
from django.views.generic import ListView, CreateView

class CarListView(ListView):
    model= Car
    template_name= 'cars.html'
    context_object_name= 'cars'

    def get_queryset(self): #Aqui se execultao Filtro
        cars= super().get_queryset().order_by('factory_year')
        #SUPER= é uma funcão de orientação objeto do python para herdar propriedades da class Pai
        #.get_queryset= Aqui ela assume o "model= Car" que já existe.
        #.order_by= ordenar a list
        search= self.request.GET.get('search')
        if search:
            cars= cars.filter(model__icontains=search)
        return cars

class NewCarCreateView(CreateView):
    model= Car
    form_class= CarModelForm
    template_name= 'new_car.html'
    success_url= '/cars/'
