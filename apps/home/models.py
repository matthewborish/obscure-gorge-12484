# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tool(models.Model):
    project_name = models.CharField(max_length=100)
    project_url = models.CharField(max_length=1000, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tools"

    def __str__(self):
        return self.project_name



