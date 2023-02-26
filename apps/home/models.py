# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tool(models.Model):
    project_name = models.CharField(max_length=100)
    repo_name = models.CharField(max_length=100, default=None)
    aff_url = models.CharField(max_length=1000, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Tools"

    def __str__(self):
        return self.project_name

