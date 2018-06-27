from django.db import models
from .models import *

class Worker(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True, default=None)
	surname = models.CharField(max_length=100, blank=True, null=True, default=None)
	position = models.TextField( blank = True, null = True, default = None)
	contacts = models.CharField(max_length=200, blank=True, null=True, default=None)

	def __str__(self):
		return "%s, %s" % (self.name, self.surname)
	


class TradingTeams(models.Model):
	logo = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	nam =  models.CharField(max_length=64, blank=True, null=True, default=None)
	team_leader = models.ForeignKey(Worker, related_name='team_leader', blank = True, null = True, default = None)
	worker_1 = models.ForeignKey(Worker, related_name='worker_1', blank = True, null = True, default = None)
	worker_2 = models.ForeignKey(Worker, related_name='worker_2',blank = True, null = True, default = None)
	worker_3 = models.ForeignKey(Worker, related_name='worker_3', blank = True, null = True, default = None)
	price = models.FileField(upload_to='images/', blank = True, null = True, default = None)
	trademark = models.TextField(blank = True, null = True, default = None)



class Vacancy(models.Model):
	structural_unit = models.CharField(max_length=300, blank=True, null=True, default=None)
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = models.TextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	
