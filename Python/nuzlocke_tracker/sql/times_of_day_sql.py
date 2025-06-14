from django.db import connection
from django.http import JsonResponse

def get_all_times():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM time_of_day;')
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)
    
def search_times(string):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM time_of_day WHERE time_of_day_name ILIKE %s;',
            ['%' + string + '%']
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)