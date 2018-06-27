from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *
from django.shortcuts import render, render_to_response


def main(request):
	args = {}
	args['brands'] = TradingTeams.objects.all
	return render_to_response('in_main.html', args)

def brand(request, brand_id = 1):
	args = {}
	args['brand'] = TradingTeams.objects.get(id = brand_id)
	return render_to_response('brand.html', args)

def brands(request):
	args = {}
	args['brands'] = TradingTeams.objects.all
	return render_to_response('brand_list.html', args)


def vacancy(request):
	args = {}
	args['vacancys'] = Vacancy.objects.order_by('-date')
	return render_to_response('vacancy.html', args)




