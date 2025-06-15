from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.GetAllPokemon.as_view(), name='list-pokemon'),
    path('pokemon/<str:pokemon_name>', views.SearchPokemon.as_view(), name='find-pokemon'),
    path('regions/', views.GetAllRegions.as_view(), name='get-regions'),
    path('regions/<str:region_name>', views.SearchRegions.as_view(), name='search-regions'),
    path('versions/', views.GetAllVersions.as_view(), name='get-versions'),
    path('versions/<str:version_name>', views.SearchVersions.as_view(), name='search-versions'),
    path('versions/<int:version_id>/regions/', views.GetRegionsByVersion.as_view(), name='version-regions'),
    path('encounter_methods/', views.GetAllEncounterMethods.as_view(), name='list-encounter-methods'),
    path('encounter_methods/<str:method_name>', views.SearchEncounterMethods.as_view(), name='search-encounter-methods'),
    path('times_of_day/', views.GetAllTimesOfDay.as_view(), name='list-times-of-day'),
    path('times_of_day/<str:time_of_day_name>', views.SearchTimesOfDay.as_view(), name='search-times-of-day'),
    path('locations/', views.GetAllLocations.as_view(), name='list-locations'),
    path('locations/<str:location_name>', views.SearchLocationLocations.as_view(), name='search-locations'),
]