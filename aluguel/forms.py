from django.forms import ModelForm
from aluguel.models import Aluguel
class AluguelForm(ModelForm):
    class Meta:
        model = Aluguel
        fields = ['nome','telefone','imagem','rua','numero','cidade','bairro']
