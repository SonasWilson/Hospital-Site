from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Department,Doctor
from . forms import BookingForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request,'confirmation.html')
    else:
        form = BookingForm()

    return render(request,'booking.html', {'form':form})

def doctors(request):
    doc_detail = {
        'doctors':Doctor.objects.all()
    }
    return render(request,'doctors.html',doc_detail)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dept_detail = {
        'dept': Department.objects.all()
    }
    return render(request,'department.html', dept_detail)