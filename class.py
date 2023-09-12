import random
import json

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

    def cursed_village(self):
        self._name = locations[2]["name"]
        self._description = locations[2]["description"]

class Travel:
    def __init__(self, location: Location = None ):
        self._locaton = location

    def curced_village():
        print(f'\nВы входите в {locations[2]["name"]}')
        print('От этой деревни отказалась империя, после того, как ее проклял лич.\nЕсть сомнение, бывал бы кто-нибудь здесь в последнее время...\nВы можете пройти внутрь деревни или обыскать здания.')
        
        while True:
            m1._name = m_classes[2]["name"]
            m1._hp = m_classes[2]["hp"]
            m1._damage = m_classes[2]["damage"]
            m1._max_hp = m_classes[2]["max_hp"]

            user_input = input('\n-------------------------\n1. Пойти вглубь деревни.\n2. Обыскать здания.\n3. Вернуться обратно.\nВаш вариант выбора:  ')
            if user_input == '1':
                print('\nДеревня призрак - это все, что приходит вам в голову, когда вы идете по ее улицам.\nПодойдя на главную площадь вы видите в ее центре огромное существо.\nПодойдя ближе существо вас замечает. \n')              #начинается бой с зомби Выход в другую локацию
                print(f'\nПеред тобой стоит {m1.get_name()}!')
                m1.enemy_normal_attack()
                fight()

            elif user_input == '2':
                pass
                    # С шансом 20% можно найти сундук в котором будет зелье здоровья и зелье восстановления ресурса
                # if random.randint(0, 100) >= 80:
                #     print(f'\nВы нашли сундук с сокровищами!\n В нем было 1 - {inventory.healing_potion.name}, и 1 - {inventory.resource_potion.name}')
                #     inventory.healing_potion.amount += 1
                #     inventory.resource_potion.amount += 1
                #     inventory.open_inventory
                    
                # else:
                #     print('\nК сожалению тут ничего нет, попробуйте другое место.\n')
                
            elif user_input == '3':
                print('\nВы решили вернуться обратно')
                # waiting()
                
            else:
                print('\nВведен не тот символ\n')
            





class Creature:
    def __init__(self, name: str, hp: int, max_hp: int, mana: int, max_mana: int, damage: int, crit: int, miss_chance: int, lvl: int = None):
        self._name = name
        self._lvl = 0 if not lvl else lvl
        self._hp = hp
        self._max_hp = max_hp
        self._mana = mana
        self._max_mana = max_mana
        self._damage = damage
        self._crit = crit
        self._miss_chance = miss_chance
    
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

class Player(Creature):
    def __init__(self, name: str, hp: int, max_hp: int,mana: int, max_mana: int, damage: int, crit: int, game_class: str, miss_chance: int, lvl: int = None):
        super().__init__(name, hp, max_hp, mana, max_mana, damage, crit, miss_chance, lvl)
        self._game_class = game_class


class Monster(Creature):
    def __init__(self, name: str, hp: int, mana: int, damage: int, xp: int, loot, crit: int, miss_chance: int, lvl: int = None):
        super().__init__(name, hp, mana, damage, crit, miss_chance, lvl)
        self._xp = xp
        self._loot = loot

    def get_xp(self):
        return self._xp
    
    def get_loot(self):
        pass
    
class Battle(Creature):
    def __init__(self, name: str, hp: int, max_hp: int, mana: int, max_mana: int, damage: int, crit: int, game_class: str, miss_chance: int, lvl: int = None):
        super().__init__(name, hp, max_hp, mana, max_mana, damage, crit, miss_chance, lvl)
        self._game_class = game_class

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



player = Player('test',100, 100, 100, 100, 15, 50, 'Mage', 15)
m1 = Battle('Zombie', 100, 100, 1, 1, 10, 1, 'Enemy', 50)
p1 = Battle(player.get_name(), player.get_hp(), player.get_max_hp(), player.get_mana(), player.get_max_mana(), player.get_damage_value(), player.get_crit_chance(), player._game_class, player.get_miss_chance())
print(p1.__class__)

def fight():
    while True:
        if p1._hp <= 0:
            break
        elif m1._hp <=0:
            break
        
        
            # m1.m_drop()
            # p1.xp_up()
            # waiting()
        else:
            # p1.fight_hp_status()
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


# p1.player_attack()
# m1.enemy_normal_attack()
# p1.cast_spell()
# m1.attack()
# m1.cast_spell()
# p1.protect()
# # attack()
# cast_spell()
# monst_attack()

fight()