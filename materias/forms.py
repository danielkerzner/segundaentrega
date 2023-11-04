from django.forms import ModelForm
from .models import materia


class materiaForm(ModelForm):
    class Meta:
        model = materia
        fields = [
            'name',
            'professor',
            'date',
            'imagem',
            'descricao',
        ]
        labels = {
            'name': 'Nome e Código da Matéria',
            'professor': 'Professor Responsável',
            'date': 'Data de Ativação (favor colocar no modelo: aaaa-mm-dd)',
            'imagem': 'URL da imagem representativa',
            'descricao': 'Descrição (Recomendo copiar do Jupyter)'
        }