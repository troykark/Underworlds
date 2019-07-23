import json
import Races


with open('races.json') as racejson:
    RACES = json.load(racejson)

class Person:
    def __init__(self,name, hp=1, proficiency=0, speed=30,
                 b_str=8, b_dex=8, b_con=8, b_int=8, b_wis=8, b_cha=8, 
                 classes = [], npc=True, skills=[], languages =["common"], 
                 multiclass = False, level=1, xp=0,
                 race='None', charmods=[], abilities = []):
        self.name        = name
        self.hp          = hp
        self.proficiency = proficiency
        self.b_str       = b_str
        self.b_dex       = b_dex
        self.b_con       = b_con
        self.b_int       = b_int
        self.b_wis       = b_wis
        self.b_cha       = b_cha
        self.a_str       = self.b_str
        self.a_dex       = self.b_dex
        self.a_con       = self.b_con
        self.a_int       = self.b_int
        self.a_wis       = self.b_wis
        self.a_cha       = self.b_cha
        self.classes     = classes
        self.npc         = npc 
        self.skills      = skills
        self.languages   = languages
        self.multiclass  = multiclass
        self.level       = level
        self.xp          = xp
        self.charmods    = charmods
        self.race        = race
        self.abilities   = abilities
        

        if(len(classes)==0):
            self.classes.append(Monk('Monk', self, 1))
        if self.race == 'None':
            self.race = Races.Human('Human',self,'None',RACES)
        else:
            #references the class from the Races module and looks it up and uses it
            self.race = getattr(Races,self.race)(self.race,self,'None',RACES)

    def __str__(self):
        prntout = ''.join(map(str,[
                        self.name,"\n",
                        "Level: ",self.level,"\n",
                        "Race: ",self.race.name,"\n",
                        "Languages: ",self.languages,"\n",
                        "XP: ",self.xp,"\n",
                        "Str:",self.b_str," Con:",self.b_con," Dex:",self.b_dex,"\n",
                        "Int:", self.b_int," Wis:", self.b_wis," Cha:", self.b_cha,"\n"])
                        )        
        return prntout

    def updateChar(self):
        # set attributers to base

        #then apply bonuses
        for mod in self.charmods:
            mod.apply()

    def applyBonus(self, attribute, add):
        #adds bonus to attribute, inteded for Bonuses
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
        
        


class charmod():
    def __init__(self, name,permanent_bonus=True,timer=0):
        self.name = name
        self.permanent_bonus = permanent_bonus
        self.timer  = timer
    
class bonus():
    pass


def testCharacterCreation(): 
    Mi = Person('Mi')
    Mi.applyBonus( "xp", 100)
    Mi.applyBonus( "b_str", -2)
    print(Mi)
    Xi = Person('Xi',race="Dwarf")
    Xi.applyBonus( "xp", 100)
    print(Xi)



testCharacterCreation()