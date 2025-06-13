from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.GetAllPokemon.as_view(), name='list-pokemon'),
    path('pokemon/<str:pokemon_name>', views.SearchPokemon.as_view(), name='find-pokemon'),
    path('regions/', views.GetAllRegions.as_view(), name='get-regions'),
    path('regions/<str:region_name>', views.SearchRegions.as_view(), name='search-regions'),
    path('versions/', views.GetAllVersions.as_view(), name='get-versions'),
    path('versions/<str:version_name>', views.SearchVersions.as_view(), name='search-versions'),
]