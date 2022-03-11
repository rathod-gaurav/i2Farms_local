from django.db import models
from datetime import date

# Create your models here.
class AddPlant(models.Model):
    crop_name = models.CharField(max_length=50)
    start_date = models.DateField(default=date.today)
    no_growth_stages = models.PositiveSmallIntegerField()
    life_span = models.PositiveSmallIntegerField() #life span in days

    def __str__(self):
        return self.crop_name

class Config(models.Model):
    crop_name = models.CharField(max_length=50)
    start_date = models.DateField(default=date.today)
    
    stage_no = models.PositiveSmallIntegerField()
    stage_name = models.CharField(max_length=50, default=1)
    span = models.PositiveSmallIntegerField() #no. of days this growth stage will span
    #nutrient tank temperature and humidity
    t1_ll = models.DecimalField(max_digits=4, decimal_places=2) 
    t1_ul = models.DecimalField(max_digits=4, decimal_places=2)
    t1_err = models.DecimalField(max_digits=4, decimal_places=2, default = 0.10)
    h1_ll = models.DecimalField(max_digits=4, decimal_places=2) 
    h1_ul = models.DecimalField(max_digits=4, decimal_places=2)
    h1_err = models.DecimalField(max_digits=4, decimal_places=2, default = 0.10)
    #plants temperature and humidity
    t2_ll = models.DecimalField(max_digits=4, decimal_places=2) 
    t2_ul = models.DecimalField(max_digits=4, decimal_places=2)
    t2_err = models.DecimalField(max_digits=4, decimal_places=2, default = 0.10)
    h2_ll = models.DecimalField(max_digits=4, decimal_places=2) 
    h2_ul = models.DecimalField(max_digits=4, decimal_places=2)
    h2_err = models.DecimalField(max_digits=4, decimal_places=2, default = 0.10)
    #pH of nutrient tank
    pH_ll = models.DecimalField(max_digits=4, decimal_places=2) 
    pH_ul = models.DecimalField(max_digits=4, decimal_places=2)
    pH_err = models.DecimalField(max_digits=4, decimal_places=2, default = 0.10)
    #tds of nutrient tank
    tds_ll = models.DecimalField(max_digits=4, decimal_places=2) 
    tds_ul = models.DecimalField(max_digits=4, decimal_places=2)
    tds_err = models.DecimalField(max_digits=4, decimal_places=2, default = 0.10)
    
    def __str__(self):
        return self.stage_name