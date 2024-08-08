from cars.models import Car
from cars.forms import CarModelForm 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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

#Emcapsulado esta classe com DECORATOR e executa a 
#função LOGIN_ REQUIRED, ou seja, se usuário não estiver logado não consegue acessar esta pagina.
#Como a tela de login é personalizado é usado "(login_url='login')" para mostra ao django o caminho para a tela de login.
@method_decorator(login_required(login_url='login'), name='dispatch') 
class NewCarCreateView(CreateView):
    model= Car
    form_class= CarModelForm
    template_name= 'new_car.html'
    success_url= '/cars/'


class CardetailView(DetailView):
    model= Car
    template_name= 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch') 
class CarUpdateView(UpdateView):
    model= Car
    form_class= CarModelForm
    template_name= 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch') 
class CarDeleteView(DeleteView):
    model= Car
    template_name= 'car_delete.html'
    success_url= '/cars/'
