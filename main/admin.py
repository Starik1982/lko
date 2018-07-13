from django.contrib import admin
from .models import *



class TradingTeamsAdmin(admin.TabularInline):
    model = TradingTeams
    extra = 0

class TradingTeamsAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in TradingTeams._meta.fields]

    class Meta:
        model = TradingTeams
admin.site.register(TradingTeams, TradingTeamsAdmin)




class VacancyKievAdmin(admin.TabularInline):
    model = VacancyKiev
    extra = 0

class VacancyKievAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in VacancyKiev._meta.fields]

    class Meta:
        model = VacancyKiev
admin.site.register(VacancyKiev, VacancyKievAdmin)



class VacancyNivkiAdmin(admin.TabularInline):
    model = VacancyNivki
    extra = 0

class VacancyNivkiAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in VacancyNivki._meta.fields]

    class Meta:
        model = VacancyNivki
admin.site.register(VacancyNivki, VacancyNivkiAdmin)



class VacancyZhitomirAdmin(admin.TabularInline):
    model = VacancyZhitomir
    extra = 0

class VacancyZhitomirAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in VacancyZhitomir._meta.fields]

    class Meta:
        model = VacancyZhitomir
admin.site.register(VacancyZhitomir, VacancyZhitomirAdmin)



class VacancyOblastAdmin(admin.TabularInline):
    model = VacancyOblast
    extra = 0

class VacancyOblastAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in VacancyOblast._meta.fields]

    class Meta:
        model = VacancyOblast
admin.site.register(VacancyOblast, VacancyOblastAdmin)



class VacancyBerezanAdmin(admin.TabularInline):
    model = VacancyBerezan
    extra = 0

class VacancyBerezanAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in VacancyBerezan._meta.fields]

    class Meta:
        model = VacancyBerezan
admin.site.register(VacancyBerezan, VacancyBerezanAdmin)

class ProductAdmin(admin.TabularInline):
    model = Product
    extra = 0

class ProductAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in Product._meta.fields]

    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
