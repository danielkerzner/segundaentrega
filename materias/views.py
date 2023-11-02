from django.http import HttpResponse, HttpResponseRedirect
from .temp_data import materia_data
from django.shortcuts import render
from django.urls import reverse

def detail_materia(request, materia_id):
    materia = materia_data[materia_id - 1]
    return HttpResponse(
        f'Detalhes da materia: {materia["name"]} ({materia["professor"]})')

def list_materias(request):
    context = {"materia_list": materia_data}
    return render(request, 'materias/main.html', context)

def detail_materia(request, materia_id):
    context = {'materia': materia_data[materia_id - 1]}
    return render(request, 'materias/detail.html', context)

def search_materias(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "materia_list": [
                m for m in materia_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'materias/search.html', context)

def create_materias(request):
    if request.method == 'POST':
        materia_data.append({
            'name': request.POST['name'],
            'professor': request.POST['professor'],
            'date': request.POST['date'],
            'imagem': request.POST['imagem'],

        })
        return HttpResponseRedirect(
            reverse('materias:detail', args=(len(materia_data), )))
    else:
        return render(request, 'materias/create.html', {})


# Create your views here.
