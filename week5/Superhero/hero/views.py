from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Superhero
from .models import Hero

class IndexView(TemplateView):
    template_name = 'index.html'

class SuperHeroListView(ListView):
    model = Superhero
    template_name = 'superhero_list.html'

class SuperHeroDetailView(TemplateView):
    model = Superhero
    template_name = 'superhero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Hero.objects.get(pk=hero_id)
        return {'hero': hero}