from django import forms
from django.forms.widgets import DateInput, SelectDateWidget
from .models import Hospital, Tutor, Patient

HOSP_CHOICES= [
    ('hosp1', 'Hosp1'),
    ('hosp2', 'Hosp2'),
    ('hosp3', 'Hosp3'),
    ]
STATE_CHOICES= [
    ('campeche', 'Campeche'),
    ('quintana roo', 'Quintana Roo'),
    ('yucatan', 'Yucatan'),
    ]
GENDER_CHOICES= [
    ('m', 'M'),
    ('f', 'F'),
    ('x', 'X'),
    ]

def tutor_choices():
    result = []
    for tutor in Tutor.objects.all():
        result.append((tutor.id, tutor.name))
    return result

def hospital_choices():
    result = []
    for hospital in Hospital.objects.all():
        result.append((hospital.id, hospital.name))
    return result       


class registroHospital(forms.Form):
    name = forms.CharField(label = 'Primer nombre', max_length=100)
    loc_state = forms.CharField(label= 'Estado', widget=forms.Select(choices=STATE_CHOICES))


class registroTutor(forms.Form):
    f_name = forms.CharField(label = 'Primer nombre', max_length=100)
    phone = forms.CharField(label = 'Telefono', max_length=10)

class registroPaciente(forms.Form):
    f_name = forms.CharField(label = 'Primer nombre', max_length=100)
    l_name = forms.CharField(label = 'Segundo nombre', max_length=100)
    gender = forms.CharField(label = 'Genero', widget=forms.Select(choices=GENDER_CHOICES))
    dob = forms.DateField(label = 'Fecha Nacimiento', widget=SelectDateWidget)
    in_date = forms.DateField(label = 'Fecha Registro', widget=SelectDateWidget)
    age = forms.IntegerField(label = 'Edad')
    #Foreign Keys
    
    #h_origin = forms.CharField(label= 'Hospital de origen', widget=forms.Select(choices=hospital_choices))
    #tut_info = forms.CharField(label= 'Tutor', widget=forms.Select(choices=tutor_choices))
