from django.conf.urls import url, include
from .views import do_search

urlpatterns = [
    url(r'^$', do_search, name='search')
]