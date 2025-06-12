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
    if val == '6':
        with open('poke.csv', 'r') as read_file:
            with open('pokemon.txt', 'a') as write_file:
                for line in read_file.readlines():
                    new_line = line.strip().split(',')
                    number = int(new_line[0])
                    write_file.write(f"({number}, '{new_line[1].capitalize()}'),\n")
    else:
        print('Goodbye')

if __name__ == "__main__":
    main()