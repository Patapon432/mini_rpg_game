import json
import random

locations = json.load(open('json_files\locations.json', 'r'))
 
monsters_file = open('json_files/monsters.json', 'r')
monster = json.load(monsters_file)

pl_class_file = open('json_files\class.json', 'r')
pl_classes = json.load(pl_class_file)

class Player:
    def __init__(self, player_name:str= None, name:str = None):

        self._name = player_name
        if name:
            self._hp = pl_classes[name]['hp']
            self._max_hp = pl_classes[name]['max_hp']
            self._damage = pl_classes[name]['damage']
            self._game_class = name
            self._miss_chance = pl_classes[name]['miss_chance']
            self._crit_chance = pl_classes[name]['crit_chance']
            self._mana = pl_classes[name]['mana']
            self._max_mana = pl_classes[name]['max_mana']
            self._xp = pl_classes[name]['xp']
            self._lvl = pl_classes[name]['lvl']

    def get_hit(self, damage):
        self._hp -= damage
    
    def status(self):
        print(f'-------------------------------\n\nВаше имя - {self._name}\n'
              f'Класс вашего персонажа - {self._game_class}\nКоличество вашего здоровья - {self._max_hp}|{self._hp}\n'
              f'Количество вашего ресурса - {self._max_mana}|{self._mana}\n'
              f'Ваш уровень - {self._lvl}\n'
              f'Количество вашего опыта - {self._xp}\n')

    def xp_up(self, xp):
        self._xp += xp
        if self._xp >= 100:
            self._xp = 0
            self._lvl += 1
            self._damage += 15
            self._max_hp += 20
            self._max_mana += 20
            self._hp = self._max_hp
            self._mana = self._max_mana
            print(f'Вы повысили уровень! Теперь ваш уровень составляет {self._lvl}.\nВаши характеристики увеличены!')
            
        self.status()


class Monster:
    def __init__(self, name: str):
        self._name = name
        self._damage = monster[name]["damage"]
        self._crit = monster[name]["crit"]
        self._exp = monster[name]["xp"]
        self._miss_chance = monster[name]["miss_chance"]
        self._max_hp = monster[name]["max_hp"]
        self._hp = monster[name]["hp"]
        self._lvl = monster[name]["lvl"]
     
    def get_hit(self, damage):
        self._hp -= damage

