from django.contrib import admin
from .models import Alumno, Carrera, Historial, Pagos
# Register your models here.

admin.site.register(Alumno)
admin.site.register(Carrera)
admin.site.register(Historial)
admin.site.register(Pagos)