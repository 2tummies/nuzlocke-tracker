from django.db import models

# Database tables
class Region(models.Model):
    region_id = models.SmallIntegerField(primary_key=True)
    region_name = models.TextField(unique=True)
    class Meta:
        managed = False
        db_table = 'regions'

class Version(models.Model):
    version_id = models.SmallIntegerField(primary_key=True)
    version_name = models.TextField(unique=True)
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
    nat_dex = models.BooleanField(blank=True, null=True)
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
    region = models.ForeignKey(Region, models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'locations'

class PokemonEncounter(models.Model):
    pk = models.CompositePrimaryKey('location_id', 'pokemon_id', 'method_id')
    location = models.ForeignKey(Location, models.DO_NOTHING)
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING)
    method = models.ForeignKey(EncounterMethod, models.DO_NOTHING)
    nat_dex = models.BooleanField(blank=True, null=True)
    version_exclusive = models.ForeignKey(Version, models.DO_NOTHING, blank=True, null=True)
    time_of_day = models.ForeignKey(TimeOfDay, models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pokemon_encounters'