from django.shortcuts import render,redirect
from django.contrib.auth import logout as do_logout
from BaseDatos.models import Alumno, Carrera, Historial, Pagos
from .forms import CarreraForm, AddAlumnoForm, AddHistorialForm, viewHistorialForm, PagosForm, PagosAdicionalesForm

#####
from django.views.generic import View
#html2pdf imports
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders



####
# Create your views here.
def autenticacion(request):
   # Si estamos identificados devolvemos la portada
   
    if request.user.is_authenticated:
        Alumnos = Alumno.objects.all()
        for alumnado in Alumnos:
            historiales = Historial.objects.filter(Alumno = alumnado.pk)
            print(historiales)
        Contexto = {
            'Alumnos':Alumnos,
            'Historial':historiales,
            
        }
        
        return render(request, "usuarios/alumnos.html", Contexto)
    # En otro caso redireccionamos al login
    return redirect('/')

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
    
def AddAlumno(request):#formulario para añandir alumnos
    if request.user.is_authenticated:
        if request.method == 'POST':#Se comprueba si el fomulario envia inf por el metod post
            form = AddAlumnoForm(request.POST)#Se crea un objeto mas lo que se obtuno con el post
            if form.is_valid():#Se comprueba si el fomuario es valio
                form.save()#Se guarda la informacicion
                Matricula = form['Matricula']#Se obtiene la parte del form perteneciente a matricual
                Matricula = Matricula.value()#se obtiene le valor de la matricula
                print(Matricula)
                return redirect('addHistorial',Matricula)
        else:
            form = AddAlumnoForm()#se crea un formulario separado   
            return render(request, "usuarios/addAlumno.html", {'form':form})
    return redirect('/')

def editAlumnos(request, pk):#Edicion de alumnos, se pide la llave primaria 
    alumno = Alumno.objects.get(pk = pk) # se obtiene el valor de pk y se le asigna a otra varible del mismo nombre
    if request.method == 'GET':
        form = AddAlumnoForm(instance = alumno)
    else:
        form = AddAlumnoForm(request.POST, instance = alumno) # se toma el fomulario con las modificaciones
        if form.is_valid():#se verifica si es valido 
            form.save()#se guarde el formulario
            return redirect('autenticacion')#se redirecciona una ves guardado el formulario
    return render (request, "usuarios/addAlumno.html", {'form':form}) # se envian datos al template

def VisualizarCarreras(request):
    if request.user.is_authenticated:
        Carreras = Carrera.objects.all()
        obj = {
            'Carreras':Carreras,
        }
        return render(request,"usuarios/carreras.html", obj)
    return redirect('/')

def añadirCarrera(request):
    if request.user.is_authenticated:
        
        if request.method == 'GET':
            form = CarreraForm()
            Carreras = Carrera.objects.all()
            contexto = {
                'form':form,
                'Carreras':Carreras,
            }
            if form.is_valid():
                form.save()
                return render(request,'usuarios/añadirCarrera.html',contexto)
        else:
            form = CarreraForm(request.POST)
            Carreras = Carrera.objects.all()
            contexto = {
                'form':form,
                'Carreras':Carreras,
            }
            if form.is_valid():
                form.save()
                return render(request,'usuarios/añadirCarrera.html',contexto)
        return render(request,'usuarios/añadirCarrera.html',contexto)
    return redirect('/')

def editarCarrera(request, pk):
    carrera = Carrera.objects.get(pk = pk)
    Carreras = Carrera.objects.all()
    if request.method == 'GET': 
        form = CarreraForm(instance = carrera)
        context = {
            'form':form,
            'Carreras':Carreras,
        }
        if form.is_valid():
            form.save()
            return render(request,'usuarios/añadirCarrera.html', context)
    else:
        form = CarreraForm (request.POST, instance= carrera)
        context = {
            'form':form,
            'Carreras':Carreras,
        }
        if form.is_valid():
            form.save()
            return render(request,'usuarios/añadirCarrera.html', context) 
    return render(request,'usuarios/añadirCarrera.html',context)
    
def eliminarCarrera(request, pk):
    carrera = Carrera.objects.get(pk = pk)
    carrera.delete()
    return redirect('añadirCarrera')

