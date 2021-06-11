from django.urls import path
from . import views
from users.views import imprimePdf


urlpatterns = [
    path('logout', views.logout),
    path('autenticacion', views.autenticacion, name='autenticacion'),
    path('carreras', views.VisualizarCarreras),
    path('añadirCarrera', views.añadirCarrera, name='añadirCarrera'),
    path('editarCarreras/<int:pk>/',views.editarCarrera,name = 'Editar_Carreras'),
    path('addAlumno/', views.AddAlumno, name = 'addAlumno'),
    path('editAlumno/<int:pk>/', views.editAlumnos, name = 'editAlumno'),#ruta para la edicion de alumnos.
    path('eliminarCarrera/<int:pk>/',views.eliminarCarrera,name = 'eliminarCarrera'),
    path('addHistorial/<str:matricula>/', views.addHistorial, name = 'addHistorial'),#ruta para añadir historiales
    path('searchHistorial/', views.searchHistorial, name = 'searchHistorial'),
    path('viewHistorial/<str:Matricula>/', views.viewHistorial, name = 'viewHistorial'),
    path('addPagos/', views.addPagos, name = 'addPagos'),
    path('searchPagos/', views.searchPagos, name = 'searchPagos'), 
    path('imprimePdf/<int:pk>/<str:nombre>', views.imprimePdf,name = 'imprimePdf'),
    path('PagoAdicional/', views.PagoAdicional, name = 'PagoAdicional'),
    path('imprimePdfAdicional/<int:pk>/<str:nombre>', views.imprimePdfAdicional,name = 'imprimePdfAdicional'),
]

