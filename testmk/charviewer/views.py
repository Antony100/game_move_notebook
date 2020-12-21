from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, TemplateView, CreateView, FormView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from charviewer.models import Moves, Notes
from .forms import LoginForm, NoteForm
from django.contrib import messages
from django.contrib.auth.models import User
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
        print (f"the move taken from the frames page is: {request.session['move']}")
        return HttpResponseRedirect(reverse('add_note'))



# def barakaframes(request):
#     qs = Moves.objects.filter(character_id=1)
#     context = {'moves': qs}
#     print(request.POST.get('move_id'))

#     return render(request, 'charviewer/frames.html', context)





class CassieFrames(LoginRequiredMixin, ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=2)
    context_object_name = 'moves'


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

        # print (context['note'])
        return render(request, self.template_name, context)



    def form_valid(self, form):
        # move_id = request.session.get('move')
        note = form.save(commit=False)
        note.note = form.cleaned_data['note']
        note.author = self.request.user
        # note.move_id = move_id
        note.save()
        print(note)

        return HttpResponseRedirect(reverse('characters'))


class UpdateNoteView(LoginRequiredMixin, UpdateView):
    # template_name = 'charviewer/add_note.html'
    template_name = 'charviewer/test_update_note.html'
    model = Notes
    # form_class = NoteForm
    fields = ('note',)
    # success_url = ''

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

    # def get_object(self):
    #     id_ = self.kwargs.get("note_id")
    #     print(id_)
    #     return get_object_or_404(Notes, id=id_)

    def get_success_url(self):
        return reverse('notes')


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


# testing the noteform built into the table
class Expandview(FormView):
    template_name = 'charviewer/expand.html'
    form_class = NoteForm
    queryset = Moves.objects.filter(character_id=1)
    # context_object_name = 'moves'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moves'] = Moves.objects.filter(character_id=1)
        return context


    def form_valid(self, form):
        note = form.save(commit=False)
        note.author = self.request.user

        note.save()

        return HttpResponseRedirect(reverse('notes'))



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


