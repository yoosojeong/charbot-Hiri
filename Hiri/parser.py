#!/mnt/d/sjyoo/Study/KakaoBot/Hiri/kakaenv/lib/python3.6

import json 
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
from urllib.parse import quote
import urllib.request
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hiri.settings")
import django
django.setup()

from app.models import * 

def cafeteriaList():

    m = datetime.today().month
    d = datetime.today().day

    li = []

    url = "https://stu.sen.go.kr/sts_sci_md00_001.do"
    data = {"ay":2018,                 
            "mm":"0"+str(m),                 
            "schulCode":"B100000662",   
            "schulKndScCode":"04",      
            "schulCrseScCode":"4"}      
    eduOfficeUrl = "https://stu.sen.go.kr/edusys.jsp?page=sts_m40000&returnDomain=B10"
    referer = {"referer":eduOfficeUrl} 
    session = requests.Session()
    html = session.post(url, data=data, headers=referer)
    soup = BeautifulSoup(html.text, "html.parser")

    school = soup.select(
        "td > div"
        )

    for cafeteriaList in school:
        
        cout = ""
        cafeteria = cafeteriaList.text.split("*")
        
        for count in range(len(cafeteria)):
            cout += cafeteria[count].split(".")[-1] + "\n"

        if len(cout) > 4:
            cout = cout.replace("[", "일 - ")
            cout = cout.replace("]", "\n")

            li.append(cout[:-2])

        else:
            li.append("급식이 없습니다.")


    data = [li[d-1], li[d]]

    return data

def cafeteriaSeq():

    dic_class = {0: '해킹', 1: '유센', 2: '게임'}
    week_number = date.today().isocalendar()[1] # 몇 주차

    seq = dic_class[week_number % len(dic_class.keys())]
    if seq == "해킹":
        return seq # 몇 주 % 반 갯수

    elif seq == "유센":
        return seq

    elif seq == "게임":
        return seq

def weatherList():

    data = {}

    api_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    api_key = '&APPID=df00ece630ea6c71cd69f538567edc2e'

    url = urllib.request.urlopen(api_url + 'Seoul' + api_key)
    apid = url.read()
    data = json.loads(apid)

    cityname= data['name']
    weather = data['weather'][0]['main']
    temp = int(data['main']['temp'] - 273.15)

    weatherKinds = {'thunderstorm with light rain': '가벼운 비를 동반한 천둥구름 (우산)',
    'thunderstorm with rain': '비를 동반한 천둥구름 (우산)',
    'thunderstorm with heavy rain':	'폭우를 동반한 천둥구름 (우산)',
    'light thunderstorm': '약한 천둥구름',
    'thunderstorm':	'천둥구름',
    'heavy thunderstorm': '강한 천둥구름',
    'ragged thunderstorm': '불규칙적 천둥구름',
    'thunderstorm with light drizzle': '약한 연무를 동반한 천둥구름',
    'thunderstorm with drizzle': '연무를 동반한 천둥구름',
    'thunderstorm with heavy drizzle': '강한 안개비를 동반한 천둥구름 (우산)',
    'light intensity drizzle': '가벼운 안개비 (우산)',
    'drizzle': '안개비 (우산)',
    'heavy intensity drizzle': '강한 안개비 (우산)',
    'light intensity drizzle rain': '가벼운 적은 비 (우산)',
    'drizzle rain': '적은비 (우산)',
    'heavy intensity drizzle rain': '강한 적은비 (우산)',
    'shower rain and drizzle': '소나기와 안개비 (우산)',
    'heavy shower rain and drizzle': '강한 소나기와 안개비 (우산)',
    'shower drizzle': '소나기 (우산)',
    'light rain': '약한 비 (우산)',
    'moderate rain': '중간 비 (우산)',
    'heavy intensity rain': '강한 비 (우산)',
    'very heavy rain': '매우 강한 비 (우산)',
    'extreme rain': '극심한 비 (우산)',
    'freezing rain': '우박',
    'light intensity shower rain': '약한 소나기 비 (우산)',
    'shower rain': '소나기 비 (우산)',
    'heavy intensity shower rain': '강한 소나기 비 (우산)',
    'ragged shower rain': '불규칙적 소나기 비 (우산)',
    'light snow': '가벼운 눈',
    'snow': '눈',
    'heavy snow': '강한 눈',
    'sleet': '진눈깨비',
    'shower sleet': '소나기 진눈깨비',
    'light rain and snow': '약한 비와 눈',
    'rain and snow': '비와 눈',
    'light shower snow': '약한 소나기 눈',
    'shower snow': '소나기 눈',
    'heavy shower snow': '강한 소나기 눈 (우산)',
    'mist': '엷게 낀 안개',
    'smoke': '연기',
    'haze': '맑음',
    'Clear': '맑음',
    'sand, dust whirls': '모래 먼지',
    'fog': '안개',
    'sand': '모래',
    'dust': '먼지',
    'volcanic ash': '화산재',
    'squalls': '돌풍',
    'tornado': '토네이도',
    'Clouds': '구름 조금',
    'clear sky': '구름 한 점 없는 맑은 하늘',
    'few clouds': '약간의 구름이 낀 하늘',
    'scattered clouds': '드문드문 구름이 낀 하늘',
    'broken clouds': '구름이 거의 없는 하늘',
    'overcast clouds': '구름으로 뒤덮인 흐린 하늘',
    'tornado': '토네이도',
    'tropical storm': '태풍',
    'hurricane': '허리케인',
    'cold': '한랭',
    'hot': '고온',
    'windy': '바람부는',
    'hail': '우박',
    'calm': '바람이 거의 없는',
    'light breeze': '약한 바람',
    'gentle breeze': '부드러운 바람',
    'moderate breeze': '중간 세기 바람',
    'fresh breeze': '신선한 바람',
    'strong breeze': '센 바람',
    'high win': '돌풍에 가까운 센 바람',
    'gale': '돌풍',
    'severe gale': '심각한 돌풍',
    'storm': '폭풍',
    'violent storm': '강한 폭풍',
    'hurricane': '허리케인'}
    
    for i in weatherKinds:
        if weather.upper() == i.upper():
            weather = weatherKinds[i]

    data = [weather, temp]

    return data

