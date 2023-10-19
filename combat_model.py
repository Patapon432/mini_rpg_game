# import json
import models_mxin
import test
import random

class Battle:

    def __init__(self, player: models_mxin.Player, monster: models_mxin.Monster):
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
                return test.game.waiting()
            else:
                return test.game.endgame()


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

