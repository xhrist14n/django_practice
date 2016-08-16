from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect

def redirect(request):
   script = "<script>window.location='index.html'</script>"
   return HttpResponse(script)

def main(request):
   text = "<div>hola mundo</h1>"
   return HttpResponse(text)

def index(request):
   text = "<div>Sitio principal</h1>"
   return HttpResponse(text)
