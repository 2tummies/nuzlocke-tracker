from django.db import connection
from django.http import JsonResponse

def get_all_regions():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM regions;')
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)

def search_regions(string):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM regions WHERE region_name ILIKE %s;',
            ['%' + string + '%']
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)
    
def get_regions_by_version(version_id):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT regions.region_name FROM regions ' +
            'JOIN versions_regions ON regions.region_id = versions_regions.region_id ' +
            'WHERE version_id = %s;',
            [version_id]
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)