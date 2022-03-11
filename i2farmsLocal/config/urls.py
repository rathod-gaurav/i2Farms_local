from unicodedata import name
from django.urls import path, re_path
from . import views

app_name = 'config'

urlpatterns = [
    # path('', views.view_config, name="view_config"),
    path('add_plant', views.add_plant, name="add_plant"),
    path('edit_config/<crop_id>', views.edit_config, name='edit_config')
]