from django.shortcuts import render, redirect

from ispitnaApp.forms import RealEstateForm
from ispitnaApp.models import RealEstate, RealEstateCharacteristic


# Create your views here.
def index(request):
    houses = RealEstate.objects.filter(is_bought=False).all()
    context = []
    for house in houses:
        price = 0
        house_characteristics = RealEstateCharacteristic.objects.filter(real_estate=house).all()
        for house_characteristic in house_characteristics:
            price += house_characteristic.characteristic.price
        context.append({'house': house, 'price': price})
    return render(request, 'index.html', {'houses': context})


def edit(request, house_id):
    instance = RealEstate.objects.filter(id=house_id).first()
    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = RealEstateForm(instance=instance)
    return render(request, 'edit.html', {'form': form, 'house_id': house_id})
