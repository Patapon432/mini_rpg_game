



class Inventory:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        amount = 0


healing_potion = Inventory('Зелье исцеления', 10)
resource_potion = Inventory('Зелье восстановления ресурса', 10)   


def open_inventory():
        print(f'{healing_potion.name} - количество: {healing_potion.amount}\n{resource_potion.name} - количество: {resource_potion.amount}')
        