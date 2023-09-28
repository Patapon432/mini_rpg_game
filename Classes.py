import random
import json
import travel_test
# import inventory

location_file = open('json_files\locations.json', 'r')
locations = json.load(location_file)

pl_class_file = open('json_files\class.json', 'r')
pl_classes = json.load(pl_class_file)

m_class_file = open('json_files/monsters.json', 'r')
m_classes = json.load(m_class_file)

class Location:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description

    def dungeon(self):
        if self._name == 'Dungeon':
            print(locations[0]["description"])
            print('\nВы заходите в темное подземелье.\nВы можете:\nИдти вглубь подземелья, или обыскать его.')
            
            while True:
                user_input = input('\n-------------------------\n1. Идти по подземелью.\n2. Обыскать подземелье.\n3. Вернуться обратно.\nВаш вариант выбора:  ')
                if user_input == '1':  
                    m1 = Battle('Zombie', 100, 100, 1, 1, 10, 1, 'Enemy', 50, 5)
                    print('\nЭто подземелье вам кажется бесконечным, ничего не видя на своем пути вы идете дальше.\nНаконец то виден свет в конце коридора.')              #начинается бой с зомби Выход в другую локацию
                    print(f'\nВас что-то хватает за ногу. \nПосмотрев вниз вы видите почти разложившигося мертвеца, перед вами {m1._name}!')
                    m1.enemy_normal_attack()
                    fight()
                        
                elif user_input == '3':
                    print('\nВы решили вернуться обратно ')    
                    waiting()

                else:
                    print('\nВы нажали не ту кнопку')
        if self._name == 'Dead forrest':
            print(locations[1]["description"]) 
            print('Мертвый лес является таким уже несколько сотен лет, даже ветер тут не дует.\nМожет быть тут все таки есть кто - то живой...\n\nВы можете пройти по тропе вглубь леса или обыскать местность.')
            while True:
                user_input = input('\n-------------------------\n1. Пойти по тропе.\n2. Обыскать местность.\n3. Вернуться обратно.\nВаш вариант выбора:  ')
                if user_input == '1':
                    m1 = Battle('Lich', 100, 100, 1, 1, 10, 1, 'Enemy', 50, 5)
                    print('\nПройдя по тропе вы выходите к старому клдбищу. Оно кажется заброшенным, а некоторые могилы разрыты.\nВы замечаете одну могилу в центре, которая сильно выделяется среди остальных, вы подходите к ней и осматриваете. ')              #начинается бой с зомби Выход в другую локацию
                    print(f'\nИз могилы поднимается скелет в одежде мага. \nПеред вами с огнем в глазах стоит {m1._name}!')
                    m1.enemy_normal_attack()
                    p1.fight()
        

class Creature:
    def __init__(self, name: str, hp: int, max_hp: int, mana: int, max_mana: int, damage: int, crit: int, miss_chance: int, xp: int,  lvl: int = None):
        self._name = name
        self._lvl = 0 if not lvl else lvl
        self._hp = hp
        self._max_hp = max_hp
        self._mana = mana
        self._max_mana = max_mana
        self._damage = damage
        self._crit = crit
        self._miss_chance = miss_chance
        self._xp = xp
    
    def get_name(self):
        return self._name
    
    def get_lvl(self):
        return self._lvl
    
    def get_hp(self):
        return self._hp
    
    def get_max_hp(self):
        return self._max_hp
    
    def get_mana(self):
        return self._mana
    
    def get_max_mana(self):
        return self._max_mana
    
    def get_damage_value(self):
        return self._damage
    
    def get_crit_chance(self):
        return self._crit
    
    def get_miss_chance(self):
        return self._miss_chance
    
    def get_xp(self):
        return self._xp

class Player(Creature):
    def __init__(self, name: str, hp: int, max_hp: int,mana: int, max_mana: int, damage: int, crit: int, game_class: str, miss_chance: int, xp: int, lvl: int = None):
        super().__init__(name, hp, max_hp, mana, max_mana, damage, crit, miss_chance, xp, lvl)
        self._game_class = game_class

    def get_game_class(self):
        return self._game_class

    def status(self):
        print(f'-------------------------------\nВаше имя - {self.get_name()}\nКласс вашего персонажа - {self.get_game_class()}\nКоличество вашего здоровья - {self.get_max_hp()}|{self.get_hp()}\nКоличество вашего ресурса - {self.get_max_mana()}|{self.get_mana()}\nВаш уровень - {self.get_lvl()}\nКоличество вашего опыта - {self.get_xp()}')    

