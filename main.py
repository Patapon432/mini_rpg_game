import json

import random

import inventory 


location_file = open('json_files\locations.json', 'r')
locations = json.load(location_file)

pl_class_file = open('json_files\class.json', 'r')
pl_classes = json.load(pl_class_file)

m_class_file = open('json_files/monsters.json', 'r')
m_classes = json.load(m_class_file)

class Player:
    def __init__(self, pl_name, pl_class_name, pl_damage, pl_hp, pl_res, pl_lvl, pl_maxhp, pl_maxres, xp):   # Класс игрок  Инициализация атрибутов игрока

        self._pl_name = pl_name
        self._pl_class_name = pl_class_name
        self._pl_damage = pl_damage
        self._pl_hp = pl_hp
        self._pl_res = pl_res   
        self._pl_maxhp = pl_maxhp
        self._pl_lvl = pl_lvl    
        self._pl_maxres = pl_maxres 
        self._pl_xp = xp


    def xp_up(self):
        p1._pl_xp += 70    
        if p1._pl_xp >= 100:
            p1.pl_lvlup()
            p1._pl_xp = 0
        print(f'Поздравляем, вы получили 25 опыта\nДо следующего уровня {100 - p1._pl_xp} Опыта!')

    def status(self):
        print(f'\nВаше имя - {p1._pl_name}\nВаш класс - {p1._pl_class_name}\nКоличество вашего здоровья - {p1._pl_maxhp}|{p1._pl_hp}\nКоличество вашего ресурса - {p1._pl_maxres}|{p1._pl_res}\nВаш уровень - {p1._pl_lvl}\n'
              f'Количество вашего опыта - {p1._pl_xp}\nКоличество опыта до следующего уровня - {100 - p1._pl_xp} ')
        
    def win_instance(self):
        print(f'Вы победили {m1._m_name}')

    def game_over(self):
        while True:
            user_input = input('\nВы проиграли. 1. Попробовать снова 2. Сдаться\nВведите ваш вариант выбора: ')
            if user_input == '1':
                start_game()
            if user_input == '2':
                exit()
            else:
                print('Не те символы')
                continue

    def fight_hp_status(self):
        print(f'-------------------------------\nЗдоровье врага - {m1._m_hp}\nКласс врага - {m1._m_class}\nКоличество вашего здоровья - {p1._pl_maxhp}|{p1._pl_hp}\nКоличество вашего ресурса - {p1._pl_res}')

    def pl_punch(self):
        if random.randint(0, 100) > 15:
            if random.randint(0, 100) >= 50:
                print('\nВы замечаете слабое место врага и наносите критический удар!\n')
                print(f'Вы наносите {p1._pl_damage * 2} урона!\n')
                m1._m_hp -= (p1._pl_damage * 2)
            else:
                print('\nВы выпускаете стрелу, ')
                print(f'Вы наносите {p1._pl_damage} урона!\n')
                m1._m_hp -= p1._pl_damage
        else:
            print('\nВы промахнулись\n')
            pass
    
    def pl_protect(self):
        print('\nВы готовы к атаке противника и будете защищаться')
        if random.randint(0, 100) > 25:
            print('Вы не смогли увернуться от атаки, в вас попали!', end=' ')
            m1.m_punch100()
        else:
            print('Вы успешно уклонились от удара\n')
    
    def pl_pass(self):
        print('\nВы ничего не делаете')
        pass    

    def pl_magic(self):
        p1._pl_res -= 25
        print('\nБлагодаря своему непревзойденному опыту вы делаете меткий выстрел в голову. Враг повержен!\n')
        m1._m_hp = 0

    def pl_lvlup(self):
        p1._pl_lvl = p1._pl_lvl + 1
        print(f'\nПоздравляем, вы подняли свой уровень! Ваш уровень - {p1._pl_lvl}')
        p1._pl_maxhp += 50
        p1._pl_hp = p1._pl_maxhp
        p1._pl_maxres +=50
        p1._pl_res = p1._pl_maxres
        p1.fight_hp_status()

    def checkmaxhp(self):
        if p1._pl_hp > p1._pl_maxhp:
            p1._pl_hp = p1._pl_maxhp

    def checkmaxres(self):
        if p1._pl_res > p1._pl_maxhp:
            p1._pl_res = p1._pl_maxhp
            

    
