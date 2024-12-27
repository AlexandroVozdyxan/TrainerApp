from django.urls import path

from booking.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.trainer_page, name='trainer_page'),
    path('<int:trainer_id>/', views.specific_trainer, name='specific_trainer'),
    path('<trainer_id>/<service_id>/', views.trainer_service, name='trainer_service'),
]