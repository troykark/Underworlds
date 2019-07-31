class characterClass(object):
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
        self.attacks = 1
        self.classTable = classtable[self.name]
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
    def __init__(self, name, character, classtable, level=1, isstartingclass=True, 
                 initialLevel=True,hitdicetype= 6):
        super().__init__(name, character, classtable, level, isstartingclass, 
                 initialLevel,hitdicetype)
        self.character.secondwind = 1
        self.character.fightingstyle = None 
        self.character.indomitable = 0
        
        
    def initializeClass(self):
        self.updateClass()

    def updateClass(self):
        self.abilities = []
        for level in range(self.level):
            self.abilities.extend(self.classTable["levels"][str(level + 1)]["abilities"])
        self.attacks =  self.classTable["levels"][str(self.level)]["features"]["attacks"]
    def getClassHp(self):
        return self.hitdicetype * self.level 