class Warrior(Player):
    
    def pl_punch(self):
        if random.randint(0, 100) > 15:
            if random.randint(0, 100) >= 15:
                print(f'\nВы бьете мечом!\nКритический удар!\n{m1._m_name} получает {p1._pl_damage * 2} урона!\n')
                m1._m_hp -= (p1._pl_damage * 2)
            else:
                print(f'\nВы бьете мечом \n{m1._m_name} получает {p1._pl_damage} урона!\n')
                m1._m_hp -= p1._pl_damage
        else:
            print('\nВы промахнулись\n')
            pass


    def pl_protect(self):
        print(f'\nВы готовы к атаке противника и будете защищаться\n{m1._m_name} нанес {(m1._m_damage / 3)} урона!\n')
        p1._pl_hp -= (m1._m_damage / 3)


    def pl_magic(self):
        p1._pl_res -= 25
        print(f'\nСвоей яростью вы заставляете {m1._m_name} пропустить ход!\n')

class Mage(Player):
   
    def pl_punch(self):
        if random.randint(0, 100) > 15:
            if random.randint(0, 100) >= 15:
                print(f'\nВы бьете посохом!\nКритический удар!\n{m1._m_name} получает {p1._pl_damage * 2} урона!\n')
                m1._m_hp -= (p1._pl_damage * 2)
            else:
                print(f'\nВы бьете посохом! \n{m1._m_name} получает {p1._pl_damage} урона!\n')
                m1._m_hp -= p1._pl_damage
        else:
            print('\nВы промахнулись\n')
            pass


    def pl_protect(self):
        print(f'\nВы готовы к атаке противника и будете защищаться\n{m1._m_name} нанес {(m1._m_damage / 3)} урона!\n')
        p1._pl_hp -= m1._m_damage - (m1._m_damage * 0.25)
        
    def pl_magic(self):
        p1._pl_res -= 25
        print(f'\nВы кастуете огненный шар! - {p1._pl_damage * 2.5} \n')
        m1._m_hp -= p1._pl_damage * 2.5
        if m1._m_hp <= 0:
            p1.win_instance()
            m1.m_drop()
            p1.xp_up()
            waiting()

class Archer(Player):

    def pl_punch(self):
        if random.randint(0, 100) > 15:
            if random.randint(0, 100) >= 50:
                print('\nВы замечаете слабое место врага и наносите критический удар!\n')
                print(f'Вы наносите {p1._pl_damage * 2} урона!\n')
                m1._m_hp -= (p1._pl_damage * 2)
            else:
                print('\nВы выпускаете стрелу, ')
                print(f'Вы наносите {p1._pl_damage} урона!\n')
                m1._m_hp -= p1._pl_damage
        else:
            print('\nВы промахнулись\n')
            pass


    def pl_protect(self):
        print('\nВы готовы к атаке противника и будете защищаться')
        if random.randint(0, 100) > 25:
            print('Вы не смогли увернуться от атаки, в вас попали!', end=' ')
            m1.m_punch100()
        else:
            print('Вы успешно уклонились от удара\n')


    def pl_magic(self):
        p1._pl_res -= 25
        print('\nБлагодаря своему непревзойденному опыту вы делаете меткий выстрел в голову. Враг повержен!\n')
        m1._m_hp = 0
        p1.win_instance()
        m1.m_drop()
        p1.xp_up
        waiting()



