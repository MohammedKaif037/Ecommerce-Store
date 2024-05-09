from django.shortcuts import render

# Create your views here.

def index_function(request):
    return render(request, 'StoreApp/index.html')
