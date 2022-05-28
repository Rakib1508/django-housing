from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models as gis_models
from django.db import models


class County(models.Model):
    county_number = models.IntegerField(primary_key=True)
    county_name = models.CharField(_('county'), max_length=50)
    label = models.CharField(_('label for county'), max_length=50, blank=True)
    boundary = gis_models.PolygonField()
    
    def __str__(self):
        return self.label


class City(models.Model):
    city_number = models.IntegerField(primary_key=True)
    city_name = models.CharField(_('city'), max_length=50)
    label = models.CharField(_('label for city'), max_length=50, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    boundary = gis_models.PolygonField()
    
    def __str__(self):
        return self.label


class PostalCode(models.Model):
    postal_code = models.IntegerField(primary_key=True)
    postal_location = models.CharField(_('postal location'), max_length=50)
    label = models.CharField(_('label for postal code'), max_length=50, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    boundary = gis_models.PolygonField()
    
    def __str__(self):
        return self.label
