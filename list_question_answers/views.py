# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
import requests
import urllib2
import base64
import urllib
import json
import re
from django.shortcuts import render
from django.contrib import auth
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.http import Http404,JsonResponse
from oauth2_provider.models import AccessToken
from django.http import JsonResponse
import time
from api.models import *

# Create your views here.
# function for call login page
def get_que_ans(request):
    payload = {}
    user_token = settings.ACCESS_TOKEN
    if user_token:
        try:
            url = settings.API_BASE + "get_que_ans/"
            username = str(request.GET.get('username', None))

            response = requests.get(settings.API_BASE + "get_user_id/", headers={'Authorization': 'Bearer {}'.format(user_token)} , params = {'username': username})
            content =  response.json()
            user_id = content['user_id']
            payload['user_id'] = user_id
            response = requests.get(url, headers={'Authorization': 'Bearer {}'.format(user_token)}, params = payload)
            content =  response.json()
            return render(request, 'list_question_answers/index.html', {'content': content['ques_ans_set']})
        except:
            content = {}
            content['questions_count'] = Question.objects.count()
            content['answer_count'] = Answer.objects.count()
            content['users_count'] = User.objects.count()
            content['visit_count'] = Count.objects.all().first().count_per_day
            return render(request, 'list_question_answers/index.html', {'content': content})
    else:
        content = "Please Provide Valid Credentials"
        return render(request, 'list_question_answers/index.html', {'content': content})
            
