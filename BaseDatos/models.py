from django.db import models

# Create your models here.
class Alumno(models.Model):
    Matricula = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=50)
    ApellidoPater = models.CharField( max_length=20)
    ApellidoMater = models.CharField(max_length=20)
    Correo = models.EmailField( max_length=254)
    Telefono = models.CharField(max_length=10)
    TipoPeriodo = models.CharField(max_length=15)
    

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return self.Matricula


class Carrera(models.Model):
    Nombre = models.CharField(max_length=50)
    Cuatrimestral = models.BooleanField()
    NumCuatrimestres = models.IntegerField()
    Semestral = models.BooleanField()
    NumSemestres = models.IntegerField()
    

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return self.Nombre


class Historial(models.Model):
    Alumno = models.ForeignKey(Alumno,  on_delete=models.CASCADE)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    PeriodoAct = models.IntegerField()
    Grupo = models.CharField(max_length=1)
    FechaInicio = models.DateField(auto_now=False, auto_now_add=False)
    FechaFinal = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Regristo Academico"
        verbose_name_plural = "Historial"

    def __str__(self):
        return str(self.Alumno)


class Pagos(models.Model):
    Historial = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    MontoTotal = models.IntegerField(default = 0)
    Abono = models.IntegerField(default = 0)
    Resto = models.IntegerField(default = 0)
    FechaPago = models.DateField(auto_now=False, auto_now_add=False)
    FechaLimite = models.DateField( auto_now=False, auto_now_add=False)
    Beca = models.CharField(max_length=50, default = 0)
    Cargo = models.IntegerField(default = 0)
    liquidado = models.BooleanField(default = False)
    
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Pagos'
        verbose_name_plural = 'Historial de Pagos'






