from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import materia
from .forms import materiaForm


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
        form = materiaForm(request.POST)
        if form.is_valid():
            materia_name = form.cleaned_data['name']
            materia_professor = form.cleaned_data['professor']
            materia_date = form.cleaned_data['date']
            materia_imagem = form.cleaned_data['imagem']
            materia_descricao = form.cleaned_data['descricao']
            materia_criada = materia(name=materia_name,professor = materia_professor, date = materia_date, imagem = materia_imagem, descricao = materia_descricao)
            materia_criada.save()
            return HttpResponseRedirect(
                reverse('materias:detail', args=(materia_criada.id, )))
    else:
        form = materiaForm()
    context = {'form': form}
    return render(request, 'materias/create.html', context)

    
def delete_materia(request, materia_id):
    materia_del = get_object_or_404(materia, pk=materia_id)

    if request.method == "POST":
        materia_del.delete()
        return HttpResponseRedirect(reverse('materias:confirm_delete'))

    context = {'materia': materia_del}
    return render(request, 'materias/delete.html', context)

def confirm_delete(request):
    context = {}
    return render(request, 'materias/confirm_delete.html', context)


def update_materia(request, materia_id):
    materia_atual = get_object_or_404(materia, pk=materia_id)

    if request.method == "POST":
        form = materiaForm(request.POST)
        if form.is_valid():
            materia_atual.name= form.cleaned_data['name']
            materia_atual.professor = form.cleaned_data['professor']
            materia_atual.date = form.cleaned_data['date']
            materia_atual.imagem = form.cleaned_data['imagem']
            materia_atual.descricao = form.cleaned_data['descricao']
            materia_atual.save()
            return HttpResponseRedirect(
                reverse('materias:detail', args=(materia_atual.id, )))
    else:
        form = materiaForm(
            initial={
                'name': materia_atual.name,
                'professor': materia_atual.professor,
                'date': materia_atual.date,
                'imagem': materia_atual.imagem,
                'descricao':materia_atual.descricao
            })

    context = {'materia': materia_atual, 'form': form}
    return render(request, 'materias/update.html', context)
    

# Create your views here.
