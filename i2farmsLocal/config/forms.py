from django import forms
from . import models

class AddNewPlant(forms.ModelForm):
    class Meta:
        model = models.AddPlant
        fields = ['crop_name', 'start_date', 'no_growth_stages', 'life_span']


class EditConfig(forms.ModelForm):
    class Meta:
        model = models.Config
        fields = ['crop_name', 'start_date', 'stage_no', 'stage_name', 'span', 't1_ll', 't1_ul', 't1_err', 'h1_ll', 'h1_ul', 'h1_err', 't2_ll', 't2_ul', 't2_err', 'h2_ll', 'h2_ul', 'h2_err', 'pH_ll', 'pH_ul', 'pH_err', 'tds_ll', 'tds_ul', 'tds_err']