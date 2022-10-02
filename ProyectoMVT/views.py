from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

def saludo(request):
    return HttpResponse ('<h1> Buenas y santas </h1>')

def fecha (request):
    fecha_actual = datetime.now()
    return HttpResponse (f'La hora y fecha actual es {fecha_actual}')

def calcular_fecha_nac(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años, es {fecha}')

def mi_template (request):
    
    cargar_archivo = open(r'C:\Users\fedef\OneDrive\Documentos\Python\Proyecto\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def tu_template (request, nombre):
    
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
        
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    mi_contexto = {
        'rango': list(range (1,11)),
        'valor_aleatorio': random.randrange(1,11)
        }
    
    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)
        
    return HttpResponse(template_renderizado)
