from django.views.generic import View, ListView, TemplateView
from django.shortcuts import render
from charviewer.models import Moves

class Characters(TemplateView):
    template_name = 'charviewer/characters.html'

class BarakaFrames(ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=1)
    context_object_name = 'moves'

class CassieFrames(ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=2)
    context_object_name = 'moves'

