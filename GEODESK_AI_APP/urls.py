from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Directs root URL of the app to the home view
    path('umap/', views.umap_view, name='umap'), # Umap root
    path('umap/home/', views.umap_home_redirect, name='umap_home_redirect'), # Redirects /umap/home to /
    # other URL patterns
]