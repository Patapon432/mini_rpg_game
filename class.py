



class Player:
    def __init__(self, class_name, damage):
        self.class_name = class_name
        self.damage = damage

    def punch(self):
        if self.class_name == 'Archer':
            print('Вы стреляете из лука')        
        elif self.class_name == 'Warrior':
            print('Вы бьете мечом')
        elif self.class_name == 'Mage':
            print('Вы бьете посохом')
        else:
            print('Выберите класс персонажа')
    

class Monster(Player):
    def __init__(self, m_name, m_class_name, m_hp):
        self.m_name = m_name
        self.m_class_name = m_class_name
        self.m_hp = m_hp  

    def check_name(self):
        print(self.m_name)


p1 = Player('Archer', 15)
m1 = Monster('Zombie ', 'Warrior', 100)



        

m1.punch()