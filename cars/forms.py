from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):
    model= forms.CharField(max_length=200, required=False)
    brand= forms.ModelChoiceField(Brand.objects.all(), required=False)
    factory_year= forms.IntegerField(required=False)
    model_year= forms.IntegerField(required=False)
    plate= forms.CharField(max_length=10, required=False)
    value= forms.FloatField(required=False)
    photo= forms.ImageField(required=False)

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


