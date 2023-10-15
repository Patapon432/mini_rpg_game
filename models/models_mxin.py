

class AbstractClaas:
    name: str = None
    exp: int = 100
    
    def her(self):
        print("Hui")

class Player(AbstractClaas):
    def __init__(self) -> None:
        self.name = "Pipa"


a = Player()

print("__")
a.her()

