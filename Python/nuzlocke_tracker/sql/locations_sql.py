from django.db import connection
from django.http import JsonResponse

def get_all_locations():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM locations;')
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)
    
def search_locations(string):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM locations WHERE location_name ILIKE %s;',
            ['%' + string + '%']
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)

def get_locations_by_version_and_region(version_id, region_id):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT DISTINCT locations.location_id, locations.location_name FROM locations ' +
            'JOIN locations_regions ON locations.location_id = locations_regions.location_id ' +
            'JOIN regions ON locations_regions.region_id = regions.region_id ' +
            'JOIN versions_regions ON versions_regions.region_id = versions_regions.region_id ' +
            'JOIN versions ON versions.version_id = versions_regions.version_id ' +
            'WHERE versions.version_id = %s AND regions.region_id = %s ' +
            'ORDER BY locations.location_id;',
            [version_id, region_id]
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)