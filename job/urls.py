from django.urls import path
from .views import *
urlpatterns = [
    path("registration/",registrationview.as_view()),
    path("login/",login.as_view()),
]
