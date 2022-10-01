from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

def saludo(request):
    return HttpResponse ('<h1> Buenas y santas </h1>')

def fecha (request):
    fecha_actual = datetime.now()
    return HttpResponse (f'La hora y fecha actual es {fecha_actual}')

def calcular_fecha_nac(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años, es {fecha}')

def mi_template (request):
    
    cargar_archivo = open(r'C:\Users\fedef\OneDrive\Documentos\Python\Proyecto\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)
