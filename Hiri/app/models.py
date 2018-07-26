from django.db import models

#오늘 급식 / 내일 급식 / 급식순서 / 기온 / 미세먼지
"""
    cafeteriaList(급식표)
    : [오늘급식,내일급식]

    cafeteriaSeq(급식순서)
    : 해당과

    weatherList(날씨)
    : [날씨, 기온]

    air_status(대기)
    : [미세먼지, 초미세먼지, 오존]

"""
class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class TodayCafeteriaData(TimeStampedModel):

    """ TodayCafeteria Model """

    todayMenu = models.CharField(max_length=200)

class YesdayCafeteriaData(TimeStampedModel):
    
    """ YesdayCafeteria Model """

    yesdayMenu = models.CharField(max_length=200)

class SeqCafeteriaData(TimeStampedModel):

    """ SeqCafeteria Model """

    seqMenu = models.CharField(max_length=200)

class WeatherData(TimeStampedModel):

    """ WeatherCafeteria Model """

    statData = models.CharField(max_length=100)
    dumpData = models.CharField(max_length=100)
    
    pm10 = models.CharField(max_length=100)
    pm25 = models.CharField(max_length=100)
    o3 = models.CharField(max_length=100)
