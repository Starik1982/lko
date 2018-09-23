# -*- coding: utf-8 -*-
from django.db import models
from .models import *
from ckeditor.fields import RichTextField



class Product(models.Model):
	tag = models.CharField(max_length=64, blank=True, null=True, default=None)
	name = models.CharField(max_length=200, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	description = models.TextField(blank = True, null = True, default = None)
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

		
class TradingTeams(models.Model):
	logo = models.ImageField(upload_to='images/', blank = True, null = True, default = None)
	nam =  models.CharField(max_length=64, blank=True, null=True, default=None)	
	trademark = models.TextField(blank = True, null = True, default = None)
	price = models.FileField(upload_to='images/', blank = True, null = True, default = None)
	class Meta:
		verbose_name = 'Бренд'
		verbose_name_plural = 'Бренды'


class VacancyKiev(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = RichTextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	class Meta:
		verbose_name = 'Вакансию'
		verbose_name_plural = 'Вакансии Выдубычи'
	
class VacancyNivki(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = RichTextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	class Meta:
		verbose_name = 'Вакансию'
		verbose_name_plural = 'Вакансии Нивки'

class VacancyZhitomir(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = RichTextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	class Meta:
		verbose_name = 'Вакансию'
		verbose_name_plural = 'Вакансии Житомир'
	
class VacancyOblast(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = RichTextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	class Meta:
		verbose_name = 'Вакансию'
		verbose_name_plural = 'Вакансии Петровцы'

class VacancyBerezan(models.Model):
	name_vacancy = models.CharField(max_length=300, blank=True, null=True, default=None)
	text = RichTextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	class Meta:
		verbose_name = 'Вакансию'
		verbose_name_plural = 'Вакансии Березань'

class Message(models.Model):
	visitor = models.CharField(max_length=100, blank=True, null=True, default=None)
	text = models.TextField(blank = True, null = True, default = None, verbose_name="текст повідомлення")
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	def __str__(self):
		return "%s" % (self.visitor)
	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'


class Comments(models.Model):
	commentator = models.CharField(max_length=100, blank=True, null=True, default=None)
	comments_text = models.TextField(blank = True, null = True, default = None)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	comments_message = models.ForeignKey(Message)
	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы на Сообщения'

	


