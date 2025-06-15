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
    
def get_version_by_id(version_id):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version_name FROM versions WHERE version_id = %s',
            [version_id]
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)