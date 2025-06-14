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