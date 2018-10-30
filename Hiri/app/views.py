import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.core.serializers import serialize

class Keyboard(APIView):
    
    def get(self, request):
        
        
        return JsonResponse(
            {
            'type': 'buttons',
            'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
        }
    )

class Message(APIView):

    def post(self, request):

        json_str = (request.body).decode('utf-8')
        received_json = json.loads(json_str)
        content_name = received_json['content']
        
        #공지사항 - 학생회
        if content_name == "공지사항":
            
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )
            

        #급식
        elif content_name == "급식표":
    
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
            
            today = models.TodayCafeteriaData.objects.all().last()

            return JsonResponse(
                {
                    'message': {
                        'text': today.todayMenu
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        elif content_name == "내일급식":
            
            yesday = models.YesdayCafeteriaData.objects.all().last()

            return JsonResponse(
                {
                    'message': {
                        'text': yesday.yesdayMenu
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        #급식순서
        elif content_name == "급식순서":
            
            seq = models.SeqCafeteriaData.objects.all().last()
            #seq.seqMenu

            return JsonResponse(
                {
                    'message': {
                        'text': "게임 -> 유센 -> 해킹"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        #날씨
        elif content_name == "날씨":
            # "서울특별시(현재)\n\n" +"•기온\n" + models.SeqCafeteriaData.objects.get()+ "\n\n•대기상태\n" + air

            return JsonResponse(
                {       
                    'message': {
                        'text':  content_name + "를 눌렀습니다."
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["기온", "미세먼지"]
                    }
                }
            )

        elif content_name == "기온":

            weather = models.WeatherData.objects.all().last()

            return JsonResponse(
                {       
                    'message': {
                        'text':  "서울특별시(현재) - 기온 \n\n" + weather.statData + " / " + weather.dumpData + "℃"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        elif content_name == "미세먼지":

            weather = models.WeatherData.objects.all().last()

            return JsonResponse(
                {       
                    'message': {
                        'text':  "서울특별시(현재) - 미세먼지 \n\n" + "오존농도: " + weather.pm10 + "\n미세먼지: " + weather.pm25 + "\n초 미세먼지: " + weather.o3
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
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
                        'buttons': ["1학년", "2학년", "3학년"]
                    }
                }
            )

        elif content_name == "1학년":
            return JsonResponse(
                {
                    'message': {
                        'text': content_name + "를 눌렀습니다."
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["해킹 1반", "해킹 2반", "유센 1반", "유센 2반", "게임"]
                    }
                }
            )

        elif content_name == "2학년":
            return JsonResponse(
                {
                    'message': {
                        'text': content_name + "를 눌렀습니다."
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["해킹 1반", "해킹 2반", "유센 1반", "유센 2반", "게임"]
                    }
                }
            )

        elif content_name == "3학년":
            return JsonResponse(
                {
                    'message': {
                        'text': content_name + "를 눌렀습니다."
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["해킹 1반", "해킹 2반", "유센 1반", "유센 2반", "게임"]
                    }
                }
            )

        elif content_name == "해킹 1반":
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        elif content_name == "해킹 2반":
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        elif content_name == "유센 1반":
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        elif content_name == "유센 2반":
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        elif content_name == "게임":
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        #학사일정 - 학생회
        elif content_name == "학사일정":
            
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        #학교소개 - 학생회
        elif content_name == "학교소개":
            
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        #건의사항 - 학생회
        elif content_name == "건의사항":
            
            return JsonResponse(
                {
                    'message': {
                        'text': "준비중"
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        #개발자소개
        elif content_name == "개발자 소개":
            
            return JsonResponse(
                {
                    'message': {
                        'text': "해킹보안과 2학년 1반 유소정입니다."
                    },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                    }
                }
            )

        #exception
        else:
            return JsonResponse(
            {
                'message': {
                    'text': "잘못 입력하셨거나, 개발 중인 기능입니다."
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ["공지사항", "급식표", "급식순서", "날씨", "시간표", "학사일정", "학교소개", "건의사항", "개발자 소개"]
                }   
            }
        )
