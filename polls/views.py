from django.shortcuts import render
from .models import Especie

# Create your views here.
def index(request):
    lista_especies = Especie.objects.all()
    context = {'lista_especies': lista_especies}
    return render(request, 'polls/index.html', context)