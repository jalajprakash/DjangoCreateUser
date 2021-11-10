from django.urls import path
from .views import RegisterView, ContactList


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('', ContactList.as_view())
] 