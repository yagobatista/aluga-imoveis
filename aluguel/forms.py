from django.forms import ModelForm
from aluguel.models import Aluguel
class AluguelForm(ModelForm):
    class Meta:
        model = Aluguel
        fields = ['nome','telefone','rua','numero','cidade','bairro']
