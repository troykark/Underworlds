class characterClass:
    def __init__(self, name, character, level=1, isstartingclass=True, 
                 initialLevel=True,):
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