from django.contrib import admin
from django.urls import path
from .views import signup, login, create_note, get_note, update_note

urlpatterns = [
 path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('notes/create/', create_note, name='create_note'),
    path('notes/<int:id>/', get_note, name='get_note'),
    path('notes/<int:id>/', update_note, name='update_note'),
]
