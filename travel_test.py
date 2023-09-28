import Classes
import json

location_file = open('json_files\locations.json', 'r')
locations = json.load(location_file)

def travel():
    while True:
        user_input = input(f'\n-------------------------\nВведите куда вы хотите отправиться\n1. {locations[0]["name"]}\n2. {locations[1]["name"]}\n3. {locations[2]["name"]}\nВведите ваш выбор: ')
        if user_input == '1':
            location = Classes.Location(locations[0]["name"], locations[0]["description"])
            location.dungeon()
        elif user_input == '2':
            location = Classes.Location(locations[1]["name"], locations[1]["description"])
            location.dungeon()
        elif user_input == '3':
            # curced_village()
            pass
        else:
            print('\nВы нажали не ту кнопку!')   

travel()    