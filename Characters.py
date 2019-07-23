import json

with open('races.json') as racejson:
    RACES = json.load(racejson)

class Person:
    def __init__(self,name, hp=1, proficiency=0, speed=30,
                 a_str=8, a_dex=8, a_con=8, a_int=8, a_wis=8, a_cha=8, 
                 classes = [], npc=True, skills=[], languages =["common"], 
                 multiclass = False, level=1, xp=0,
                 race='None', charmods=[]):
        self.name        = name
        self.hp          = hp
        self.proficiency = proficiency
        self.a_str       = a_str
        self.a_dex       = a_dex
        self.a_con       = a_con
        self.a_int       = a_int
        self.a_wis       = a_wis
        self.a_cha       = a_cha
        self.classes     = classes
        self.npc         = npc 
        self.skills      = skills
        self.languages   = languages
        self.multiclass  = multiclass
        self.level       = level
        self.xp          = xp
        self.charmods    = charmods
        self.race        = race
        if(len(classes)==0):
            self.classes.append(Monk('Monk', self, 1))
        if self.race == 'None':
            self.race = Human('Human',self,'None',RACES)

    def __str__(self):
        prntout = ''.join(map(str,[
                        self.name,"\n",
                        "Level: ",self.level,"\n",
                        "Race: ",self.race.name,"\n",
                        "Languages: ",self.languages,"\n",
                        "XP: ",self.xp,"\n",
                        "Str:",self.a_str," Con:",self.a_con," Dex:",self.a_dex,"\n",
                        "Int:", self.a_int," Wis:", self.a_wis," Cha:", self.a_cha,"\n"])
                        )        
        return prntout

    def updateChar(self):
        # set attributers to base

        #then apply bonuses
        for mod in self.charmods:
            mod.apply()

    def applyBonus(self, attribute, add):
        setattr(self, attribute, (getattr(self,attribute) + add))
    
        

class characterClass:
    def __init__(self, name, character, level, startingclass=True, 
                 initialLevel=True,):
        self.name = name 
        self.character = character
        self.level = level
        self.startingclass = startingclass
        self.initialLevel  = initialLevel
        self.abilities = []
        self.subClass = None
        self.activeAbilities = []
        self.passiveAbilities = []
        if initialLevel == True:
            self.initializeClass()
            self.initialLevel = False

class Monk(characterClass):
    def initializeClass(self):
        self.character.ki    = 0
        self.character.maxki = 0
        
        
class Race():
    def __init__(self, name, character, subrace, table):
        self.name = name 
        self.subrace = subrace
        self.character = character
        self.bonusarray = table[self.name]["AttributeBonuses"]
        self.character.a_cha += self.bonusarray["cha"]
        self.character.a_con += self.bonusarray["con"]
        self.character.a_dex += self.bonusarray["dex"] 
        self.character.a_int += self.bonusarray["int"]
        self.character.a_str += self.bonusarray["str"]
        self.character.a_wis += self.bonusarray["wis"]
        self.character.languages = table[self.name]["Languages"]
        self.initializeRace()
        
        
class Human(Race):
    def initializeRace(self):
        pass

class charmod():
    def __init__(self, name,permanent_bonus=True,timer=0):
        self.name = name
        self.permanent_bonus = permanent_bonus
        self.timer  = timer
    
class bonus():
    pass


Mi = Person('Mi')


print(Mi.xp)
Mi.applyBonus( "xp", 100)
Mi.applyBonus( "a_str", -2)

print(Mi)