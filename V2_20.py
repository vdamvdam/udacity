import time

import sys

import random


# 1 sec pause is made after the text is printed
def print_pause(message):
    print(message)
    time.sleep(1)


# Description to the player of what is happening
def intro():
    print_pause("2020 is weird. Fauci is vaccinating Santa."
                "Monoliths everywhere.")
    print_pause("Space People are Guardians? Something like that.")
    print_pause("But who cares. You are hungry. It is 9pm.")
    print_pause("There are rumors that the curfew is because "
                "strange creatures come out at night.")
    print_pause("You head out anyway, but you grab some essentials "
                "first (besides your mask of course).")


# Validation of the player's input
def valid_input(message, options):
    while True:
        response = input(message).lower()
        for option in options:
            if option in response:
                response = option
                return response
        print_pause("Sorry, pick again.")


# Different scenarios based on the previous choice in case
# the player meets zombie Karens
def zombie_Karens(item, play_again_list):
    if item == "baseball bat":
        print_pause("Zombie Karens come closer.")
        print_pause("You take a good swig with your bat")
    else:
        if item == "pepper spray":
            print_pause("Your pepper spray isn't effective. "
                        "She also has a matching one.")
        elif item == "bag":
            print_pause("She says your bag is ugly."
                        "Even when they are near dead, these"
                        "Karens keep going.")
        print_pause("Oh no. Zombie Kevins. They can hear you too. "
                    "They start climbing onto you.")
        print_pause("You lost! You didn't manage to reach your home.")
        play_again(play_again_list)


# Different scenarios based on the previous choice in case
# the player meets superspreaders
def superspreaders(item, play_again_list):
    if item == "pepper sprays":
        print_pause("With your pepper spray you spray directly "
                    "at the superspreaders faces.")
        print_pause("All superspreaders died! You push through, "
                    "grabs a fried chicken, and head home.")
    elif item == "baseball bat" or item == "bag":
        print_pause("Your stomach gets louder!")
        print_pause("You start regretting your life."
                    "They start spitting their salvia at you "
                    "and you don't make it out.")
        play_again(play_again_list)


# Different scenarios based on the previous choice in case
# the player meets politicians
def politicians(item, play_again_list):
    if item == "bag":
        print_pause("You suffocate the politicians with the "
                    "bag. You demand your stimulus checks.")
        print_pause("You suffocated the main politicians. The "
                    "others fear you and you grab a fried chicken.")
    elif item == "baseball bat" or item == "pepper spray":
        print_pause("This wasn't effective against politicans!")
        print_pause("You lost! You get lost in the group of politicans."
                    "You won't come ever get back home.")
        play_again(play_again_list)


# The player uses the item in their bag against the enemy
def action_1(enemy, item, items_trunk, play_again_list, obstacles):
    # obstacles are not repeating during one game
    obstacles.remove(enemy)
    if enemy == "zombie Karens":
        zombie_Karens(item, play_again_list)
    elif enemy == "superspreaders":
        superspreaders(item, play_again_list)
    elif enemy == "politicians":
        politicians(item, play_again_list)
    print_pause("You need a new weapon to save yourself.")
    items_trunk.append(item)


# The player exchanges current item
def action_2(enemy, item, items_trunk, play_again_list, obstacles):
    print_pause("You are back your beat up Honda Civic.")
    print_pause(f"Which item do you want to exchange {item} for?\n")
    items_trunk.append(item)
    print_pause(f" - {items_trunk[0].capitalize()}\n"
                f" - {items_trunk[1].capitalize()}\n")
    item = valid_input("Please, enter a name of the item.\n", items_trunk)
    print_pause(f"You put {item} in your car and return to the {enemy}.")
    items_trunk.remove(item)
    action_1(enemy, item, items_trunk, play_again_list, obstacles)


# The player returns to car  and has to pick an item from
# the ["baseball bat", "pepper spray", "bag"] list
def find_trunk(items_trunk):
    print_pause("What is your trusty tool to keep you safe?")
    print_pause("Your stomach is grumbling.")
    print_pause("Which one sounds the best?\n")
    print_pause(f" - {items_trunk[0].capitalize()}\n"
                f" - {items_trunk[1].capitalize()}\n"
                f" - {items_trunk[2].capitalize()}\n")
    item = valid_input("Baseball bat, pepper spray, or bag.\n", items_trunk)
    print_pause(f"You decide to do pick {item} .")
    items_trunk.remove(item)
    return item


# The player is given a choice of two actions after meeting an enemy:
# to use an item against the enemy
# or to return to the trunk and pick another item.
def meet_enemy(item, items_trunk, actions, play_again_list, obstacles):
    # Enemy is chosen in a random order
    enemy = random.choice(obstacles)
    print_pause(f"Suddenly, you've been approached by a bunch of {enemy}.")
    print_pause("What's your next step?\n")
    print_pause(f" 1. Get your {item} out of the bag.\n"
                " 2. Run back to the car to pick another item.\n")
    action = valid_input("Please enter a number 1 or 2.\n", actions)
    if action == '1':
        action_1(enemy, item, items_trunk, play_again_list, obstacles)
    elif action == '2':
        action_2(enemy, item, items_trunk, play_again_list, obstacles)


# After the game is over, the user can play the game again
def play_again(play_again_list):
    print_pause("Would you like to play again?")
    response = valid_input("Please, enter yes or no.\n", play_again_list)
    if response == "yes":
        print_pause("Great! Restarting now...\n")
        play_game()
    elif response == "no":
        sys.exit()


def game_body(items_trunk, obstacles, actions, play_again_list):
    while len(obstacles) != 0:
        item = find_trunk(items_trunk)
        meet_enemy(item, items_trunk, actions, play_again_list, obstacles)
    print_pause("Congratulatons!")
    print_pause("You are not hungry anymore. Now go get some sleep!")
    play_again(play_again_list)


def play_game():
    items_trunk = ["baseball bat", "pepper spray", "bag"]
    obstacles = ["zombie Karens", "superspreaders", "politicians"]
    actions = ['1', '2']
    play_again_list = ["yes", "no"]
    intro()
    game_body(items_trunk, obstacles, actions, play_again_list)


play_game()
