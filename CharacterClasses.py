class characterClass:
    def __init__(self, name, character, classtable, level=1, isstartingclass=True, 
                 initialLevel=True,hitdicetype= 6):
        self.name = name 
        self.character = character
        self.level = level
        self.isstartingclass = isstartingclass
        self.initialLevel  = initialLevel
        self.abilities = []
        self.subClass = None
        self.activeAbilities = []
        self.passiveAbilities = []
        self.reactionAbilities = []
        self.savingthrowprofs = classtable[self.name]["SavingThrows"]["Str"]
        self.hitdicetype = classtable[self.name]["HitDiceType"] 
        if initialLevel == True:
            self.initializeClass()
            self.initialLevel = False
    def __str__(self):
        prntout = ''.join(map(str,[
                        self.name,": ", self.level]))
        return prntout
class Monk(characterClass):
    def initializeClass(self):
        self.character.ki    = 0
        self.character.maxki = 0

class Fighter(characterClass):
    def initializeClass(self):
        pass