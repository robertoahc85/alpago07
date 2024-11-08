from django.shortcuts import render, get_object_or_404, redirect
from .models import Escuela
from .form  import EscuelaForm

# Vista para listar todas las escuelas
def escuela_list(request):
    escuelas = Escuela.objects.all()
    return render(request, 'escuelas/escuela_list.html', {'escuelas': escuelas})

# Vista para ver los detalles de una escuela
def escuela_detail(request, pk):
    escuela = get_object_or_404(Escuela, pk=pk)
    return render(request, 'escuelas/escuela_detail.html', {'escuela': escuela})

# Vista para crear una nueva escuela
def escuela_create(request):
    if request.method == "POST":
        form = EscuelaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('escuela_list')
    else:
        form = EscuelaForm()
    return render(request, 'escuelas/escuela_form.html', {'form': form})

# Vista para editar una escuela existente
def escuela_edit(request, pk):
    escuela = get_object_or_404(Escuela, pk=pk)
    if request.method == "POST":
        form = EscuelaForm(request.POST, instance=escuela)
        if form.is_valid():
            form.save()
            return redirect('escuela_list')
    else:
        form = EscuelaForm(instance=escuela)
    return render(request, 'escuelas/escuela_form.html', {'form': form})

# Vista para eliminar una escuela
def escuela_delete(request, pk):
    escuela = get_object_or_404(Escuela, pk=pk)
    if request.method == "POST":
        escuela.delete()
        return redirect('escuela_list')
    return render(request, 'escuelas/escuela_confirm_delete.html', {'escuela': escuela})
