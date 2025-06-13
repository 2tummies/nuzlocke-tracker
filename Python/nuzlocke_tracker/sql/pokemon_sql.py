from django.db import connection
from django.http import JsonResponse

def get_all_pokemon():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM pokemon;')
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)

def search_pokemon(string):
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT * FROM pokemon WHERE pokemon_name ILIKE %s;',
            ['%' + string + '%']
        )
        rows = cursor.fetchall()
        return JsonResponse(rows, safe=False)
