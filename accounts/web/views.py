# accounts/web/views.py
from django.http import HttpResponse

def sample_view(request):
    return HttpResponse("Sample view working!")
