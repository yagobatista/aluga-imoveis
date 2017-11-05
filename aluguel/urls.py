from django.conf.urls import url
from aluguel.views import home
from aluguel.views import cadastro
from aluguel.views import pesquisa
urlpatterns = [
    url(r'^$',home),
    url(r'^cadastrar/$',cadastro),
    url(r'^pesquisa/$', pesquisa),
]
