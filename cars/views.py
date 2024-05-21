from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import CarForm


def cars_view(request):
    cars= Car.objects.all().order_by('model')
    search = request.GET.get('search')
    #print(request.GET.get('search'))  #por este comando conseguimos extrair as buscas que o cliente faz.
    #print(request.GET)  #por este comando conseguimos extrair as buscas que o cliente faz.

    if search:
        cars= Car.objects.filter(model__contains=search)  
    
    #cars= Car.objects.filter(brand=2)  #Busca os carros pela ID cadastrada no BD"
    #cars= Car.objects.filter(brand__name='Chevrolet')  #Busca todos os carros do modelo "Chevrolet"
    #cars= Car.objects.filter(model='Uno')  #Busca todos o modelo de carro no BD
    #cars= Car.objects.filter(model__contains='Marajó')  #Busca todos os carros que CONTEM a informação "Marajó"

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )

def new_car_view(request):
    if request.method == 'POST':
        new_car_form= CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form= CarForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})