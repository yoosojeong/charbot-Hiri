# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# models에서 BlogData를 import 해옵니다.
from . import models
# 아래의 코드를 입력하면 BlogData를 admin 페이지에서 관리할 수 있습니다.
# admin.site.register(TodayCafeteriaData)

@admin.register(models.TodayCafeteriaData)
class TodayCafeteriaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'todayMenu',
        'created_at',
    )

@admin.register(models.YesdayCafeteriaData)
class YesdayCafeteriaAdmin(admin.ModelAdmin):

    list_display = (
        'yesdayMenu',
        'created_at',
    )

@admin.register(models.SeqCafeteriaData)
class SeqCafeteriaAdmin(admin.ModelAdmin):

    list_display = (
        'seqMenu',
        'created_at',
    )

@admin.register(models.WeatherData)
class WeatherAdmin(admin.ModelAdmin):

    list_display = (
        'statData',
        'dumpData',
        'pm10',
        'pm25',
        'o3',
        'created_at',
    )
