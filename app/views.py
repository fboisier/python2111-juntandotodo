from django.shortcuts import redirect, render
from app.models import Camion, Ruta
from django.contrib import messages


# Create your views here.
def index(request):
    
    context = {
        "nombre" : "Francisco",
        "listaCamiones" : Camion.objects.all()
    }
    
    
    return render(request, 'app/index.html', context)

def addCamion(request):
    # print(request.POST)
    
    errors = Camion.objects.validar(request.POST)
    
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:    
        Camion.objects.create(
            nombre=request.POST['nombre'], 
            marca=request.POST['marca'], 
            tonelaje=request.POST['tonelaje']
            )

        messages.success(request,"El camion fue agregado correctamente")
        return redirect('/')

def addRuta(request):
    print(request.POST)
    
    
    if len(request.POST['origen']) == 0:
        messages.error(request,"ORIGEN NO PUEDE SER VACIO.")
        return redirect('/')
    
    camion = Camion.objects.get(id=request.POST['camion'])
    
    
    Ruta.objects.create(
        camion=camion, 
        origen=request.POST['origen'], 
        destino=request.POST['destino'], 
        kilometros=request.POST['kms']
        )

    messages.success(request, "La ruta fue agregada correctamente.")
    return redirect('/')


def prueba(request):
    
    messages.success(request,"MENSAJE DE EXITO (success)")
    messages.error(request,"MENSAJE DE ERROR (error)")
    messages.info(request,"MENSAJE DE INFORMACION (info)")
    messages.warning(request,"MENSAJE DE ADVERTENCIA (warning)")
    
    return redirect('/')