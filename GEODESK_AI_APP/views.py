from django.shortcuts import render,redirect
import numpy as np 
import umap


# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'GEODESK_AI_APP/home.html')

def umap_view(request):
    # Pass the embedding data to the template
    return render(request, 'GEODESK_AI_APP/umap.html')

def geodesk_view(request):
    # Pass the embedding data to the template
    return render(request, 'GEODESK_AI_APP/geodesk.html')

def home_redirect(request):
    return redirect('/')

def umap_redirect(request):
    return redirect('umap')

def geodesk_redirect(request):
    return redirect('geodesk')