class Monster:
    def __init__(self, m_name, m_damage, m_hp, m_maxhp, m_class):
        self._m_name = m_name
        self._m_damage = m_damage
        self._m_hp = m_hp
        self._m_maxhp = m_maxhp
        self._m_class = m_class

    def m_attack(self):
        if random.randint(0, 100) >= 60:
            m1.m_punch()
        else:
            m1.m_magic()
    
    def __del__(self):
        pass

    def m_drop(self):
        if random.randint(0, 100) >= 50:
            print(f'Вы подобрали 1 {inventory.healing_potion.name} и 1 {inventory.resource_potion.name}')
            inventory.healing_potion.amount += 0
            inventory.resource_potion.amount += 0

    def m_magic(self):
        print('\nЗомби наполнился яростью и наносит несколько быстрых ударов!\n')
        m1.m_punch()
        m1.m_punch()

    def m_punch(self):
        if random.randint(0, 100) > 25:
            print(f'{m1._m_name} замахивается на вас и бьет своей полуразложившейся клешней')
            print(f'Вы получаете {m1._m_damage} урона!\n')
            p1._pl_hp -= m1._m_damage
        else:
            print(f'\n{m1._m_name} промахнулся!\n')

    def m_punch100(self):
        print(f'\n{m1._m_name} замахивается на вас и бьет своей полуразложившейся клешней')
        print(f'Вы получаете {m1._m_damage} урона!\n')
        p1._pl_hp -= m1._m_damage
            

    def m_first_strike(self):
        if random.randint(0, 100) > 70:
            print(f'\n{m1._m_name} замахивается на вас и делает первый удар!')
            print(f'Вы получаете {m1._m_damage} урона!\n')
            p1._pl_hp -= m1._m_damage
        else:
            print(f'\n{m1._m_name} промахнулся!\n')
            pass

class Zombie(Monster):
    
    def m_drop(self):
            print(f'Вы подобрали 1 {inventory.healing_potion.name} и 1 {inventory.resource_potion.name}')
            inventory.healing_potion.amount += 1
            inventory.resource_potion.amount += 1
        
    def m_attack(self):
        if random.randint(0, 100) >= 25:
            m1.m_punch()
        else:
            m1.m_magic()


        

class Lich(Monster):

    def m_drop(self):
        if random.randint(0, 100) >= 50:
            print(f'Вы подобрали 1 {inventory.healing_potion.name} и 1 {inventory.resource_potion.name}')
            inventory.healing_potion.amount += 2
            inventory.resource_potion.amount += 2

    def m_attack(self):
            if random.randint(0, 100) >= 60:
                m1.m_punch()
            else:
                m1.m_magic()

    def m_magic(self):
        print(f'\n{m1._m_name} выпускает в вас ледяную стрелу!\n')
        print(f'Вы получаете {m1._m_damage * 5} урона!\n')
        p1._pl_hp -= (m1._m_damage * 5)


    def m_punch(self):
            print(f'{m1._m_name} атакует вас!')
            print(f'Вы получаете {m1._m_damage} урона!\n')
            p1._pl_hp -= m1._m_damage

    def m_first_strike(self):
        if random.randint(0, 100) > 70:
            print(f'\n{m1._m_name} замахивается на вас и делает первый удар!')
            print(f'Вы получаете {m1._m_damage} урона!\n')
            p1._pl_hp -= m1._m_damage
        else:
            print(f'\n{m1._m_name} промахнулся!\n')
            pass

    

class Ogre(Monster):

    def m_drop(self):
        if random.randint(0, 100) >= 50:
            print(f'Вы подобрали 1 {inventory.healing_potion.name} и 1 {inventory.resource_potion.name}')
            inventory.healing_potion.amount += 3
            inventory.resource_potion.amount += 3

    def m_magic(self):
        print(f'\n{m1._m_name} ломает вам череп!\n')
        p1.game_over()


    def m_punch(self):
        if random.randint(0, 100) >= 70:
            print(f'{m1._m_name} бьет вас своей дубиной')
            print(f'Вы получаете {m1._m_damage} урона!\n')
            p1._pl_hp = p1._pl_hp - m1._m_damage
        else:
            print(f'\n{m1._m_name} промахнулся!\n')


    def m_first_strike(self):
        if random.randint(0, 100) > 70:
            print(f'\n{m1._m_name} замахивается на вас и делает первый удар!')
            print(f'Вы получаете {m1._m_damage} урона!\n')
            p1._pl_hp -= m1._m_damage
        else:
            print(f'\n{m1._m_name} промахнулся!\n')
            pass

    def m_attack(self):
        if random.randint(0, 100) >= 25:
            m1.m_punch()
        else:
            m1.m_magic()




