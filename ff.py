class Nucleus:
    def __init__(self):
        print("Nucleus created")
    def __del__(self):
        print("Nucleus is gone")

class Mitochondria:
    def __init__(self):
        print("Mitochondria created")
    def __del__(self):
        print("Mitochondria is gone")
    def powerthecell(self):
        print("Mitochondria is providing energy")

class Cell:
    def __init__(self):
        print("Cell created")
        self.nucleus = Nucleus()
        self.mitochondria = Mitochondria()
    def exist(self):
        print("Cell is existing")
        self.mitochondria.powerthecell()
    def __del__(self):
        del self.nucleus
        del self.mitochondria
        print("Cell is gone")

cellatwork = Cell()
cellatwork.exist()
del cellatwork
