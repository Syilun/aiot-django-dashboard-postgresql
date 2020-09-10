# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import PERSON
from .models import FACE


# Register your models here.
admin.site.register(PERSON)
admin.site.register(FACE)
