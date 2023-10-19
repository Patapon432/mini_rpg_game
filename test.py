import json
import models_mxin
import combat_model

locations = json.load(open('json_files\locations.json', 'r'))

pl_class_file = open('json_files\class.json', 'r')
pl_classes = json.load(pl_class_file)


class Location:
    def __init__(self, name: str):
        self._name = name
        if name:
            self._description = locations[name]["description"]


class Game:
    def __init__(self):
        print('Выбран игрок\n')
        self.player = models_mxin.Player()


    def endgame(self):
        print('Вы проиграли')
        user_choice = input('\n1. Начать заново.\n\n2. Закончить игру.\n\n-------------------------\n\nВведите ваш выбор: ')
        if user_choice == '1':
            return game.start_game()
        else:
            exit()


    def choose_class(self, name = None):
        i = 1
        class_count = []
        classes = []
        for class_name in pl_classes:
            print(f'\n{i}. {class_name}')
            class_count.append(i)
            classes.append(class_name)
            i += 1     
        user_choose = input('\n-------------------------\n\nВведите ваш выбор: ')
        if int(user_choose) in class_count:
            self.player = models_mxin.Player(self.player._name, classes[int(user_choose) - 1])
        else:
            print('\nВы ввели не те символы\n')
            return self.choose_class(self, name = None)
        self.player.status()
        return self.waiting()
    

    def _fight(self, monster: models_mxin.Monster):
        battle = combat_model.Battle(self.player, monster)
        battle.fight()


    def start_game(self):
        self.player._name = input('Вы начали игру\nПожалуйста введите имя персонажа: ')
        self.choose_class()
        self.player.status()
        self.waiting()


    def travel(self):
        while True:
            user_input = input(f'\n-------------------------\n\n1. {"Dungeon"}\n\n2. {"Dead forrest"}\n\n3. {"Curced_village"}\n\n'
                               f'4. {"Вернуться обратно"}\n\n-------------------------\n\nВведите куда вы хотите отправиться: ')
            if user_input == '1':
                location = Location("Dungeon")
                self.dungeon(location) 
            elif user_input == '2':
                location = Location("Dead_forrest")
                self.dungeon(location) 
            elif user_input == '3':
                location = Location("Cursed_village")
                self.dungeon(location) 
            elif user_input == '4':
                print('\nВы решили вернуться обратно!')
                return self.waiting()
            else:
                print('\nВы нажали не ту кнопку!')
        # i = 1
        # locations_count = []
        # locations_list = []
        # for locations_name in locations:
        #     print(f'\n{i}. {locations_name}')
        #     locations_count.append(i)
        #     locations_list.append(locations_name)
        #     i += 1     
        # print(locations_count)
        # user_choose = input('\n-------------------------\nВведите ваш выбор: ')
        # if int(user_choose) in locations_count:
        #     location = Location("", locations[int(user_choose) - 1])
        #     self.dungeon(location)
        # else:
        #     print('\nВы ввели не те символы\n')
        #     return self.travel(self)
        # return self.waiting(self)
                

    def dungeon(self, location: Location):
        print(f'\n{location._name}\n{location._description}')
        if location._name == "Dungeon":
            new_monster = models_mxin.Monster('Zombie')
        elif location._name == "Dead_forrest":
            new_monster = models_mxin.Monster('Lich')
        else:
            location._name == "Curced_village"
            new_monster = models_mxin.Monster('Ogre')    
        user_input = input('\n-------------------------\n1. Идти по подземелью.\n2. Обыскать подземелье.\n3. Вернуться обратно.\nВаш вариант выбора: ')
        if user_input == '1':
            print(f'\nНа своем пути вы встречаете врага! это {new_monster._name}\n')
            self._fight(new_monster)
        

    def waiting(self):
        user_input = input('\n-------------------------\n1. Открыть инвентарь \n2. Просмотр статуса \n3. Отправиться в путешествие\nВведите ваш выбор: ')
        while True:
            if user_input == '1':   
                while True:
                    self.waiting()
                    # inventory.bag.open_inventory()
                    return
                    # user_input = input(f'1. {inventory.bag.items[0]}\n2. {inventory.bag.items[1]}')
                #     inventory.open_inventory()           
                #     user_input = input('\n-------------------------\n1. Выпить зелье исцеления.\n2. Выпить зелье восстановления ресурса.\n3. Закрыть рюкзак\nВведите ваш выбор: ')
                    
                #     if user_input == '1':
                #             if p1._pl_hp < p1._pl_maxhp:  
                #                 p1._pl_hp += 50
                #                 p1.check_max_hp()
                #                 inventory.healing_potion.amount -= 1
                #                 p1.status()
                                
                #             else:
                #                 print(f'\nУ вас максимальное количество здоровья, использовать {inventory.healing_potion.name} нельзя! ')
                #                 p1.status()
                            
                #     elif user_input == '2':
                #         if p1._pl_res < p1._pl_maxres:
                #             p1._pl_res += 50     
                #             p1.check_max_res()
                #             inventory.resource_potion.amount -= 1
                #             p1.status()

                #         else:
                #             print(f'\nУ вас максимальное количество ресурса, использовать {inventory.resource_potion.name} нельзя! ')
                #             p1.status()
            
                #     elif user_input == '3':
                #         waiting()

                #     else:
                #         print('\nВы нажали не ту кнопку!\n')
            elif user_input == '2':
                self.player.status()
                self.waiting()
            elif user_input == '3':
                self.travel()     
            else:
                print('\nВы нажали не ту кнопку!')
                self.waiting()    


game = Game()
game.start_game()