from django.shortcuts import render

from MiApp.models import Familiar
# Create your views here.

def mostrar_familia(request):
    f1 = Familiar(nombre='Jose Norberto', apellido='Torres', edad=55, cumpleanios='1967-10-27')
    f2 = Familiar(nombre='Viviana Monica', apellido='Garcia', edad=55, cumpleanios='1967-09-19')
    f3 = Familiar(nombre='Selene Monica', apellido='Torres', edad=23, cumpleanios='1998-09-19')

    return render(request, 'amigos.html', {'familiares':[f1, f2, f3]})

