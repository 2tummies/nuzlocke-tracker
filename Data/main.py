import urllib.request
import json
import time

BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    val = input('type 1 for 1-5, 6 to parse big .csv, type anything else to exit:  ')
    if val == '1':
        with open('pokemon.txt', 'a') as file:
            for num in range(1,6):
                new_url = BASE_URL + str(num)
                req = urllib.request.urlopen(new_url)
                data = json.loads(req.read().decode('utf-8'))
                name = data['name']
                file.write(f"({num}, '{name}'),\n")
                time.sleep(2)
            print('all done')
    elif val == '6':
        with open('poke.csv', 'r') as read_file:
            with open('pokemon.txt', 'a') as write_file:
                for line in read_file.readlines():
                    new_line = line.strip().split(',')
                    number = int(new_line[0])
                    write_file.write(f"({number}, '{new_line[1].capitalize()}'),\n")
    elif val == '8':
        with open('old_locations.txt', 'r') as read_file:
            with open('new_locations.txt', 'a') as write_locations_file:
                with open('new_locations_regions.txt', 'a') as write_locations_regions_file:
                    for line in read_file.readlines():
                        new_line = line.strip().split(', ')
                        write_locations_file.write(f"({int(new_line[0])}, {new_line[1].title()}),\n")
                        val_three = None
                        val_four = None
                        if len(new_line) < 4 or new_line[3] == 'pass':
                            val_three = 0
                        else:
                            val_three = new_line[3]
                        if len(new_line) > 4:
                            if new_line[4] is not None:
                                val_four = new_line[4]
                        else:
                            val_four = 0
                        write_locations_regions_file.write(f"({int(new_line[0])}, {int(new_line[2])}, {val_three}, {val_four}),\n")


    else:
        print('Goodbye')

if __name__ == "__main__":
    main()