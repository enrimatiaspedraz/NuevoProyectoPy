from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .models import Boton
from .models import Turno
# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    return render(request, 'gestionCursos.html', {'cursos': cursosListados})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    
    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/') 

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'edicionCurso.html', {"curso": curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    
    return redirect('/') 




def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    
    return redirect('/') 

def probando(request):
    
    nombre="Leo"
    creditos="10"
    
    boton = Boton.objects.create(
        nombre=nombre, creditos=creditos)
    
    return redirect('/')



def tienda(request):
    turnosListados = Turno.objects.all()
    return render(request, 'tienda.html', {'turnos': turnosListados})

def registrarTurno(request):
    nombre=request.POST['nombre']
    fecha=request.POST['fecha']
    hora=request.POST['hora']
    
    
    turno = Turno(
        nombre=nombre, fecha=fecha, hora=hora)
    turno.save()
    
    return redirect('/tienda') 

def eliminarTurno(request, id):
    eliminarturno = get_object_or_404(Turno, id=id)
    eliminarturno.delete()
    
    return redirect('/tienda')

def edicionTurno(request, id):
    turno = get_object_or_404(Turno, id=id)
    return render(request, 'edicionTurno.html', {"turno": turno})

def editarTurno(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    fecha=request.POST['fecha']
    hora=request.POST['hora']
    
   
    turno = Turno.objects.get(id=id)
    turno.nombre = nombre
    turno.fecha = fecha
    turno.hora = hora
    turno.save()
    
    return redirect('/tienda') 

