from django.shortcuts import render
import numpy as np 
import umap


# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'GEODESK_AI_APP/home.html')

def umap_view(request):
    # Generate random data points for demonstration
    np.random.seed(42)
    n_samples = 1000
    n_features = 10
    data = np.random.rand(n_samples, n_features)

    # Process the data using UMAP
    reducer = umap.UMAP()
    embedding = reducer.fit_transform(data)

    # Pass the embedding data to the template
    return render(request, 'umap.html', {'embedding': embedding})