class Monster(Creature):
    def __init__(self, name: str, hp: int, mana: int, damage: int,  loot, crit: int, miss_chance: int, xp: int, lvl: int = None):
        super().__init__(name, hp, mana, damage, crit, miss_chance, xp, lvl)
        self._loot = loot
    
    def get_loot(self):
        pass
    
class Battle(Creature):
    def __init__(self, name: str, hp: int, max_hp: int, mana: int, max_mana: int, damage: int, crit: int, game_class: str, miss_chance: int, xp: int, lvl: int = None):
        super().__init__(name, hp, max_hp, mana, max_mana, damage, crit, miss_chance, xp, lvl)
        self._game_class = game_class
        print(self._name)

    def player_attack(self):
        if self._game_class == 'Archer':
            print('Вы выпускаете стрелу')
        elif self._game_class == 'Warrior':  
            print('Вы бьете мечом')  
        elif self._game_class == 'Mage':
            print('Вы атакуете посохом')
        if self.get_miss_chance() <= random.randint(0, 100):       
            if self.get_crit_chance() >= random.randint(0, 100):
                m1._hp -= (self.get_damage_value() * 2)
                print(f'Критический удар!\nВы наносите {p1.get_damage_value() * 2} по {m1.get_name()}!\n')
            else:
                print(f'Вы наносите {self.get_damage_value()} по {m1.get_name()}!\n')
                m1._hp -= self.get_damage_value()
        else:
            print('Вы промахнулись!\n')
        
    def enemy_normal_attack(self):
        if self.get_miss_chance() <= random.randint(0, 100):
            p1._hp -= self.get_damage_value() 
            print(f'{self.get_name()} атакует вас!\nВы получаете {self.get_damage_value()} урона!\n')
        else:
            print(f'{self.get_name()} промахнулся!\n')

    def enemy_normal_attack_true_strike(self):
            p1._hp -= self.get_damage_value() 
            print(f'{self.get_name()} атакует вас!\nВы получаете {self.get_damage_value()} урона!\n')

    def cast_spell(self):
        if self.get_mana() >= 25:
            self._mana -= 25
            if self._game_class == 'Archer':
                m1._hp = 0
                print(f'Вы выпускаете стрелу в голову {m1.get_name()}\nВраг повержен!\n')
            elif self._game_class == 'Warrior':
                print('Своей яростью вы устрашаете врага\nВраг пропускает ход!\n')
            elif self._game_class == 'Mage':
                print(f'Вы выпускаете огненный шар!\nВы наносите {self.get_damage_value() * 3} по {m1.get_name()}!\n')
                m1._hp -= self.get_damage_value() * 3
        else:
            print('Вам не хватает маны!\n')

    def enemy_cast_spell(self):
        if self.get_name() == 'Zombie':
            if random.randint(0, 3) > 2:
                print(f'{self.get_name()} разозлился и атакует вас 3 раза!\n')
                self.enemy_normal_attack()
                self.enemy_normal_attack()
                self.enemy_normal_attack()
            else:
                print(f'{self.get_name()} разозлился и атакует вас 2 раза!\n')
                self.enemy_normal_attack()
                self.enemy_normal_attack()
        elif self.get_name() == 'Lich':
            p1._hp -= (self.get_damage_value() * 3)
            print(f'{self.get_name()} выпускает в вас ледяную стрелу!\nВы получаете {self.get_damage_value() * 5} урона!\n')
        elif self.get_name() == 'Ogre':
            p1._hp = 0
            print(f'{self.get_name()} ломает вам череп!\n')

    def protect(self):
        if self._game_class == 'Archer':
            print('\nВы готовы к атаке противника и будете защищаться')
            if random.randint(0, 100) >= 25:
                print('Вы не смогли увернуться от атаки, в вас попали!', end=' ')
                m1.enemy_normal_attack_true_strike()
            else:
                print('Вы успешно уклонились от удара\n')
        elif self._game_class == 'Warrior':
            print(f'\nВы готовы к атаке противника и будете защищаться\n{m1.get_name()} нанес {(m1.get_damage_value() / 3)} урона!\n')
            self._hp -= (m1.get_damage_value() / 3)
        elif self._game_class == 'Mage':
            print(f'\nВы готовы к атаке противника и будете защищаться\n{m1.get_name()} нанес {(m1.get_damage_value() * 0.75)} урона!\n')
            self._hp -= m1.get_damage_value() * 0.75

    def enemy_full_attack(self):
        if self.get_name() == 'Zombie':
            if random.randint(0, 100) >= 25:
                self.enemy_normal_attack()
            else:
                self.enemy_cast_spell()
        elif self.get_name() == 'Lich':
            if random.randint(0, 100) >= 60:
                self.enemy_normal_attack()
            else:
                self.enemy_cast_spell()
        elif self.get_name() == 'Ogre':
            if random.randint(0, 100) >= 10:
                self.enemy_normal_attack()
            else:
                self.enemy_cast_spell()
        
    def skipping_a_move(self):
        print('Вы ничего не делаете и пропускаете ход!\n')
        m1.enemy_full_attack()

    def fight_status(self):
        print(f'-------------------------------\nИмя врага - {m1.get_name()}\nЗдоровье врага - {m1.get_max_hp()}|{m1.get_hp()}\nКоличество вашего здоровья - {self.get_max_hp()}|{self.get_hp()}\nКоличество вашего ресурса - {self.get_max_mana()}|{self.get_mana()}')

    def xp_up(self):
        self._xp += m1._xp
        if self._xp >=100:
            self._lvl += + 1
            print(f'\nПоздравляем, вы подняли свой уровень! Ваш уровень - {self._lvl}')
            self._max_hp += 50
            self._pl_hp = self._max_hp
            self._max_mana +=50
            self._pl_res = self._max_mana
        self.fight_status()


