class Glassware:
    def __init__(self, kindofglassware):
        self.kindofglassware = kindofglassware
        print("The Lab has glassware")

class Beaker(Glassware):
    def __init__(self, thing):
        self.thing = thing
        print("There are beakers in the lab")
    def __del__(self):
        print("A beaker has shattered")
    
class Tray:
    def __init__(self):
        print("There are 5 beakers in the tray")
        self.beakers = []
        for i in range(5):
            self.beakers.append(Beaker(f"Beaker {i+1}"))
    def __del__(self):
        print("No more beakers on the tray")
tray = Tray()    
print(Tray.beakers)
tray.delete()
print(tray.beakers)
