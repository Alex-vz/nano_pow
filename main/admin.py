# coding: utf-8

from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.TaraType)
class TaraTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CollectPoint)
class CollectPointAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NanoPowder)
class NanoPowderAdmin(admin.ModelAdmin):
    fields = ('location', 
    	('tara_type', 'tara_number', 'pack_date'),
    	('prod_date', 'prod_number', 'collect_point'),
    	'label_text',
    	('poverhn', 'plotnost'),
    	'comment',
    	('brutto_mass', 'netto_mass'),
    	('mass_check_date', 'plotnost_check_date')
    	)
    list_display = ('location', 'tara_type', 'tara_number', 'brutto_mass', 'netto_mass', 'label_text')
    list_display_links = ()
    list_filter = ('location', 'tara_type', 'pack_date', 'mass_check_date', 'plotnost_check_date')



