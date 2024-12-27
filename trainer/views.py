from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def trainer_page(request):
    return HttpResponse("Trainer page")

def specific_trainer(request, trainer_id):
    return HttpResponse(f"Trainer {trainer_id}")

def trainer_service(request, trainer_id, service_id):
    return HttpResponse(f"Trainer {trainer_id} {service_id}")