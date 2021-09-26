from django.contrib import admin
from .models import Tutor, Hospital, Patient
# Register your models here.
admin.site.register(Tutor)
admin.site.register(Hospital)
admin.site.register(Patient)