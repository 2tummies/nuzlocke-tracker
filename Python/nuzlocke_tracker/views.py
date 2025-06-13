from rest_framework import generics

from .serializers import *
from .sql import pokemon_sql, regions_sql, versions_sql

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

# ListAPIView for endpoints that exclusively use GET
# ListCreateAPIView for endpoints that use GET and POST
# CreateAPIView for enpoints that exclusively use POST