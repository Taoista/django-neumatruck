from django.shortcuts import render
from django.http import HttpResponse, QueryDict  
from inicio.components.configuracion.configuracion_controller import ConfiguracionController

# Create your views here.
def getConfigure():
    controller = ConfiguracionController()
    data = controller.get_all()
    return data

def index(request):
   

    context = {
        'data' : getConfigure()
    }

    return render(request,'index.html', context)



def login(request):
   

    context = {
        'data' : getConfigure()
    }
    return render(request, 'login.html', context)





