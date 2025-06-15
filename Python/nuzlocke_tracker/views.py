from rest_framework import generics

from .serializers import *
from .sql import pokemon_sql, regions_sql, versions_sql, encounter_methods_sql, locations_sql, times_of_day_sql

class GetAllPokemon(generics.ListAPIView):
    serializer_class = Pokemon
    def get(self, req):
        return pokemon_sql.get_all_pokemon()
    
class SearchPokemon(generics.ListAPIView):
    serializer_class = Pokemon
    def get(self, req, **kwargs):
        pokemon_search = kwargs['pokemon_name']
        return pokemon_sql.search_pokemon(pokemon_search)
    
class GetAllRegions(generics.ListAPIView):
    serializer_class = Region
    def get(self, req):
        return regions_sql.get_all_regions()
    
class SearchRegions(generics.ListAPIView):
    serializer_class = Region
    def get(self, req, **kwargs):
        region_search = kwargs['region_name']
        return regions_sql.search_regions(region_search)
    
class GetAllVersions(generics.ListAPIView):
    serializer_class = Region
    def get(self, req):
        return versions_sql.get_all_versions()
    
class SearchVersions(generics.ListAPIView):
    serializer_class = Region
    def get(self, req, **kwargs):
        version_search = kwargs['version_name']
        return versions_sql.search_versions(version_search)
    
class GetAllEncounterMethods(generics.ListAPIView):
    serializer_class = EncounterMethod
    def get(self, req):
        return encounter_methods_sql.get_all_encounter_methods()
    
class SearchEncounterMethods(generics.ListAPIView):
    serializer_class = EncounterMethod
    def get(self, req, **kwargs):
        method_search = kwargs['method_name']
        return encounter_methods_sql.search_encounter_methods(method_search)
    
class GetAllTimesOfDay(generics.ListAPIView):
    serializer_class = TimeOfDay
    def get(self, req):
        return times_of_day_sql.get_all_times()
    
class SearchTimesOfDay(generics.ListAPIView):
    serializer_class = TimeOfDay
    def get(self, req, **kwargs):
        time_search = kwargs['time_of_day_name']
        return times_of_day_sql.search_times(time_search)
    
class GetAllLocations(generics.ListAPIView):
    serializer_class = Location
    def get(self, req):
        return locations_sql.get_all_locations()
    
class SearchLocationLocations(generics.ListAPIView):
    serializer_class = Location
    def get(self, req, **kwargs):
        location_search = kwargs['location_name']
        return locations_sql.search_locations(location_search)
    
class GetRegionsByVersion(generics.ListAPIView):
    serializer_class = GameVersion
    def get(self, req, **kwargs):
        version_locations_search = kwargs['version_id']
        return regions_sql.get_regions_by_version(version_locations_search)

# ListAPIView for endpoints that exclusively use GET
# ListCreateAPIView for endpoints that use GET and POST
# CreateAPIView for enpoints that exclusively use POST