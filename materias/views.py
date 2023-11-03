from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import materia


def list_materias(request):
    materia_list = materia.objects.all()
    context = {'materia_list': materia_list}
    return render(request, 'materias/main.html', context)

def detail_materia(request, materia_id):
    materia_detail = get_object_or_404(materia, pk=materia_id)
    context = {'materia': materia_detail}
    return render(request, 'materias/detail.html', context)


def search_materias(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        materia_list = materia.objects.filter(name__icontains=search_term)
        context = {"materia_list": materia_list}
    return render(request, 'materias/search.html', context)

def create_materias(request):
    if request.method == 'POST':
        
        m_name= request.POST['name']
        m_professor = request.POST['professor']
        m_date = request.POST['date']
        m_imagem = request.POST['imagem']
        m_descricao = request.POST['descricao']
        materia_adicionada = materia(name = m_name, professor = m_professor, date = m_date, imagem = m_imagem, descricao = m_descricao)
        materia_adicionada.save()

        return HttpResponseRedirect(
            reverse('materias:detail', args=(len(materia.id), )))
    else:
        return render(request, 'materias/create.html', {})

def update_materia(request, materia_id):
    materia = get_object_or_404(materia, pk=materia_id)

    if request.method == "POST":
        materia.name = request.POST['name']
        materia.professor = request.POST['professor']
        materia.date = request.POST['date']
        materia.imagem = request.POST['imagem']
        materia.descricao = request.POST['descricao']
        materia.save()
        return HttpResponseRedirect(
            reverse('materias:detail', args=(materia.id, )))

    context = {'materia': materia}
    return render(request, 'materias/update.html', context)

def delete_materia(request, materia_id):
    materia = get_object_or_404(materia, pk=materia_id)

    if request.method == "POST":
        materia.delete()
        return HttpResponseRedirect(reverse('materias:main'))

    context = {'materia': materia}
    return render(request, 'materias/delete.html', context)

# Create your views here.
