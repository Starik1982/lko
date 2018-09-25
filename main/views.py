# -*- coding: utf-8 -*-
import json
import urllib
import urllib.request
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib import messages


def main(request):
	args = {}
	args['brands'] = TradingTeams.objects.all
	return render_to_response('in_main.html', args)

def brand(request, brand_id = 1):	
	args = {}
	args['brand'] = TradingTeams.objects.get(id = brand_id)
	tag = args['brand'].nam
	args['products'] = Product.objects.filter(tag = tag)
	
	
	return render_to_response('brand.html', args)

def brands(request):
	args = {}
	args['brands'] = TradingTeams.objects.all
	return render_to_response('brand_list.html', args)

def vacancy(request):
	
	return render_to_response('vacancy_list.html')

def vacancy_kiev(request):
	args = {}
	args['vacancys'] = VacancyKiev.objects.order_by('-date')
	return render_to_response('vacancy_kiev.html', args)

def get_vacancy_kiev(request, vacancy_id = 1):
	args = {}
	args['vacancy'] = VacancyKiev.objects.get(id = vacancy_id)
	return render_to_response('vacancy.html', args)

def vacancy_nivki(request):
	args = {}
	args['vacancys'] = VacancyNivki.objects.order_by('-date')
	return render_to_response('vacancy_nivki.html', args)

def get_vacancy_nivki(request, vacancy_id = 1):
	args = {}
	args['vacancy'] = VacancyNivki.objects.get(id = vacancy_id)
	return render_to_response('vacancy.html', args)

def vacancy_zhitomir(request):
	args = {}
	args['vacancys'] = VacancyZhitomir.objects.order_by('-date')
	return render_to_response('vacancy_zhitomir.html', args)

def get_vacancy_zhitomir(request, vacancy_id = 1):
	args = {}
	args['vacancy'] = VacancyZhitomir.objects.get(id = vacancy_id)
	return render_to_response('vacancy.html', args)

def vacancy_oblast(request):
	args = {}
	args['vacancys'] = VacancyOblast.objects.order_by('-date')
	return render_to_response('vacancy_oblast.html', args)

def get_vacancy_oblast(request, vacancy_id = 1):
	args = {}
	args['vacancy'] = VacancyOblast.objects.get(id = vacancy_id)
	return render_to_response('vacancy.html', args)

def vacancy_berezan(request):
	args = {}
	args['vacancys'] = VacancyBerezan.objects.order_by('-date')
	return render_to_response('vacancy_berezan.html', args)

def get_vacancy_berezan(request, vacancy_id = 1):
	args = {}
	args['vacancy'] = VacancyBerezan.objects.get(id = vacancy_id)
	return render_to_response('vacancy.html', args)



def contacts(request):
	args = {}	
	args.update(csrf(request))
	args['messages'] = Message.objects.order_by('-date')[:10]
	args['comments'] = Comments.objects.all
	

	return render_to_response('contacts.html',  args)

def addmessage(request):
	comments_text = ''
	none = None
	args = {}
	args.update(csrf(request))
	if request.method == 'POST':
		visitor = request.POST.get('visitor')
		text = request.POST.get('text')
		if visitor and text:
			''' Begin reCAPTCHA validation '''
			recaptcha_response = request.POST.get('g-recaptcha-response')
			url = 'https://www.google.com/recaptcha/api/siteverify'
			values = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
				}
			data = urllib.parse.urlencode(values).encode()
			req =  urllib.request.Request(url, data=data)
			response = urllib.request.urlopen(req)
			result = json.loads(response.read().decode())
			''' End reCAPTCHA validation '''
			if result['success']:
				p = Message(visitor=visitor, text=text)
				p.save()		
	else:
		return redirect('/contacts/')

	return redirect('/contacts/')

