from random import random
from pokemon import Pokemon

class FlyingType(Pokemon):
    pass
class WaterType(Pokemon):
    pass
class BugType(Pokemon):
    pass
class FireType(Pokemon):
    pass
class GhostType(Pokemon):
    pass
class FairyType(Pokemon):
    pass

# Poison class by Emily Macway
class PoisonType(Pokemon):
    """ Poison Type Pokemon"""

    def __init__(self, name, trainer, hp):
        """Initialize"""
        Pokemon.__init__(self, name, trainer)
        self.basic_attack = 'poison jab'
        self.prob = 0.3
        self.hp = hp

    def __str__(self):
        return "Your Opponent's Pokemon: " + str(self.name) + "\n" + "Here are its stats: \n" + "\tTrainer: " + str(self.trainer) + "\n" + "\tType: Poison\n" + "\tHP: " + str(self.hp) + "\n" + "\tBasic Attack: " + str(self.basic_attack) + "\n" + "\tProbability of Inflicting Paralysis: " + str(self.prob)

    def attack(self, other):
        """Override Attack for specific Poison Type"""
        if isinstance(self, PoisonType):
            if not self.paralyzed:
                self.speak()
                print(self.name, ' used ', self.basic_attack, '!')
                if isinstance(other, GrassType) or isinstance(other, FairyType):
                    other.receive_damage(self.damage*2)
                if isinstance(other, PoisonType) or isinstance(other, GhostType):
                    other.receive_damage(self.damage*0.5)
                else:
                    other.receive_damage(self.damage)
            if random() < self.prob and type(other) != PoisonType:
                print(other.name, 'is poisoned')

class GrassType(Pokemon):

    def __init__(self, name, trainer, hp):
        Pokemon.__init__(self, name, trainer)
        self.basic_attack = 'stun spore'
        self.prob = 1
        self.hp = hp

    def __str__(self):
        return "Your Opponent's Pokemon: " + str(self.name) + "\n" + "Here are its stats: \n" + "\tTrainer: " + str(self.trainer) + "\n" + "\tType: Grass\n" + "\tHP: " + str(self.hp) + "\n" + "\tBasic Attack: " + str(self.basic_attack) + "\n" + "\tProbability of Inflicting Paralysis: " + str(self.prob)

    def attack(self, other):
        if isinstance(other, WaterType):
            if not self.paralyzed:
                self.speak()
                print(self.name, ' used ', self.basic_attack, '!')
                other.receive_damage(self.damage * 2)
        elif isinstance(other, (FlyingType, PoisonType, BugType, FireType, GrassType)):
            if not self.paralyzed:
                self.speak()
                print(self.name, ' used ', self.basic_attack, '!')
                other.receive_damage(self.damage * 0.5)
        else:
            super().attack(other)
        if random() < self.prob and type(other) != GrassType:
            other.paralyzed = True
            print(other.name + ' is paralyzed!')
