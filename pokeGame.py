from random import randrange
from pokemonTypeClasses import *

class PokeGame:
    def __init__(self):
        self.game_master = self.setup()

    def setup(self):
        poke_list = []
        grass1 = GrassType('Bulbasaur', 'Ash', 60)
        grass2 = GrassType('Turtwig', 'Misty', 70)
        grass3 = GrassType('Treeko', 'Brock', 70)
        grass4 = GrassType('Chikorita', 'May', 60)
        poison1 = PoisonType('Arbok', 'Jessie', 90)
        poison2 = PoisonType('Koffing', 'James', 80)
        poison3 = PoisonType('Muk', 'Professor Oak', 200)
        poke_list.append(grass1)
        poke_list.append(grass2)
        poke_list.append(grass3)
        poke_list.append(grass4)
        poke_list.append(poison1)
        poke_list.append(poison2)
        poke_list.append(poison3)
        return poke_list

    def drawPokemon(self):
        if len(self.game_master) > 0:
            selected_pokemon = self.game_master.pop(randrange(0, len(self.game_master)))
            print(selected_pokemon)
            return selected_pokemon
        else:
            print("Game Over")
            return False
