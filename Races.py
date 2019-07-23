class Race():
    def __init__(self, name, character, subrace, table):
        self.name = name 
        self.subrace = subrace
        self.character = character
        self.bonusarray = table[self.name]["attributeBonuses"]
        self.character.b_cha += self.bonusarray["cha"]
        self.character.b_con += self.bonusarray["con"]
        self.character.b_dex += self.bonusarray["dex"] 
        self.character.b_int += self.bonusarray["int"]
        self.character.b_str += self.bonusarray["str"]
        self.character.b_wis += self.bonusarray["wis"]
        self.character.languages = table[self.name]["languages"]
        self.initializeRace()
        
        
class Human(Race):
    def initializeRace(self):
        pass

class Dwarf(Race):
    def initializeRace(self):
        pass

class HalfElf(Race):
    def initializeRace(self):
        pass

class HalfOrc(Race):
    def initializeRace(self):
        pass

class Elf(Race):
    def initializeRace(self):
        pass

class Halfling(Race):
    def initializeRace(self):
        pass
        
class Tiefling(Race):
    def initializeRace(self):
        pass