from django.conf.urls import url
from app.views import error, IndexSearch, HouseplantDetailView

urlpatterns = [
    url(r'^error/', error, name='error'),
    url(r'^$', IndexSearch.as_view(), name='index'),
    url(r'^plants/(?P<slug>[-_\w]+)$', HouseplantDetailView.as_view(), name='houseplant_detail'),
]

from .signals import *  # NOQA ensure that the signals are attatched via import
