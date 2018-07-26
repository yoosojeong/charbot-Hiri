from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from . import models

class Keyboard(APIView):
    
    def get(self, request):
        return JsonResponse(
            {
            "type": "buttons",
            "buttons": ["급식표","급식순서", "날씨"] #급식표, 급식순서, 날씨, 롤전적
        }
    )

class Message(APIView):

    def post(self, request):

        json_str = (request.body).decode('utf-8')
        received_json = json.loads(json_str)
        content_name = received_json['content']
        
        #급식 
        if content_name == "급식표":
    
            return JsonResponse(
                {
                    'message': {
                        'text': content_name + "를 눌렀습니다."
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["오늘급식", "내일급식"]
                    }
                }
            )
    
        elif content_name == "오늘급식":
            return JsonResponse(
                {
                    'message': {
                        'text': models.TodayCafeteriaData.objects.get()
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["급식표", "급식순서", "날씨"]
                    }
                }
            )

        elif content_name == "내일급식":
            return JsonResponse(
                {
                    'message': {
                        'text': models.YesdayCafeteriaData.objects.get()
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["급식표", "급식순서", "날씨"]
                    }
                }
            )

        #급식순서
        elif content_name == "급식순서":
            return JsonResponse(
                {
                    'message': {
                        'text': models.SeqCafeteriaData.objects.get()
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["급식표", "급식순서", "날씨"]
                    }
                }
            )

        #날씨
        elif content_name == "날씨":
            # "서울특별시(현재)\n\n" +"•기온\n" + models.SeqCafeteriaData.objects.get()+ "\n\n•대기상태\n" + air

            return JsonResponse(
                {       
                    'message': {
                        'text': models.SeqCafeteriaData.objects.get()
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["급식표", "급식순서", "날씨"]
                    }
                }
            )

        #시간표
        elif content_name == "시간표":
            return JsonResponse(
                {
                    'message': {
                        'text': content_name + "를 눌렀습니다."
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['월', '화', '수', '목', '금']
                    }
                }
            )

        #exception
        else:
            return JsonResponse(
            {
                'message': {
                    'text': "잘못 입력하셨거나, 개발 중인 기능입니다."
                }
            }
        )
