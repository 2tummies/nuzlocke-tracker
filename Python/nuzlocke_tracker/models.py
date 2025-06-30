from django.db import models

from .sql import regions_sql

# Database Tables
class Region(models.Model):
    region_id = models.SmallIntegerField(primary_key=True)
    region_name = models.TextField(unique=True)
    class Meta:
        managed = False
        db_table = 'regions'

class Version(models.Model):
    version_id = models.SmallIntegerField(primary_key=True)
    version_name = models.TextField(unique=True)
    generation_num = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'versions'

class Pokemon(models.Model):
    dex_number = models.SmallIntegerField(primary_key=True)
    pokemon_name = models.TextField(unique=True)
    class Meta:
        managed = False
        db_table = 'pokemon'

class EncounterMethod(models.Model):
    method_id = models.SmallIntegerField(primary_key=True)
    method_name = models.TextField(unique=True)
    class Meta:
        managed = False
        db_table = 'encounter_methods'

class TimeOfDay(models.Model):
    time_of_day_id = models.SmallIntegerField(primary_key=True)
    time_of_day_name = models.TextField(unique=True)
    class Meta:
        managed = False
        db_table = 'time_of_day'

class Location(models.Model):
    location_id = models.SmallIntegerField(primary_key=True)
    location_name = models.TextField()
    class Meta:
        managed = False
        db_table = 'locations'

class PokemonEncounter(models.Model):
    pk = models.CompositePrimaryKey('location_id', 'pokemon_id', 'method_id')
    location = models.ForeignKey(Location, models.DO_NOTHING)
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING)
    method = models.ForeignKey(EncounterMethod, models.DO_NOTHING)
    version_exclusive = models.SmallIntegerField()
    time_of_day = models.ForeignKey(TimeOfDay, models.DO_NOTHING, blank=True, null=True)
    percent_encounter = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'pokemon_encounters'

# Combo Tables
class VersionsRegions(models.Model):
    pk = models.CompositePrimaryKey('version_id', 'region_id')
    version_id = models.ForeignKey(Version, on_delete=models.CASCADE, db_column='version_id')
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='region_id')
    class Meta:
        managed = False
        db_table = 'versions_regions'

class LocationsRegions(models.Model):
    pk = models.CompositePrimaryKey('location_id', 'region_id')
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, db_column='location_id')
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='region_id')
    game_exclusive_id = models.SmallIntegerField()
    gen_exclusive_id = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'locations_regions'

# Wrapper Classes
class GameVersion:
    def __init__(self, version: Version):
        self.version = version
        self.id = version.version_id
        self.name = version.version_name
        self.region_list = self.get_regions()
    def get_regions(self):
        return regions_sql.get_regions_by_version(self.id)