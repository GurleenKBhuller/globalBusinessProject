from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="index"),
    path('pestle/', pestle_view, name='pestle_view'),
    path('hofsted/', hofsted_view, name='hofsted_view'),
    path('competitiveness/', competitive_view, name="competitive_view")
]