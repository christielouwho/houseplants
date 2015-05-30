from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .forms import HouseplantSearchForm
from .models import Houseplant


def error(request):
    """for testing purposes"""
    raise Exception


class IndexSearch(ListView):
    template_name = 'index.html'
    model = Houseplant
    form = HouseplantSearchForm

    def get_queryset(self):
        form = HouseplantSearchForm(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data.get('q', '')
            query = Q(common_name__icontains=q) | Q(latin_name__icontains=q)
            return Houseplant.objects.filter(query)
        return Houseplant.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HouseplantSearchForm(self.request.GET)
        return context


class HouseplantDetailView(DetailView):
    template_name = 'houseplant_detail.html'
    model = Houseplant
