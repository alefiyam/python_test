# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=500)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Answer(models.Model):
    body = models.CharField(max_length=9000)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['body']


class Tenant(models.Model):
    name = models.CharField(max_length=9000)
    api_key = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)


class Count(models.Model):
    count_per_day = models.IntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)