p1 = Player(None, None, None, None, None, None, None, None, None)  # Создание экземпляра класса игрок
m1 = Monster(None, None, None, None, None)  # Создание экземпляра класса монстр



def waiting():  # Функция ожидания из которой можно что либо сделать персонажу   
    print('\n-------------------------\n1. Просмотр статуса.\n2. Открыть инвентарь\n3. Пойти в подземелье')
    return


def choose_class():   # Функция выбора класса
    print('Вы можете выбрать свой класс из предоставленных:\n')
    for _class in pl_classes:
        print(f'Класс -', _class["name"])

    while True:
        user_choice = input(f'\n1. {pl_classes[0]["name"]} 2.{pl_classes[1]["name"]} 3. {pl_classes[2]["name"]}\n-------------------------\nВведите ваш выбор: ')    # Выбор класса и присвоение экземпляру p1 нужных значений
        if user_choice == '1':
            p1.__class__ = Warrior
            p1._pl_class_name = pl_classes[0]["name"]
            p1._pl_damage = pl_classes[0]["damage"]
            p1._pl_hp = pl_classes[0]["hp"]
            p1._pl_res = pl_classes[0]["how_many_res"]
            p1._pl_lvl = pl_classes[0]["lvl"]
            p1._pl_maxhp = pl_classes[0]["hp"]
            p1._pl_maxres = pl_classes[0]["how_many_res"]
            p1._pl_xp = pl_classes[0]["xp"]
            inventory.healing_potion.amount = 1
            inventory.resource_potion.amount = 0
            p1.status()
            waiting()

        elif user_choice == '2':
            p1.__class__ = Mage
            p1._pl_class_name = pl_classes[1]["name"]
            p1._pl_damage = pl_classes[1]["damage"]
            p1._pl_hp = pl_classes[1]["hp"]
            p1._pl_res = pl_classes[1]["how_many_res"]
            p1._pl_lvl = pl_classes[1]["lvl"]
            p1._pl_maxhp = pl_classes[1]["hp"]
            p1._pl_maxres = pl_classes[1]["hp"]
            p1._pl_maxres = pl_classes[1]["how_many_res"]
            p1._pl_xp = pl_classes[1]["xp"]
            inventory.healing_potion.amount = 1
            inventory.resource_potion.amount = 1         
            p1.status()
            waiting()

        elif user_choice == '3':
            p1.__class__ = Archer
            p1._pl_class_name = pl_classes[2]["name"]
            p1._pl_damage = pl_classes[2]["damage"]
            p1._pl_hp = pl_classes[2]["hp"]
            p1._pl_res = pl_classes[2]["how_many_res"]
            p1._pl_lvl = pl_classes[2]["lvl"]
            p1._pl_maxhp = pl_classes[2]["hp"]
            p1._pl_maxres = pl_classes[2]["how_many_res"]
            p1._pl_xp = pl_classes[2]["xp"]
            inventory.healing_potion.amount = 1
            inventory.resource_potion.amount = 0
            p1.status()
            waiting()

        else:
            print('Вы ввели не те символы')
            continue
    

def fight():
        
    while True:
        if p1._pl_hp <= 0:
            p1.game_over()
        elif m1._m_hp <=0:
            p1.win_instance 
            m1.m_drop()
            p1.xp_up()
            waiting()
        else:
            p1.fight_hp_status()
            user_choice = input('\nВыберите одно действие:\n1. Обычный удар. 2. Способность персонажа. 3. Защититься. 4. Пропуск хода. \nВведите ваш выбор: ')
            print('--------------------------')
        
            if user_choice == '1':
                p1.pl_punch()
                if m1._m_hp <= 0:
                    p1.win_instance
                    m1.m_drop()
                    p1.xp_up()
                    waiting()
                m1.m_attack()
            elif user_choice == '2':
                if p1._pl_res >= 25:
                    p1.pl_magic()
                    m1.m_attack()
                else:
                    print('\nВам не хватает ресурса для использования данной способности\n')
                    continue

            elif user_choice == '3':
                p1.pl_protect()

            elif user_choice == '4':
                p1.pl_pass()
                m1.m_attack()
            else:
                print('\nВы нажали не ту кнопку!\n')
                continue
    