def air_status():
    
    data = {}

    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=UO%2Ff1JIdATORyBZlMoob7p9jA%2F8qPAuEPC%2BLahj%2FcG%2BvOTVAw%2FQ5bs1CstZmYU0cpLYNG75IKVMrI%2FM3u1V8yQ%3D%3D&numOfRows=999&pageSize=999&pageNo=1&startPage=1&ver=1.3&sidoName='
    cityName=quote("서울")
    page = urllib.request.urlopen(url+cityName)
    text = page.read().decode('utf8')
    soup = BeautifulSoup(text, 'html.parser')
    
    error_checker = text.find('마포구')

    if error_checker != -1:
        items = soup.find_all('item')
        items = list(items)
        index = 0
        for s in items:
            s = str(s)
            if s.find('마포구') != -1:
                index = index
                break
            else:
                index = index + 1

        if len(items) != index:
            need_parsing = str(items[index])
            start_so2value = need_parsing.find('<so2value>')
            end_so2value = need_parsing.find('</so2value>')
            so2value = need_parsing[start_so2value + len('<so2value>') : end_so2value]
            start_covalue = need_parsing.find('<covalue>')
            end_covalue = need_parsing.find('</covalue>')
            covalue = need_parsing[start_covalue + len('<covalue>') : end_covalue]
            start_o3value = need_parsing.find('<o3value>')
            end_o3value = need_parsing.find('</o3value>')
            o3value = need_parsing[start_o3value + len('<o3value>') : end_o3value]
            start_no2value = need_parsing.find('<no2value>')
            end_no2value = need_parsing.find('</no2value>')
            no2value = need_parsing[start_no2value + len('<no2value>') : end_no2value]
            start_pm10value = need_parsing.find('<pm10value>')
            end_pm10value = need_parsing.find('</pm10value>')
            pm10value = need_parsing[start_pm10value + len('<pm10value>') : end_pm10value]
            start_pm25value = need_parsing.find('<pm25value>')
            end_pm25value = need_parsing.find('</pm25value>')
            pm25value = need_parsing[start_pm25value + len('<pm25value>') : end_pm25value]

            check = [o3value, pm10value, pm25value]

            #print(o3value) #오존농도
            #print(pm10value) #미세먼지
            #print(pm25value) #초 미세먼지

            for c in check:
                if c != "-":
                    
                    pm10valu = float(pm10value)
                    pm25valu = float(pm25value)
                    o3valu = float(o3value)
                    
                    pm10 = ''
                    pm25 = ''
                    o3 = ''

                    if pm10valu > 75 :
                        pm10 = '매우나쁨'
                    elif pm10valu > 35:
                        pm10 = '나쁨'
                    elif pm10valu > 15:
                        pm10 = '보통'
                    else :
                        pm10 = '좋음'

                    if pm25valu > 75 :
                        pm25 = '매우나쁨'
                    elif pm25valu > 35:
                        pm25 = '나쁨'
                    elif pm25valu > 15:
                        pm25 = '보통'
                    else :
                        pm25 = '좋음'

                    if o3valu > 0.15 :
                        o3 = '매우나쁨'
                    elif o3valu > 0.09:
                        o3 = '나쁨'
                    elif o3valu > 0.03:
                        o3 = '보통'
                    else :
                        o3 = '좋음'

                    data = [pm10, pm25, o3]

                else:
                    data = ["분석중", "분석중", "분석중"]

            return data

if __name__=='__main__':

    cafeters = cafeteriaList()
    cafeterseq = cafeteriaSeq()
    weather = weatherList()
    air = air_status()

    TodayCafeteriaData(todayMenu=cafeters[0]).save()
    YesdayCafeteriaData(yesdayMenu=cafeters[1]).save()

    SeqCafeteriaData(seqMenu=cafeterseq).save()
    
    WeatherData(statData=weather[0], dumpData=weather[1], pm10=air[0], pm25=air[1], o3=air[2]).save()