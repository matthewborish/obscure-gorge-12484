# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from django.contrib import admin
from .models import Tool


class ToolAdmin(admin.ModelAdmin):
    list_display = ("project_name", "project_url")

# Register your models here.
admin.site.register(Tool, ToolAdmin)
