"""
Shunan Zhu
Foothill College, CS3B, Summer 2022
Project 3 - Pokemon Game
8-1-2022
"""

from random import random, randrange
from pokemon import Pokemon
from pokemonTypeClasses import *
from pokeGame import PokeGame

def main():
    match = PokeGame()
    valid_types_menu = ["Grass", "Poison"]

    for i in range(1, 8):
        print(f"\nRound {i}:")
        opponent_pokemon = match.drawPokemon()
        print("Menu: Valid Types to Choose From: ")
        for j in range(0, len(valid_types_menu)):
            print(valid_types_menu[j])

        poke_type = input("Choose a type: ")
        name = input("Choose a name for your Pokemon: ")
        trainer = input("Input your name as the trainer: ")
        hp = input("Input HP of your Pokemon: ")

        if poke_type.lower() == "grass":
            user_pokemon = GrassType(name, trainer, hp)
            while opponent_pokemon.hp != 0:
                user_pokemon.attack(opponent_pokemon)
        elif poke_type.lower() == "poison":
            user_pokemon = PoisonType(name, trainer, hp)
            while opponent_pokemon.hp != 0:
                user_pokemon.attack(opponent_pokemon)
        else:
            print("You are disqualified: Invalid Input")

if __name__ == "__main__":
    main()
