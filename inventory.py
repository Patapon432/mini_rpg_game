



class Inventory:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        amount = 0


healing_potion = Inventory('Зелье исцеления', 10)
resource_potion = Inventory('Зелье восстановления ресурса', 10)   


def open_inventory():
        print(f'\n{healing_potion.name} - количество: {healing_potion.amount}\n{resource_potion.name} - количество: {resource_potion.amount}')
        


class Item:
     def __init__(self, name, value):
          self.name = name
          self.value = value

class bag:
    items = []

    def __init__(self, item: Item = None):
        if item:
            self.items.append(item)

#     def add_item(self, item: Item)
         
    