def addHistorial(request, matricula):#formulario para añandir Historiales
    if request.method == 'POST':#Se comprueba si el fomulario envia inf por el metod post
        form = AddHistorialForm(request.POST)#Se crea un objeto mas lo que se obtuno con el post
        matricula = matricula
        if form.is_valid():#Se comprueba si el fomuario es valio
            form.save()#Se guarda la informacicion
            return redirect('autenticacion')#al final se redirecciona al inicio
    else:
        form = AddHistorialForm()#se crea un formulario separado 
        matricula = matricula
    return render(request, "usuarios/addHistorial.html", {'form':form, 'matricula':matricula})


def searchHistorial(request):
    if request.method == 'POST':
        form = viewHistorialForm(request.POST)
        if form.is_valid():
            Matricula = form['Matricula']
            Matricula = Matricula.value()
            return redirect('viewHistorial', Matricula)
    else:
        form = viewHistorialForm()
    return render(request, "usuarios/searchHistorial.html", {'form':form})


def viewHistorial(request, Matricula):
    Matricula = Matricula #se saca la matricula del alumno 
    Alumnos = Alumno.objects.filter(Matricula = Matricula) #se busca la id del alumno mediante la matricula
    for alumnado in Alumnos:#se sacan todos los alumnos     
        historiales = Historial.objects.filter(Alumno = alumnado.pk)#se filta una busqueda para que solo se tengan ciertos datos
        return render(request, 'usuarios/viewHistorial.html',{'Historiales':historiales})


def addPagos(request):
    if request.method == 'POST':
        form = PagosForm(request.POST)
        if form.is_valid():
            form.save()
            idAlumno = form['Historial']#se toma la matricula del alumno ('pk para ser mas preciso')
            idAlumno = idAlumno.value()
            nombrePag = form['Nombre']#se toma el nombre del pago.
            nombrePag = nombrePag.value()
            return redirect('imprimePdf',idAlumno, nombrePag)
            
    else:
        form = PagosForm()
    return render(request, 'usuarios/addPagos.html',{'form':form})

def searchPagos(request):
    if request.method == 'POST':
        form = viewHistorialForm(request.POST)
        if form.is_valid():
            Matricula = form['Matricula']
            Matricula = Matricula.value()
            Alumnos = Alumno.objects.get(Matricula = Matricula)
            HistPagos = Pagos.objects.filter(Historial = Alumnos.pk)
            context = {
                'form':form,
                'validacion':True,
                'Pagos':HistPagos
            }
    else:
        form = viewHistorialForm()
        context = {
                'form':form,
                'validacion':False,
            }
    return render(request, 'usuarios/searchPagos.html',context)


def imprimePdf(request, pk, nombre):
            pk = pk
            nombre = nombre
            alumno = Alumno.objects.get(pk = pk)
            pago = Pagos.objects.filter(Nombre = nombre).filter(Historial=pk)
            template = get_template('baucher/recibo.html')
            context = {
                'comp': {'name': 'Universidad Los Angeles', 'ruc': 'clave', 'address':'Direccion'},
                'Alumno':alumno,
                'Pagos': pago
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf',)
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                    html, dest=response)
            return response

def imprimePdfAdicional(request, pk, nombre):
            pk = pk
            nombre = nombre
            alumno = Alumno.objects.get(pk = pk)
            pago = Pagos.objects.filter(Nombre = nombre).filter(Historial=pk)
            template = get_template('baucher/recibo1.html')
            context = {
                'comp': {'name': 'Universidad Los Angeles', 'ruc': 'clave', 'address':'Direccion'},
                'Alumno':alumno,
                'Pagos': pago
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf',)
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                    html, dest=response)
            return response

def PagoAdicional(request):
    if request.method == 'POST':
        form = PagosAdicionalesForm(request.POST)
        if form.is_valid():
            form.save()
            idAlumno = form['Historial']#se toma la matricula del alumno ('pk para ser mas preciso')
            idAlumno = idAlumno.value()
            nombrePag = form['Nombre']#se toma el nombre del pago.
            nombrePag = nombrePag.value()
            return redirect('imprimePdfAdicional',idAlumno, nombrePag)
            
    else:
        form = PagosAdicionalesForm()
    return render(request, 'usuarios/addPagos.html',{'form':form})