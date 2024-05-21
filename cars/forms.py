from django import forms
from cars.models import Brand, Car

#FORMS SIMPLES
class CarForm(forms.Form):
    model= forms.CharField(max_length=200)
    brand= forms.ModelChoiceField(Brand.objects.all())
    factory_year= forms.IntegerField()
    model_year= forms.IntegerField()
    plate= forms.CharField(max_length=10)
    value= forms.FloatField()
    photo= forms.ImageField()

    def save(self):
        car = Car(
            model= self.cleaned_data['model'],
            brand= self.cleaned_data['brand'],
            factory_year= self.cleaned_data['factory_year'],
            model_year= self.cleaned_data['model_year'],
            plate= self.cleaned_data['plate'],
            value= self.cleaned_data['value'],
            photo= self.cleaned_data['photo'],
        )
        car.save()
        return car

#Model FORMS AVANÇADO (que substitui todo o forms simples)
class CarModelForm(forms.ModelForm):
    class Meta: #reescrever a class
        model= Car #Tabela do BD
        fields= '__all__'  #Os campos da tabela Cars(nesta caso TODOS)


