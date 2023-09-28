import json
import random

monsters_file = open('json_files/monsters.json', 'r')
m_class = json.load(monsters_file)

class Player:
    # def __init__(self, name: str, hp: int, max_hp: int, mana: int, max_mana: int, damage: int, crit: int, miss_chance: int, xp: int,  lvl: int = None):
    #     self._name = name
    #     self._lvl = 0 if not lvl else lvl
    #     self._hp = hp
    #     self._max_hp = max_hp
    #     self._mana = mana
    #     self._max_mana = max_mana
    #     self._damage = damage
    #     self._crit = crit
    #     self._miss_chance = miss_chance
    #     self._xp = xp
    def __init__(self):
        self._name = 'Test'
        self._hp = 100
        self._max_hp = 100
        self._damage = 20
        self._game_class = 'Archer'
        self._miss_chance = 15
        self._crit_chance = 15
        self._mana = 100
        self._max_mana = 100
        self._xp = 0
        self._lvl = 1

    def get_hit(self, damage):
        self._hp -= damage
    
    def status(self):
        print(f'-------------------------------\nВаше имя - {self._name}\nКласс вашего персонажа - {self._game_class}\nКоличество вашего здоровья - {self._max_hp}|{self._hp}\nКоличество вашего ресурса - {self._max_mana}|{self._mana}\nВаш уровень - {self._lvl}\nКоличество вашего опыта - {self._xp}')
    
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
    def __init__(self, name):
        self._name = name
        self._hp = 100
        # if self._name == 'Zombie':
        #     self._damage = m_class[0]["damage"]
        #     self._crit = m_class[0]["crit"]
        #     self._xp = m_class[0]["xp"] 
        #     self._miss_chance = m_class[0]["miss_chance"]
        #     self._max_hp = m_class[0]["max_hp"]
        #     self._hp = m_class[0]["hp"]
        #     self._lvl = m_class[0]["lvl"]
            
        # elif self._name == 'Lich':
        #     self._damage = m_class[1]["damage"]
        #     self._crit = m_class[1]["crit"]
        #     self._xp = m_class[1]["xp"] 
        #     self._miss_chance = m_class[1]["miss_chance"]
        #     self._max_hp = m_class[1]["max_hp"]
        #     self._hp = m_class[1]["hp"]
        #     self._lvl = m_class[1]["lvl"]

        # elif self._name == 'Ogre':
        #     self._damage = m_class[2]["damage"]
        #     self._crit = m_class[2]["crit"]
        #     self._xp = m_class[2]["xp"] 
        #     self._miss_chance = m_class[2]["miss_chance"]
        #     self._max_hp = m_class[2]["max_hp"]
        #     self._hp = m_class[2]["hp"]
        #     self._lvl = m_class[2]["lvl"]

    def get_hit(self, damage):
        self._hp -= damage

    def choose_monster(self, name: str):
        print(f'Выбран монстр {self._name}\n HP: {m_class[name]["hp"]}\n Урон: {m_class[name]["damage"]}')

class Battle:
    def __init__(self, player: Player, monster: Monster):
        self.player = player
        self.monster = monster

    def fight_status(self):
        print(f'-------------------------------\nИмя врага - {self.monster._name}\nЗдоровье врага - {self.monster._max_hp}|{self.monster._hp}\nКоличество вашего здоровья - {self.player._max_hp}|{self.player._hp}\nКоличество вашего ресурса - {self.player._max_mana}|{self.player._mana}')

    def fight(self):
        while True: 
            if self.player._hp <= 0:
                print('Игра окончена')
                break
            elif self.monster._hp <= 0:
                print('Вы победили монстра!')
                self.player.xp_up(self.monster._xp)
                print(self.player._xp)
                break
            else:
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
                print(f'Вы выпускаете стрелу в голову {self.monster._name}\nВраг повержен!\n')
            elif self.player._game_class == 'Warrior':
                print('Своей яростью вы устрашаете врага\nВраг пропускает ход!\n')
            elif self.player._game_class == 'Mage':
                print(f'Вы выпускаете огненный шар!\nВы наносите {self.player._damage * 3} по {self.monster._name}!\n')
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

class Game:
    def __init__(self):
        print('Выбран игрок\n')
        self.player = Player()

    def _fight(self, monster: Monster):
        print(f'27 Ваше хп сейчас {self.player._hp}')
        battle = Battle(self.player, monster)
        battle.fight()
               
    def start_game(self):
        print('Вы начали игру\nСейчас будет драка с монстром\n')
        new_monster = Monster('Zombie')
        self._fight(new_monster)
        print('Вы подрались с монстром')

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
                # player.status()
                self.waiting()
            elif user_input == '3':
                # travel_test.travel()
                battle = Battle
            else:
                print('\nВы нажали не ту кнопку!')
                self.waiting()    

game = Game()
game.start_game()