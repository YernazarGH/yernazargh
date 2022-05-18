from urllib.parse import urlencode

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView

from webapp.forms import SearchForm, MyTariffForm
from webapp.models import AllTariff, MyTariff


class ListTariffView(ListView):
    template_name = 'webapp/tariff_list.html'
    context_object_name = 'tariffs'
    model = AllTariff

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super(ListTariffView, self).get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = (
                    Q(gb__icontains=self.search_value['searchgb']) |
                    Q(sms__icontains=self.search_value['searchsms']) |
                    Q(min__icontains=self.search_value['searchmin'])
            )
            queryset = queryset.filter(query)
        return queryset


def index_view(request):
    return render(request, 'webapp/main.html')


class CreateMyTariffView(CreateView):
    model = MyTariff
    form_class = MyTariffForm
    template_name = 'webapp/tariff_list.html'

    def form_valid(self, form):
        tariff = get_object_or_404(AllTariff, pk=self.kwargs.get('pk'))
        mytariff = form.save(commit=False)
        mytariff.tariff = tariff
        mytariff.user = self.request.user
        mytariff.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('tariff_list')


class DetailTariffView(DetailView):
    model = AllTariff
    template_name = 'webapp/tariff_detail.html'
    context_object_name = 'tariff'