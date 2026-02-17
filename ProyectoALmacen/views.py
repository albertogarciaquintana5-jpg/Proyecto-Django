from django.shortcuts import render, redirect, get_object_or_404
from .models import childs, fathers, classroom, teachers
from .form import ChildsForm, FathersForm, ClassroomForm

def home(request):
    error = None
    if request.method == 'POST':
        usuario = request.POST.get('usuario', '').strip()
        contrasena = request.POST.get('contraseña', '').strip()
        existe = teachers.objects.filter(Nombre=usuario, contrasena=contrasena).exists()
        if existe:
            return redirect('inicio')
        error = 'Usuario o contraseña incorrectos.'
    return render(request, 'login.html', {'error': error})

def inicio(request):
    return render(request, 'Inicio.html')

# ============ NIÑOS ============
def lista_niños(request):
    niños = childs.objects.all()
    return render(request, 'lista_niños.html', {'childs': niños})

def crear_niño(request):
    if request.method == 'POST':
        form = ChildsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_niños')
    else:
        form = ChildsForm()
    return render(request, 'crear.html', {'form': form, 'titulo': 'Registrar Niño'})

def editar_niño(request, id):
    niño = get_object_or_404(childs, id=id)
    if request.method == 'POST':
        form = ChildsForm(request.POST, instance=niño)
        if form.is_valid():
            form.save()
            return redirect('lista_niños')
    else:
        form = ChildsForm(instance=niño)
    return render(request, 'crear.html', {'form': form, 'titulo': 'Editar Niño'})

def borrar_niño(request, id):
    niño = get_object_or_404(childs, id=id)
    if request.method == 'POST':
        niño.delete()
        return redirect('lista_niños')
    return render(request, 'borrar.html', {'objeto': niño, 'tipo': 'niño', 'nombre': f"{niño.name} {niño.last_name}"})

# ============ PADRES ============
def lista_padres(request):
    padres = fathers.objects.all()
    return render(request, 'lista_padres.html', {'padres': padres})

def crear_padre(request):
    if request.method == 'POST':
        form = FathersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_padres')
    else:
        form = FathersForm()
    return render(request, 'crear.html', {'form': form, 'titulo': 'Registrar Padre'})

def editar_padre(request, id):
    padre = get_object_or_404(fathers, id=id)
    if request.method == 'POST':
        form = FathersForm(request.POST, instance=padre)
        if form.is_valid():
            form.save()
            return redirect('lista_padres')
    else:
        form = FathersForm(instance=padre)
    return render(request, 'crear.html', {'form': form, 'titulo': 'Editar Padre'})

def borrar_padre(request, id):
    padre = get_object_or_404(fathers, id=id)
    if request.method == 'POST':
        padre.delete()
        return redirect('lista_padres')
    return render(request, 'borrar.html', {'objeto': padre, 'tipo': 'padre', 'nombre': f"{padre.name} {padre.last_name}"})

# ============ CLASES ============
def lista_clases(request):
    clases = classroom.objects.all()
    return render(request, 'lista_clases.html', {'clases': clases})

def crear_clase(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clases')
    else:
        form = ClassroomForm()
    return render(request, 'crear.html', {'form': form, 'titulo': 'Registrar Clase'})

def editar_clase(request, id):
    clase = get_object_or_404(classroom, id=id)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            return redirect('lista_clases')
    else:
        form = ClassroomForm(instance=clase)
    return render(request, 'crear.html', {'form': form, 'titulo': 'Editar Clase'})

def borrar_clase(request, id):
    clase = get_object_or_404(classroom, id=id)
    if request.method == 'POST':
        clase.delete()
        return redirect('lista_clases')
    return render(request, 'borrar.html', {'objeto': clase, 'tipo': 'clase', 'nombre': clase.clase})
