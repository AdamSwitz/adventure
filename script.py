import random

# TODO: Add enemies
# TODO: Add chests. Random chance for weapon (strength), scroll (accuracy) potion, spider bite (poison), rat (damage), key (key can only be obtained once)
# TODO: Add boss room, randomly selected on startup, requires player.has_key to be true.
# TODO: Add boss room check to movement
# TODO: Add random encounter selector - if room is visited, just print("You have already visited this room")
# TODO: Add stats screen on death
# make enemy health global variable. change check_in_combat to check if enemy health > 0.
# On enemy encounter, add 5 + player.combat_count to enemy health. Check enemy health after each turn.
# make enemy strength global variable. Something like 2 + player.combat_count
# TODO: Add attacks for player and enemy. Check whether attack hits based on accuracy, if so, deal damage as rand int between 1 and player/enemy.strength
# fuck it just make an enemy class.


map = [["a1", "a2"],["b1", "b2"],["c1","c2"]]
x_coordinate = 1
y_coordinate = 0
boss_room = ""
visited_rooms = []

class player_class:
    name = ""
    health = 10
    strength = 3
    accuracy = 80
    has_key = False
    potions = 1
    in_combat = False
    combat_count = 0
    location = map[x_coordinate][y_coordinate]
    poison = 0

player = player_class()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def check_in_combat():
    if player.in_combat:
        combat_prompt
    else:
        move_player
#if player.in_combat

def check_player_health():
    if player.health <= 0:
        print("You Died\nGame Over.")
        input("Press enter to continue.")
        restart_program

def use_potion():
    if player.potions > 0:
        player.health += 5
        player.potions -= 1
    else:
        print("You don't have any potions!")
    check_in_combat


def generate_boss_room():
    boss_room = map[random.randint(0, len(map) - 1)][0, len(map[0])]

def append_to_visited():
    visited_rooms.append(player_location)

def check_if_visited():
    if player_location in visited_rooms:
        print("You have already visited this room.")
        move_player
    elif player_location == boss_room:
        if player.has_key:
            yn = lower(input("The key you found seems to fit this lock. Do you wish to enter? (Y/N) "))
            if yn == y or yn == yes:
                boss_encounter
            elif yn == n or yn == no:
                move_player
    else:
        append_to_visited
        random_encounter

def move_player():
    direction = input("Which direction would you like to move (N,E,S,W)? ")
    direction = lower(direction)
    if direction == "n" or direction == "north":
        y_coordinate += 1
        if y_coordinate > len(map[x_coordinate]):
            print("A wall blocks your path.")
            y_coordinate -= 1
    elif direction == "s" or direction == "south":
        y_coordinate -= 1
        if y_coordinate < 0:
            print("A wall blocks your path.")
            y_coordinate += 1
    elif direction == "e" or "east":
        x_coordinate += 1
        if x_coordinate > len(map):
            print("A wall blocks your path.")
            x_coordinate -= 1
    elif direction == "w" or "west":
        x_coordinate -= 1
        if x_coordinate < 0:
            print("A wall blocks your path")
            x_coordinate += 1
    else:
        print("Please enter a valid direction (N,E,S,W)")
        move_player
