from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('characters/', views.Characters.as_view(), name='characters'),
    path('add_note/', views.AddNoteView.as_view(), name='add_note'),
    path('update_note/<int:pk>/',
         views.UpdateNoteView.as_view(), name='update_note'),
    path('delete_note/<int:pk>/',
         views.DeleteNoteView.as_view(), name='delete_note'),
    path('notes/', views.Notebook.as_view(), name='notes'),
    path('baraka/', views.BarakaFrames.as_view(), name='baraka'),
    path('cassie/', views.CassieFrames.as_view(), name='cassie'),
    # Authentication
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register_done/',
         views.RegisterDoneView.as_view(), name='register_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
