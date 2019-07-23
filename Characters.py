import json
import Races
import CharacterClasses as chrclasses
import dice 

with open('races.json') as racejson:
    RACES = json.load(racejson)

with open('classes.json') as classjson:
    CLASSES = json.load(classjson)

class Person:
    def __init__(self,name, hp=1, proficiency=0, speed=30,
                 b_str=8, b_dex=8, b_con=8, b_int=8, b_wis=8, b_cha=8,
                 npc=True, 
                 multiclass = False, level=1, xp=0,
                 race='None', randomStats = False,
                 startingclass='None',
                 combat_x = 0, combat_y = 0):
        self.name            = name
        self.hp              = hp
        self.proficiency     = proficiency
        self.b_str           = b_str
        self.b_dex           = b_dex
        self.b_con           = b_con
        self.b_int           = b_int
        self.b_wis           = b_wis
        self.b_cha           = b_cha
        self.classes         = []
        self.npc             = npc 
        self.skills          = []
        self.languages       = ["common"]
        self.multiclass      = multiclass
        self.level           = level
        self.xp              = xp
        self.charmods        = []
        self.race            = race
        self.abilities       = []
        self.startingclass   = startingclass
        self.levelup         = False
        self.combat_loc      = (combat_x, combat_y)
        if randomStats:
            self.b_str = dice.statarray()
            self.b_dex = dice.statarray()
            self.b_con = dice.statarray()
            self.b_int = dice.statarray()
            self.b_wis = dice.statarray()
            self.b_cha = dice.statarray()
        self.a_str       = self.b_str
        self.a_dex       = self.b_dex
        self.a_con       = self.b_con
        self.a_int       = self.b_int
        self.a_wis       = self.b_wis
        self.a_cha       = self.b_cha

        if(self.startingclass != "None"):
            #self.classes.append(chrclasses.Fighter('Fighter', self, CLASSES))
            self.classes.append(getattr(chrclasses,self.startingclass)(self.startingclass,self,CLASSES))
        if self.race == 'None':
            self.race = Races.Race('Human', self, RACES)
        else:
            #references the class from the Races module and looks it up and uses it
            #self.race = getattr(Races,self.race)(self.race,self,'None',RACES)
            self.race = Races.Race(self.race, self,RACES)

    def __str__(self):
        prnclasses = []
        for chrclass in self.classes:
            prnclasses.append(str(chrclass))
        prntout = ''.join(map(str,[
                        self.name,"\n",
                        "Level: ",self.level,"\n",
                        "Classes: ", prnclasses,"\n",
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
    
    Xi = Person('Xi',race="Dwarf",randomStats=True)
    Xi.applyBonus( "xp", 100)
    print(Xi)

    Gi = Person('Gi',race="HillDwarf",startingclass="Fighter",randomStats=True)
    Gi.applyBonus( "xp", 100)
    print(Gi)

    Wi = Person('Wi',race="Elf",startingclass="Monk",randomStats=True)
    Wi.applyBonus( "xp", 700)
    print(Wi)

    Li = Person('Li',race="Tiefling",startingclass="Monk",randomStats=True)
    Li.applyBonus( "xp", 700)
    print(Li)

testCharacterCreation()