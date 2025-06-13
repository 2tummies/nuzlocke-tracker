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