import time
import random
items = []

# building lists


monsters = ["ghost", "mummy", "vampire"]
dwellers = ["lizzard", "serpent", "snake"]
objects = ["waffle", "toaster", "spoon"]
option2 = ["Better you'd go to another place\n ",
           "Don't seem that friendly, it's not your fight...\n ",
           "Best get out and look for the real moonster...\n"]

# building functions


def victory(message):
    print_pause("Suddenly the creature appears from nowhere \n")
    print_pause("But with your mighty object, \n")
    print_pause("you manage to slay the beast!")
    print_pause("You are victorious!")
    print_pause("Thank you for getting rid, \n")
    print_pause("of the evil in this lands!")

# defining pause message


def print_pause(message):
    print(message)
    time.sleep(2)

# defining introduction


def intro():
    print_pause("You find yourself standing in an open field, ")
    print_pause("filled with grass and yellow wildflowers.\n")
    print_pause("A wicked creature is somewhere around here ")
    print_pause("and has been terrifying the nearby village.\n")
    print_pause("The city is empty and still...")
    print_pause("The monster is said to be hiding in the forests\n")

# defining house option


def house(items):
    monster = random.choice(monsters)
    items.append("house")
    print_pause("You have entered the house")
    print_pause("Inside the house lurks a friendly..." + monster)
    print_pause("What would you like to do next?\n")
    print_pause("Please enter 1 or 2:\n")
    choice = input("1. Say hello and stay for tea\n"
                   "2. Be on your way, you got a real monster to catch\n")
    if "house" in items:
        if choice == "1":
            print_pause("Seems as if the monster was not that friendly, ")
            print_pause("good thing you got out of there fast,")
            print_pause("you should be more cautios next time...\n")
            print_pause("Maybe we should start from scratch again\n")
            ask(items)

        elif choice == "2":
            answer2 = random.choice(option2)
            print_pause(answer2)
            ask(items)
        else:
            print_pause("You should make up your mind...")
            print_pause("Sun is getting low...\n")
            house(items)

# defining cave option


def cave(items):
    dweller = random.choice(dwellers)
    object = random.choice(objects)
    items.append("cave")
    print_pause("You have entered the cave")
    print_pause("Inside there seem to be some noises from a giant " + dweller)
    print_pause("What should you do now?\n")
    print_pause("Please enter 1 or 2:\n")
    choice = input("1.Keep on going, that must be it\n"
                   "2.Best you get out, and live to tell the story\n")
    if "cave" in items:
        if choice == "1":
            print_pause("You stumble upon a mighty..." + object)
            print_pause("Would you like to take it?")
            magic = input("1. I don't need it, I got this!\n"
                          "2. Best take it,you never know...\n")
            if magic == "1":
                print_pause("A swift sound passes behind you.")
                print_pause("The monster was fast, too fast for you...\n")
                print_pause("You probably should have taken the " + object)
                play_again(items)
            elif magic == "2":
                victory(items)
                play_again(items)

        elif choice == "2":
            print_pause("No real hero runs away from adventure.")
            print_pause("Maybe you should go and check it out\n")
            cave(items)
        else:
            print_pause("Didn't get that, it's dark here in the cave, \n"
                        "say that again...")
            cave(items)

# ask if you want to play again


def play_again(items):
    items = []
    print_pause("Are thy brave enough to face the dangers again?")
    say = input("1.Yey\n"
                "2.No way\n")
    if say == "1":
        ask(items)
    elif say == "2":
        print_pause("Farewell brave warrior.")

# loop for getting back in the city


def ask(items):
    items = []
    print_pause("...Where to now?")
    print_pause("Please press 1 or 2\n")
    choice = input("1.Knock on the door to enter the house\n"
                   "2.Peer into the cave\n")
    if choice == "1":
        house(items)
    elif choice == "2":
        cave(items)
    else:
        print_pause("Didn't get that my hero, say-at again?")
        ask(items)

# grouping all functions


def play(items):
    intro()
    ask(items)

# play the game with one function


play(items)
