from django.urls import path

from StoreApp import views
urlpatterns = [
    path('',views.index_function,name='home'),
    path('shop/',views.shop_function,name='shop'),
    path('about/',views.aboutus_function,name='about'),
    path('categories/',views.categories_function,name='categories'),
    path('contact/',views.contactus_function,name='contact'),
    path('electronics/',views.electronics_function,name='electronics'),
    path('fashion',views.fashion_function,name='fashion'),
    path('homeanddecorations/',views.home_and_decorations_function,name='homeanddecorations'),
    path('toyandgames/',views.toys_and_games_function,name='toyandgames'),
    path('sportsandfitness/',views.sports_and_fitness_function,name='sportsandfitness'),
    path('skincare/',views.skincare_function,name='skincare'),
]