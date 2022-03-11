from django.shortcuts import render

# Create your views here.
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import AddPlant
from . import forms

def add_plant(request):
    if request.method=='POST':
        formTop = forms.AddNewPlant(request.POST)
        if formTop.is_valid():
            #save Crop to database
            instance = formTop.save(commit=False)
            instance.save()
            crop_id = instance.id
            # return HttpResponse(f'{instance.id}')
            return redirect('config:edit_config', crop_id = crop_id)
    else:
        formTop = forms.AddNewPlant()
    return render(request, "config/add_plant.html", {'formTop':formTop})

def edit_config(request, crop_id):
    #populate details of crop passed from previous page
    crop = AddPlant.objects.get(id = crop_id)

    if request.method == 'POST':
        configForm = forms.EditConfig(request.POST, initial={'crop_name':crop.crop_name, 'start_date':crop.start_date})
        # configForm.crop_name = crop.crop_name
        # configForm.start_date = crop.start_date
        if configForm.is_valid():
            #save config to database
            instance = configForm.save(commit=False)
            instance.save()
            settings_id = instance.id
            return HttpResponse(f'config saved successfully {settings_id}')
    else:
        configForm = forms.EditConfig(initial={'crop_name':crop.crop_name, 'start_date':crop.start_date})
    return render(request, 'config/edit_config.html', {'crop':crop, 'form':configForm})
    # crop_name = AddPlant.objects.get(cop_name = crop_name)

    