def dungeon():
    print(locations[0]["description"])
    
    print('\nВы заходите в темное подземелье.\nВы можете:\nИдти вглубь подземелья, или обыскать его.')
    m1.__class__ = Zombie
    m1._m_name = m_classes[0]["name"]
    m1._m_hp = m_classes[0]["hp"]
    m1._m_damage = m_classes[0]["damage"]
    m1._m_maxhp = m_classes[0]["max_hp"]
    m1._m_class = m_classes[0]["class_name"]
    while True:
        
        user_input = input('\n-------------------------\n1. Идти по подземелью.\n2. Обыскать подземелье.\n3. Вернуться обратно.\nВаш вариант выбора:  ')
        if user_input == '1':
            print('\nЭто подземелье вам кажется бесконечным, ничего не видя на своем пути вы идете дальше.\nНаконец то виден свет в конце коридора. \n')              #начинается бой с зомби Выход в другую локацию
            print(f'\nВас что-то хватает за ногу. \nПосмотрев вниз вы видите почти разложившигося мертвеца, перед вами {m1._m_name}!')
            
            m1.m_first_strike()
            fight()
            
        elif user_input == '2':
                # С шансом 20% можно найти сундук в котором будет зелье здоровья и зелье восстановления ресурса
            if random.randint(0, 100) >= 80:
                print(f'\nВы нашли сундук с сокровищами!\n В нем было 1 - {inventory.healing_potion.name}, и 1 - {inventory.resource_potion.name}')
                inventory.healing_potion.amount += 1
                inventory.resource_potion.amount += 1
                inventory.open_inventory
            else:
                print('\nК сожалению тут ничего нет, попробуйте другое место.')
                
        elif user_input == '3':
            print('\nВы решили вернуться обратно ')    
            waiting()

        else:
            print('\nВы нажали не ту кнопку\n')
            continue


def dead_forrest():
    print(f'\nВы входите в {locations[1]["name"]}')
    print('Мертвый лес является таким уже несколько сотен лет, даже ветер тут не дует.\nМожет быть тут все таки есть кто - то живой...\n\nВы можете пройти по тропе вглубь леса или обыскать местность.')
    m1.__class__ = Lich
    m1._m_name = m_classes[1]["name"]
    m1._m_hp = m_classes[1]["hp"]
    m1._m_damage = m_classes[1]["damage"]
    m1._m_maxhp = m_classes[1]["max_hp"]
    m1._m_class = m_classes[1]["class_name"]
    while True:
        user_input = input('\n-------------------------\n1. Пойти по тропе.\n2. Обыскать местность.\n3. Вернуться обратно.\nВаш вариант выбора:  ')
        if user_input == '1':
            print('\nПройдя по тропе вы выходите к старому клдбищу. Оно кажется заброшенным, а некоторые могилы разрыты.\nВы замечаете одну могилу в центре, которая сильно выделяется среди остальных, вы подходите к ней и осматриваете. ')              #начинается бой с зомби Выход в другую локацию

            print(f'\nИз могилы поднимается скелет в одежде мага. \nПеред вами с огнем в глазах стоит {m1._m_name}!')
            m1.m_first_strike()
            fight()

        elif user_input == '2':
                # С шансом 20% можно найти сундук в котором будет зелье здоровья и зелье восстановления ресурса
            if random.randint(0, 100) >= 80:
                print(f'\nВы нашли сундук с сокровищами!\n В нем было 1 - {inventory.healing_potion.name}, и 1 - {inventory.resource_potion.name}\n')
                inventory.healing_potion.amount += 1
                inventory.resource_potion.amount += 1
                inventory.open_inventory
                
            else:
                print('\nК сожалению тут ничего нет, попробуйте другое место.\n')
            
        elif user_input == '3':
            print('Вы решили вернуться обратно ')
            waiting()
           
        else:
            print('Введен не тот символ')
            continue


