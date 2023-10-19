

import json

monster = json.load(open('json_files/monsters.json', 'r'))

pl_classes = json.load(open('json_files\class.json', 'r'))

class AbstractClass:
    def __init__(self, player_name: str = None, name: str = None, hp: int = None, max_hp: int = None, damage: int = None, game_class: str = None):
        self._player_name = player_name
        self._name = name
        self._hp = hp
        self._max_hp = max_hp
        self._damage = damage
        self._game_class = game_class
        exp: int = 100

    def get_hit(self, damage):
        self._hp -= damage


class Player(AbstractClass):
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


class Monster(AbstractClass):
    def __init__(self, name: str):
        self._name = name
        self._damage = monster[name]["damage"]
        self._crit = monster[name]["crit"]
        self._exp = monster[name]["xp"]
        self._miss_chance = monster[name]["miss_chance"]
        self._max_hp = monster[name]["max_hp"]
        self._hp = monster[name]["hp"]
        self._lvl = monster[name]["lvl"]
    
    
    
     
