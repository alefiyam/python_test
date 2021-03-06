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
from .models import *

@csrf_exempt
@api_view(['GET'])
def get_user_id(request):
    user_content = {}
    username = request.GET.get('username', None)
    if username != u'None':
        user = User.objects.get(username=username)
        if not user:
            return Response({'user_id': None})
        user_content = {'user_id': user.id}
    return Response(user_content)

@csrf_exempt
@api_view(['GET'])
def get_que_ans(request):
    if(Count.objects.count()<=0):
        x=Count.objects.create()
        x.save()
    else:
        x=Count.objects.all()[0]
        x.count_per_day=x.count_per_day+1
        x.save()

    list_of_dict = []
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

@csrf_exempt
@api_view(['GET'])
def dashboard(request):
    content = {}
    content['questions_count'] = Question.objects.count()
    content['answer_count'] = Answer.objects.count()
    content['users_count'] = User.objects.count()
    content['visit_count'] = Count.objects.all().first().count_per_day
    return Response(content)

@csrf_exempt
@api_view(['GET'])
def get_que_by_search_term(request):
    search_term = request.GET.get('search_term', None)
    if search_term:
        questions_list = []
        questions = Question.objects.filter(
            title__contains = search_term).values_list(
            'title', flat=True)
        if questions:
            for que in questions:
                questions_list.append(que)
            questions_list = json.dumps(questions_list)
            content = { 'question_list': questions_list }
            return Response(content)
        else:
            content = {'no_questions': "No Question Found"}
            return Response(content)
    else:
        content = {"empty_search": "Enter Search term in URL"}
        return Response(content)