def curced_village():
    print(f'\nВы входите в {locations[2]["name"]}')
    print('От этой деревни отказалась империя, после того, как ее проклял лич.\nЕсть сомнение, бывал бы кто-нибудь здесь в последнее время...\nВы можете пройти внутрь деревни или обыскать здания.')
    
    while True:
        m1.__class__ = Ogre
        m1._m_name = m_classes[2]["name"]
        m1._m_hp = m_classes[2]["hp"]
        m1._m_damage = m_classes[2]["damage"]
        m1._m_maxhp = m_classes[2]["max_hp"]
        m1._m_class = m_classes[2]["class_name"]

        user_input = input('\n-------------------------\n1. Пойти вглубь деревни.\n2. Обыскать здания.\n3. Вернуться обратно.\nВаш вариант выбора:  ')
        if user_input == '1':
            print('\nДеревня призрак - это все, что приходит вам в голову, когда вы идете по ее улицам.\nПодойдя на главную площадь вы видите в ее центре огромное существо.\nПодойдя ближе существо вас замечает. \n')              #начинается бой с зомби Выход в другую локацию
            print(f'\nПеред тобой стоит {m1._m_name}!')
            m1.m_first_strike()
            fight()

        elif user_input == '2':
                # С шансом 20% можно найти сундук в котором будет зелье здоровья и зелье восстановления ресурса
            if random.randint(0, 100) >= 80:
                print(f'\nВы нашли сундук с сокровищами!\n В нем было 1 - {inventory.healing_potion.name}, и 1 - {inventory.resource_potion.name}')
                inventory.healing_potion.amount += 1
                inventory.resource_potion.amount += 1
                inventory.open_inventory
                
            else:
                print('\nК сожалению тут ничего нет, попробуйте другое место.\n')
            
        elif user_input == '3':
            print('\nВы решили вернуться обратно')
            waiting()
            
        else:
            print('\nВведен не тот символ\n')
            continue


def waiting():
    user_input = input('\n-------------------------\n1. Открыть инвентарь \n2. Просмотр статуса \n3. Отправиться в путешествие\nВведите ваш выбор: ')
    print()
    while True:
        if user_input == '1':
            while True:   
                inventory.open_inventory()           
                user_input = input('\n-------------------------\n1. Выпить зелье исцеления.\n2. Выпить зелье восстановления ресурса.\n3. Закрыть рюкзак\nВведите ваш выбор: ')
                
                if user_input == '1':
                        if p1._pl_hp < p1._pl_maxhp:  
                            p1._pl_hp += 50
                            p1.checkmaxhp()
                            inventory.healing_potion.amount -= 1
                            p1.status()
                            
                        else:
                            print(f'\nУ вас максимальное количество здоровья, использовать {inventory.healing_potion.name} нельзя! ')
                            p1.status()
                        
                elif user_input == '2':
                    if p1._pl_res < p1._pl_maxres:
                        p1._pl_res += 50     
                        p1.checkmaxres()
                        inventory.resource_potion.amount -= 1
                        p1.status()

                    else:
                        print(f'\nУ вас максимальное количество ресурса, использовать {inventory.resource_potion.name} нельзя! ')
                        p1.status()
        
                elif user_input == '3':
                    waiting()

                else:
                    print('\nВы нажали не ту кнопку!\n')
                    continue

        elif user_input == '2':
            p1.status()
            waiting()
        
        elif user_input == '3':
            travel()

        else:
            print('\nВы нажали не ту кнопку!\n')
            waiting()

def travel():
    while True:
        user_input = input(f'-------------------------\nВведите куда вы хотите отправиться\n1. {locations[0]["name"]}\n2. {locations[1]["name"]}\n3. {locations[2]["name"]}\nВведите ваш выбор: ')
        if user_input == '1':
            dungeon()
        elif user_input == '2':
            dead_forrest()
        elif user_input == '3':
            curced_village()
        else:
            print('\nВы нажали не ту кнопку!\n')        

def start_game():    # Функция начала игры
    print('Добро пожаловать в игру!')
    p1._pl_name = (input('\n-------------------------\nВведите имя вашего персонажа : '))   
    print(f'\nИмя вашего персонажа - {p1._pl_name}!\n')
    choose_class()


start_game()


