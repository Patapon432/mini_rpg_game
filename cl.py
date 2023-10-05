class GameclassInterface:
    def hit(self):
        pass
    def wait(self):
        pass
    def use_potion(self):
        pass

class War(GameclassInterface):
    def hit(self):
        print('Воин бьет мечом')
    

class Rouge(GameclassInterface):
    def hit(self):
        print('Разбойник стреляет из лука')


class Mage(GameclassInterface):
    def hit(self):
        print('Маг наносит удар посохом')