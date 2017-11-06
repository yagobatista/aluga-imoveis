from django.conf.urls import url
from aluguel.views import home
from aluguel.views import cadastro
from aluguel.views import pesquisa
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$',home),
    url(r'^cadastrar/$',cadastro),
    url(r'^pesquisa/$', pesquisa),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
