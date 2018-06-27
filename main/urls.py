from django.conf.urls import url, include
from main import views



urlpatterns = [
    url(r'^$', views.main, name ='main'),
    url(r'^brands/$', views.brands, name ='brands'),
    url(r'^brand/(?P<brand_id>\d+)/$', views.brand, name ='brand'),
    url(r'^vacancy/$', views.vacancy, name ='vacancy'),

] 