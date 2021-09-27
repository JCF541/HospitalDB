from django.db import models
from django import forms

class Tutor(models.Model):
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=254, null =False)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=254)
    loc_state = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Patient(models.Model):
    f_name = models.CharField(max_length=254)
    l_name = models.CharField(max_length=254)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1)
    dob = models.DateField(null=True)
    in_date = models.DateField(auto_now_add=True, null=True)
    #Foreign Keys (Composition of attributes as Hospital and Tutor classes)
    h_origin = models.ForeignKey(Hospital, on_delete=models.CASCADE, null= True, blank=True)
    t_info = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.f_name + " " + self.l_name