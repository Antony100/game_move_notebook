from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View, ListView, TemplateView
from django.shortcuts import render
from charviewer.models import Moves
from .forms import LoginForm

class Characters(LoginRequiredMixin, TemplateView):
    template_name = 'charviewer/characters.html'


class BarakaFrames(LoginRequiredMixin, ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=1)
    context_object_name = 'moves'


class CassieFrames(LoginRequiredMixin, ListView):
    template_name = 'charviewer/frames.html'
    queryset = Moves.objects.filter(character_id=2)
    context_object_name = 'moves'


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     # return HttpResponse('Authenticated '
#                     #                     'successfully')
#             #     else:
#             #         return HttpResponse('Disabled account')
#             # else:
#             #     return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})
