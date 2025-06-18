from django.urls import *
from dashboard.views import dashboard


urlpatterns = [
    path('', dashboard, name='dashboard'),
]