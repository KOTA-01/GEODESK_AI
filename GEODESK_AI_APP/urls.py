from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Directs root URL of the app to the home view
]