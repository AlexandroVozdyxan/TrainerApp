from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def booking_page(request):
    return HttpResponse("Booking Page")

def specific_booking(request, booking_id):
    return HttpResponse(f"Specific Booking {booking_id}")

def accept_booking(request, booking_id):
    return HttpResponse(f"Accept Booking {booking_id}")

def cancel_booking(request, booking_id):
    return HttpResponse(f"Cancel Booking {booking_id}")