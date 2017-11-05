from django.conf.urls import url
from aluguel.views import home
from aluguel.views import cadastro
urlpatterns = [
    url(r'^$',home),
    url(r'^cadastrar/$',cadastro),
]
