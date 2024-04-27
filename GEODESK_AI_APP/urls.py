from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Directs root URL of the app to the home view
    path('umap/', views.umap_view, name='umap'), # Umap root
    path('geodesk/', views.geodesk_view, name='geodesk'), # geodesk root
    path('umap/home/', views.home_redirect, name='home_redirect'), # Redirects /umap/home to /
    path('geodesk/home/', views.home_redirect, name='home_redirect'), # Redirects /geodesk/home to /
    # other URL patterns
]