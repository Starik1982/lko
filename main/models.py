from django.db import models
from .models import *



class Logotip (models.Model):
	name =  models.CharField(max_length=64, blank=True, null=True, default=None)	
	image_1 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_2 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_3 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_4 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_5 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_6 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_7 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_8 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_9 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	image_10 = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	def __str__(self):
		return "%s" % (self.name)



class TradingTeams(models.Model):
	logo = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	nam =  models.CharField(max_length=64, blank=True, null=True, default=None)	
	price = models.FileField(upload_to='images/', blank = True, null = True, default = None)
	trademark = models.TextField(blank = True, null = True, default = None)
	picture = models.ForeignKey(Logotip, blank = True, null = True, default = None)

class VacancyKiev(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = models.TextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	
class VacancyNivki(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = models.TextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)

class VacancyZhitomir(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = models.TextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	
class VacancyOblast(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = models.TextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)

class VacancyBerezan(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = models.TextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	


