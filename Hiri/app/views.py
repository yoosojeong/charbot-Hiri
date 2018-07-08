# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse

class Keyboard(APIView):
    def get(self, request):
        return JsonResponse(
            {
            "type": "buttons",
            "buttons": ["급식", "날씨", "테스트"]
        }
    )
