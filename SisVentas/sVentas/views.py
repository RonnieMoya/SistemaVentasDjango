from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from sVentas.models import Category
# Create your views here.
def myfirstView(request):
    data={
        'name': 'Ronnie',
        'categorias': Category.objects.all()
    }
    return render (request, "home.html",data)