player = Player('test',100, 100, 100, 100, 15, 50, 'Mage', 15, 0, 1)
m1 = Battle('Zombie', 100, 100, 1, 1, 10, 1, 'Enemy', 50, 5)
p1 = Battle(player.get_name(), player.get_hp(), player.get_max_hp(), player.get_mana(), player.get_max_mana(), player.get_damage_value(), player.get_crit_chance(), player._game_class, player.get_miss_chance(), player.get_xp(), player.get_lvl())
print(p1.__class__)


def fight():
    while p1._hp or m1._hp >0 :        
        user_choice = input('\nВыберите одно действие:\n----------------------\n1. Обычный удар. 2. Способность персонажа. 3. Защититься. 4. Пропуск хода. \nВведите ваш выбор: ')
        if user_choice == '1':
            p1.player_attack()
            if m1._hp <= 0:
                break
                # p1.win_instance
                # m1.m_drop()
                # p1.xp_up()
                # waiting()
            m1.enemy_full_attack()
        elif user_choice == '2':
            p1.cast_spell()
                

        elif user_choice == '3':
            p1.protect()

        elif user_choice == '4':
            p1.skipping_a_move()
        else:
            print('\nВы нажали не ту кнопку!\n')
        p1.fight_status()
    else:
        waiting()

def waiting():
    user_input = input('\n-------------------------\n1. Открыть инвентарь \n2. Просмотр статуса \n3. Отправиться в путешествие\nВведите ваш выбор: ')
    while True:
        if user_input == '1':
            waiting()
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
            player.status()
            waiting()
        elif user_input == '3':
            travel_test.travel()
        else:
            print('\nВы нажали не ту кнопку!')
            waiting()

# p1.xp_up()
# # inventory.bag.add_item(inventory.healpotion)
# # inventory.bag.open_inventory()
# waiting()

# print(player.__class__)
# player.status()


# def travel():
#     while True:
#         user_input = input(f'\n-------------------------\nВведите куда вы хотите отправиться\n1. {locations[0]["name"]}\n2. {locations[1]["name"]}\n3. {locations[2]["name"]}\nВведите ваш выбор: ')
#         if user_input == '1':
#             location = Location(locations[0]["name"], locations[0]["description"])
#             m1 = Battle('Zombie', 100, 100, 1, 1, 10, 1, 'Enemy', 50, 5)
#             location.dungeon()
#         elif user_input == '2':
#             dead_forrest()
#         elif user_input == '3':
#             curced_village()
#         else:
#             print('\nВы нажали не ту кнопку!\n')       

# travel()

fight()