from django import forms
from BaseDatos.models import Carrera
from BaseDatos.models import Alumno, Historial, Pagos


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
    
class AddAlumnoForm(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = '__all__'

class AddHistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = '__all__'


class viewHistorialForm(forms.Form): #sera utilizado para la busqueda de matriculas
    Matricula = forms.CharField(max_length= 10, required=True)


class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'

class PagosAdicionalesForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = ('Historial','Nombre','MontoTotal','Abono','FechaPago','FechaLimite')
