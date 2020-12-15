# -*- coding: utf-8 -*-

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SynthTest

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('test/', SynthTest.as_view(), name='test'),
]
