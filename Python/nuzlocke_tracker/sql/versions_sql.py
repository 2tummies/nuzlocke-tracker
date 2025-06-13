from django.db import connection
from django.http import JsonResponse

def get_all_versions():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM versions;')
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)

def search_versions(string):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM versions WHERE version_name ILIKE %s;',
            ['%' + string + '%']
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)