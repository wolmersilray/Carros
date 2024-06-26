from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import CarModelForm #alterando de Carforms para CarModelForm
from django.views import View

class CarsView(View):

    def get(self, request):
        cars= Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars= Car.objects.filter(model__contains=search)  

        return render(
            request, 
            'cars.html', 
            {'cars': cars}
    )
    

class NewCarView(View):

    def get(self, request):
        new_car_form= CarModelForm() #alterando de Carforms para CarModelForm
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form= CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})