from django.conf.urls import url, include
from main import views



urlpatterns = [
    url(r'^$', views.main, name ='main'),
    url(r'^brands/$', views.brands, name ='brands'),
    url(r'^brand/(?P<brand_id>\d+)/$', views.brand, name ='brand'),
    url(r'^vacancy/$', views.vacancy, name ='vacancy'),
    url(r'^vacancy_kiev/$', views.vacancy_kiev, name ='vacancy_kiev'),    
    url(r'^vacancy_kiev/(?P<vacancy_id>\d+)/$', views.get_vacancy_kiev, name ='get_vacancy_kiev'),
    url(r'^vacancy_nivki/$', views.vacancy_nivki, name ='vacancy_nivki'),
    url(r'^vacancy_nivki/(?P<vacancy_id>\d+)/$', views.get_vacancy_nivki, name ='get_vacancy_nivki'),
    url(r'^vacancy_zhitomir/$', views.vacancy_zhitomir, name ='vacancy_zhitomir'),
    url(r'^vacancy_zhitomir/(?P<vacancy_id>\d+)/$', views.get_vacancy_zhitomir, name ='get_vacancy_zhitomir'),
    url(r'^vacancy_oblast/$', views.vacancy_oblast, name ='vacancy_oblast'),
    url(r'^vacancy_oblast/(?P<vacancy_id>\d+)/$', views.get_vacancy_oblast, name ='get_vacancy_oblast'),
    url(r'^vacancy_berezan/$', views.vacancy_berezan, name ='vacancy_berezan'),
    url(r'^vacancy_berezan/(?P<vacancy_id>\d+)/$', views.get_vacancy_berezan, name ='get_vacancy_berezan'),

] 