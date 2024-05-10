from django.shortcuts import render

from StoreApp.models import Category, products

# Create your views here.

def index_function(request):
    all_products=products.objects.filter(pid_for_home=1)
    return render(request, 'StoreApp/index.html', {'products': all_products})

def shop_function(request):
    return render(request, 'StoreApp/shop.html')

def aboutus_function(request):
    return render(request, 'StoreApp/about.html')

def categories_function(request):
    return render(request, 'StoreApp/categories.html')

def contactus_function(request):
    return render(request, 'StoreApp/contactus.html')

def electronics_function(request):
    category_id=Category.objects.get(title='Electronics').id
    electronics_products=products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html',{'electronics_products':electronics_products})
def fashion_function(request):
    category_id = Category.objects.get(title='Fashion').id
    fashion_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'fashion_products': fashion_products})

def home_and_decorations_function(request):
    category_id = Category.objects.get(title='Home and Garden').id
    home_and_decor_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'home_and_decor_products': home_and_decor_products})

def toys_and_games_function(request):
    category_id = Category.objects.get(title='Toys and Games').id
    toys_and_games_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'toys_and_games_products': toys_and_games_products})

def sports_and_fitness_function(request):
    category_id = Category.objects.get(title='Sports and Fitness').id
    sports_and_fitness_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'sports_and_fitness_products': sports_and_fitness_products})

def skincare_function(request):
    category_id = Category.objects.get(title='Skincare and cosmetics').id
    skincare_products = products.objects.filter(category=category_id)
    return render(request, 'StoreApp/index.html', {'skincare_products': skincare_products})

