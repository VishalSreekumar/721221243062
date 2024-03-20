from home.views import calculator

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('numbers/e',calculator),
]
