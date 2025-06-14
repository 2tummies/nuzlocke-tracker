from django.db import connection
from django.http import JsonResponse

def get_all_encounter_methods():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM encounter_methods')
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)
    
def search_encounter_methods(string):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM encounter_methods WHERE method_name ILIKE %s;',
            ['%' + string + '%']
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)