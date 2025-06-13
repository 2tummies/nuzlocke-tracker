from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ['id', 'name']

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['dex_number', 'name']

class EncounterMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncounterMethod
        fields = ['id', 'name', 'nat_dex']

class TimeOfDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOfDay
        fields = ['id', 'name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'region']

class PokemonEncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonEncounter
        fields = ['location', 'pokemon', 'method', 'nat_dex', 'version_exclusive', 'time_of_day']

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['name']

# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()

#     class Meta:
#         model = Book
#         fields = ['title', 'author']
