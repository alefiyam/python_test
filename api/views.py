# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
import json
import os
import time
from datetime import datetime
import user

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Question , Answer
# from rest_framework.decorators import permission_classes
# from oauth2_provider.decorators import rw_protected_resource
# from oauth2_provider.decorators import protected_resource
# from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

@csrf_exempt
@api_view(['GET'])
def get_user_id(request):
    username = str(request.GET['username'])
    user = User.objects.filter(username=username)
    user_id = user[0].id
    user_content = {'user_id': user_id}
    return Response(user_content)

@csrf_exempt
@api_view(['GET'])
def get_que_ans(request):
    list_of_dict = []
    # username = str(request.GET.get('username'), None)
    user_id = str(request.GET['user_id'])
    questions = Question.objects.filter(private=False)
    for question in questions:
        ques_dict_ans = {}
        ques_dict_ans['answer'] = list()
        ques_dict_ans['question_title'] = question.title
        ques_dict_ans['user_id'] = question.user_id
        answers = question.answer_set.values().exclude(user_id = user_id)
        for answer in answers:
            answers_dict = {}
            answers_dict['body'] = answer['body']
            answers_dict['user_id'] = answer['user_id']
            ques_dict_ans['answer'].append(answers_dict)
        list_of_dict.append(ques_dict_ans.copy())
    print(list_of_dict)
    content = {'ques_ans_set': list_of_dict}
    return Response(content)
