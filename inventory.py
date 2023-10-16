
import types


# class Inventory:
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount
#         amount = 0


# healing_potion = Inventory('Зелье исцеления', 10)
# resource_potion = Inventory('Зелье восстановления ресурса', 10)   


# def open_inventory():
#         print(f'\n{healing_potion.name} - количество: {healing_potion.amount}\n{resource_potion.name} - количество: {resource_potion.amount}')
        


class Item:
    def __init__(self, name, value):
          self.__name = name
          self.__value = value

    def get_name(self) -> str:
        return self.__name
    
    def get_value(self) -> int:
        return self.__value

    def inscrice_value(self, number: int = 1) -> int:
        self.__value += number

    def use_item(self, number: int = 1) -> int:
        if not self.__value: 
            self.__value -= number
        
        return self.__value

class Bag:
    items: list[Item] = []

    def __init__(self, item: Item = None):
        if item:
            self.items.append(item)

    def add_item(self, item: Item):
        for i in self.items:
            if i.get_name() == item.get_name():
                i.inscrice_value()
                return True
        self.items.append(item)
        return True   

    def use_item(self, item: Item):
        new_bag: list[Item] = []
        print(f'Использую {item.get_name()}\n')

        for i in self.items:
            if i.get_name() == item.get_name():
                i.use_item()
            if i.get_value() > 0:
                new_bag.append(i)
        self.items = new_bag

    def open_inventory(self):
        count: int = 1
        for i in self.items:
            print(f"Нажмите {count} чтобы использовать {i.get_name()} : {i.get_value()}\n") 
            count += 1       
        # print(f"Нажмите {count + 1}")

heal_potion = Item('heal_potion', 1)
mana_potion = Item('mana_potion', 1)
bag = Bag()
bag.add_item(mana_potion)
bag.add_item(mana_potion)
bag.open_inventory()
bag.use_item(mana_potion)
bag.open_inventory()

         
    