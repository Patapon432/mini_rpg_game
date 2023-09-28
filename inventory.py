



# class Inventory:
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount
#         amount = 0


# healing_potion = Inventory('Зелье исцеления', 10)
# resource_potion = Inventory('Зелье восстановления ресурса', 10)   


# def open_inventory():
#         print(f'\n{healing_potion.name} - количество: {healing_potion.amount}\n{resource_potion.name} - количество: {resource_potion.amount}')
        


# class Item:
#      def __init__(self, name, value):
#           self.name = name
#           self.value = value

# class bag:
#     items = []

#     def __init__(self, item: Item = None):
#         if item:
#             self.items.append(item)

#     def add_item(self, item: Item):
#         find_item = None
#         for i in item.name:
#             find_item = i
#             i.value += item.value
#             return
         
#     def use_item(self, item: Item):
#         new_bag = []
#         for i in self.items:
#             if i.name == item.name:
#                 i.value -= item.value
#             if i.value > 0:
#                 new_bag.append(i)
#         self.items = new_bag

#     def open_inventory(self):
#         return self.items


# healpotion = Item('healpotion', 1)
# # bag.open_inventory()
         
    