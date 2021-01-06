from .forms import NoteForm, UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView, TemplateView, CreateView, FormView, UpdateView, DeleteView)
from django.shortcuts import redirect, render
from charviewer.models import Moves, Notes
from django.urls import reverse


class Characters(LoginRequiredMixin, TemplateView):
    template_name = 'charviewer/characters.html'


class BarakaFrames(LoginRequiredMixin, ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=1)
    context_object_name = 'moves'

    def get_context_data(self, **kwargs):
        context = super(BarakaFrames, self).get_context_data(**kwargs)
        context['moves'] = self.queryset
        return context

    def post(self, request, *args, **kwargs):
        request.session['move'] = request.POST.get('move_id')
        return HttpResponseRedirect(reverse('add_note'))


class CassieFrames(LoginRequiredMixin, ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=2)
    context_object_name = 'moves'

    def get_context_data(self, **kwargs):
        context = super(CassieFrames, self).get_context_data(**kwargs)
        context['moves'] = self.queryset
        return context

    def post(self, request, *args, **kwargs):
        request.session['move'] = request.POST.get('move_id')
        return HttpResponseRedirect(reverse('add_note'))


class Notebook(LoginRequiredMixin, ListView):
    template_name = 'charviewer/notes.html'
    # queryset = Notes.objects.filter(author_id=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.get_queryset
        context['moves'] = Moves.objects.all()
        return context

    def get_queryset(self):
        return Notes.objects.filter(author_id=self.request.user)


class AddNoteView(LoginRequiredMixin, CreateView):
    template_name = 'charviewer/add_note.html'
    model = Notes
    form_class = NoteForm

    def get(self, request, *args, **kwargs):
        move_id = request.session.get('move')
        context = {
            'moves': Moves.objects.filter(id=move_id),
            'note': Notes.objects.filter(move_id=move_id),
        }
        # if note exists, fetch note id and redirect to UpdateNoteView with id
        if Notes.objects.filter(move_id=move_id).exists():
            note_id = Notes.objects.filter(move_id=move_id).values()[0]['id']
            print(f'the note id is: {note_id}')
            return redirect(f'/update_note/{note_id}')

        return render(request, self.template_name, context)

    def form_valid(self, form):
        note = form.save(commit=False)
        note.note = form.cleaned_data['note']
        note.author = self.request.user
        note.save()
        print(note)

        return HttpResponseRedirect(reverse('characters'))


class UpdateNoteView(LoginRequiredMixin, UpdateView):
    template_name = 'charviewer/update_note.html'
    model = Notes
    fields = ('note',)

    def form_valid(self, form):
        note = form.save(commit=False)
        note.note = form.cleaned_data['note']
        note.author = self.request.user
        # note.move_id = move_id
        note.save()

        return HttpResponseRedirect(reverse('notes'))


class DeleteNoteView(LoginRequiredMixin, DeleteView):
    template_name = 'charviewer/delete_note.html'
    model = Notes

    def get_success_url(self):
        return reverse('notes')


# Registration
class RegisterView(FormView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = 'registration/register_done.html'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.email = form.cleaned_data['email']
        new_user.save()

        return HttpResponseRedirect(reverse('register_done'))


class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'
