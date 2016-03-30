from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Remiander(models.Model):
	src_lat = models.CharField(blank=False,max_length=64)
	src_lng = models.CharField(blank=False,max_length=64)
	dest_lat =models.CharField(blank=False,max_length=64)
	dest_lng= models.CharField(blank=False,max_length=64)
	reminder_time=models.CharField(blank=False,max_length=64)
	email =models.EmailField(blank=False)


