from django.contrib import admin
from .models import *

class WorkerAdmin(admin.TabularInline):
    model = Worker
    extra = 0

class WorkerAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in Worker._meta.fields]

    class Meta:
        model = Worker
admin.site.register(Worker, WorkerAdmin)


class TradingTeamsAdmin(admin.TabularInline):
    model = TradingTeams
    extra = 0

class TradingTeamsAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in TradingTeams._meta.fields]

    class Meta:
        model = TradingTeams
admin.site.register(TradingTeams, TradingTeamsAdmin)


class VacancyAdmin(admin.TabularInline):
    model = Vacancy
    extra = 0

class VacancyAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in Vacancy._meta.fields]

    class Meta:
        model = Vacancy
admin.site.register(Vacancy, VacancyAdmin)