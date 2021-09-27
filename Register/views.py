from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Patient
from .forms import registroPaciente, registroTutor, registroHospital

# Create your views here.
def index(request):
    #Function Code
    Patients=Patient.objects.all()
    print(Patients)
    return render(request, 'home.html', {'Patients':Patients})

def register(request):
    #Function Code
    if request.method == 'POST':
        form = registroPaciente(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = registroPaciente()
    return render(request, 'registro.html', {'form':form})

def register_hospital(request):
    #Function Code
    if request.method == 'POST':
        form = registroHospital(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = registroHospital()
    return render(request, 'registro_hospital.html', {'form':form})

def register_tutor(request):
    #Function Code
    if request.method == 'POST':
        form = registroTutor(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = registroTutor()
    return render(request, 'registro_tutor.html', {'form':form})

def delete_pt(request, Patient_id):
    patient = Patient.objects.get(pk=Patient_id)
    patient.delete()
    return redirect('index')

