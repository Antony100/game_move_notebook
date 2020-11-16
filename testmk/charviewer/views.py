from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, TemplateView, CreateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from charviewer.models import Moves
from .forms import LoginForm, NoteForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse


class Characters(LoginRequiredMixin, TemplateView):
    template_name = 'charviewer/characters.html'


class BarakaFrames(LoginRequiredMixin, ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=1)
    # context_object_name = 'moves'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moves'] = Moves.objects.filter(character_id=1)
        return context

        return HttpResponseRedirect(reverse('notes'))


class CassieFrames(LoginRequiredMixin, ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=2)
    context_object_name = 'moves'


class Notebook(LoginRequiredMixin, TemplateView):
    template_name = 'charviewer/notes.html'


class AddNoteView(LoginRequiredMixin, FormView):
    template_name = 'charviewer/add_note.html'
    queryset = Moves.objects.filter(character_id=1)
    form_class = NoteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moves'] = Moves.objects.filter(character_id=1)
        return context

    # def get_success_url(self):
    #     return reverse('notes')

    def form_valid(self, form):
        note = form.save(commit=False)
        note.author = self.request.user
        # note.move_id = GET_MOVE_ID_HERE

        note.save()

        return HttpResponseRedirect(reverse('notes'))


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

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():

#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             # new_user.set_password(
#             #     user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.email = user_form.cleaned_data['email']
#             print(new_user.email)
#             new_user.save()
#             return render(request,
#                           'registration/register_done.html',
#                           {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request,
#                   'registration/register.html',
#                   {'user_form': user_form})