class Battle:
    def __init__(self, player: Player, monster: Monster):
        self.player = player
        self.monster = monster

    def fight_status(self):
        print(f'-------------------------------\n\nИмя врага - {self.monster._name}\nЗдоровье врага - {self.monster._max_hp}|{self.monster._hp}\n'
              f'Количество вашего здоровья - {self.player._max_hp}|{self.player._hp}\nКоличество вашего ресурса - {self.player._max_mana}|{self.player._mana}')

    def fight(self):
        while self.player._hp > 0 and self.monster._hp > 0:
                self.fight_status()       
                user_choice = input('\nВыберите одно действие:\n----------------------\n1. Обычный удар. 2. Способность персонажа. 3. Защититься. 4. Пропуск хода. \nВведите ваш выбор: ')
                if user_choice == '1':
                    self.player_attack()
                    self.enemy_full_attack()
                elif user_choice == '2':
                    self.cast_spell()
                elif user_choice == '3':
                    self.protect()
                elif user_choice == '4':
                    print('Вы ничего не делаете')
                    self.enemy_full_attack()
                else:
                    print('\nВы нажали не ту кнопку!\n')    
        else:
            if self.player._hp > 0:
                print('Вы победили')
                self.player.xp_up(self.monster._exp)
                return game.waiting()
            else:
                return game.endgame()

    def player_attack(self):
            if self.player._game_class == 'Archer':
                print('\nВы выпускаете стрелу')
            elif self.player._game_class == 'Warrior':  
                print('\nВы бьете мечом')  
            elif self.player._game_class == 'Mage':
                print('\nВы атакуете посохом')
            if self.player._miss_chance <= random.randint(0, 100):       
                if self.player._crit_chance >= random.randint(0, 100):
                    self.monster.get_hit(self.player._damage * 2)
                    print(f'Критический удар!\nВы наносите {self.player._damage * 2} по {self.monster._name}!\n')
                else:
                    print(f'Вы наносите {self.player._damage} по {self.monster._name}!\n')
                    self.monster.get_hit(self.player._damage)
            else:
                print('Вы промахнулись!\n')

    def enemy_normal_attack(self):
        if self.monster._miss_chance <= random.randint(0, 100):
            self.player.get_hit(self.monster._damage) 
            print(f'{self.monster._name} атакует вас!\nВы получаете {self.monster._damage} урона!\n')
        else:
            print(f'{self.monster._name} промахнулся!\n')

    def enemy_normal_attack_true_strike(self):
            self.player.get_hit(self.monster._damage) 
            print(f'{self.monster._name} атакует вас!\nВы получаете {self.monster._damage} урона!\n')

    def cast_spell(self):
        if self.player._mana >= 25:
            self.player._mana -= 25
            if self.player._game_class == 'Archer':
                self.monster._hp = 0
                print(f'\nВы выпускаете стрелу в голову {self.monster._name}\nВраг повержен!\n')
            elif self.player._game_class == 'Warrior':
                print('\nСвоей яростью вы устрашаете врага\nВраг пропускает ход!\n')
            elif self.player._game_class == 'Mage':
                print(f'\nВы выпускаете огненный шар!\nВы наносите {self.player._damage * 3} по {self.monster._name}!\n')
                self.monster.get_hit(self.player._damage * 3)
        else:
            print('Вам не хватает маны!\n')
        
    def enemy_cast_spell(self):
        if self.monster._name == 'Zombie':
            if random.randint(0, 3) > 2:
                print(f'{self.monster._name} разозлился и атакует вас 3 раза!\n')
                self.enemy_normal_attack()
                self.enemy_normal_attack()
                self.enemy_normal_attack()
            else:
                print(f'{self.monster._name} разозлился и атакует вас 2 раза!\n')
                self.enemy_normal_attack()
                self.enemy_normal_attack()
        elif self.monster._name == 'Lich':
            self.player.get_hit(self.monster._damage * 3)
            print(f'{self.monster._name} выпускает в вас ледяную стрелу!\nВы получаете {self.monster._damage * 5} урона!\n')
        elif self.monster._name == 'Ogre':
            self.player._hp = 0
            print(f'{self.monster._name} ломает вам череп!\n')

    def enemy_full_attack(self):
        if self.monster._hp > 0:
            if self.monster._name == 'Zombie':
                if random.randint(0, 100) >= 25:
                    self.enemy_normal_attack()
                else:
                    self.enemy_cast_spell()
            elif self.monster._name == 'Lich':
                if random.randint(0, 100) >= 60:
                    self.enemy_normal_attack()
                else:
                    self.enemy_cast_spell()
            elif self.monster._name == 'Ogre':
                if random.randint(0, 100) >= 10:
                    self.enemy_normal_attack()
                else:
                    self.enemy_cast_spell()
        else:
            pass

    def protect(self):
        if self.player._game_class == 'Archer':
            print('\nВы готовы к атаке противника и будете уколняться')
            if random.randint(0, 100) >= 25:
                print('Вы не смогли увернуться от атаки, в вас попали!', end=' ')
                self.enemy_normal_attack_true_strike()
            else:
                print('Вы успешно уклонились от удара\n')
        elif self.player._game_class == 'Warrior':
            print(f'\nВы готовы к атаке противника и будете защищаться\n{self.monster._name} нанес {(self.monster._damage / 3)} урона!\n')
            self.player.get_hit(self.monster._damage / 3)
        elif self.player._game_class == 'Mage':
            print(f'\nВы готовы к атаке противника и будете защищаться\n{self.monster._name} нанес {(self.monster._damage * 0.75)} урона!\n')
            self.player.get_hit(self.monster._damage  * 0.75)

class Location:
    def __init__(self, name: str):
        self._name = name
        if name:
            self._description = locations[name]["description"]

class Game:
    def __init__(self):
        print('Выбран игрок\n')
        self.player = Player()

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
            self.player = Player(self.player._name, classes[int(user_choose) - 1])
        else:
            print('\nВы ввели не те символы\n')
            return self.choose_class(self, name = None)
        return self.waiting()
    
    def _fight(self, monster: Monster):
        battle = Battle(self.player, monster)
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
            new_monster= Monster('Zombie')
        elif location._name == "Dead_forrest":
            new_monster= Monster('Lich')
        else:
            location._name == "Curced_village"
            new_monster= Monster('Ogre')    
        user_input = input('\n-------------------------\n1. Идти по подземелью.\n2. Обыскать подземелье.\n3. Вернуться обратно.\nВаш вариант выбора: ')
        if user_input == '1':
            print(f'\nНа своем пути вы встречаете врага! это {new_monster._name}\n')
            self._fight(new_monster)
        
    def waiting(self):
        user_input = input('\n-------------------------\n1. Открыть инвентарь \n2. Просмотр статуса \n3. Отправиться в путешествие\nВведите ваш выбор: ')
        while True:
            if user_input == '1':
                self.waiting()
                # while True:   
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