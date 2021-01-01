from classes.game import Person, bcolors, separator
from classes.magic import spell
import os

# Black Magic
fire = spell("Fire", 10, 100, "black")
thunder = spell("Thunder", 12, 120, "black")
blizzard = spell("Blizzard", 11, 110, "black")
meteor = spell("Meteor", 20, 200, "black")
quake = spell("Quake", 13, 300, "black")

# White Magic
cure = spell("Cure", 12, -120, "white")
cura = spell("Cura", 18, -200, "white")

# Init the player and enemy
player_name = input("Enter your name: ")
os.system("clear")

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura], name=player_name)
enemy = Person(1200, 65, 45, 25, [], "Enemy")

# Start of the Battle
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

# Battle Loop until either opponent dies
while True:

    # Clear the terminal and output opponents' information
    os.system("clear")
    print("{0} \nBattle {1}".format(bcolors.FAIL, bcolors.ENDC))
    enemy.status()
    player.status()

    # Displaying available action categories
    print()
    separator("=")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    # Displaying available actions based on the category chosen by the player
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKBLUE + "\nYou attacked for {0} points of damage.".format(dmg) + bcolors.ENDC)

    elif index == 1:
        player.choose_magic()
        mgk_choice = int(input("Choose Magic: ")) - 1

        spell = player.magic[mgk_choice]
        mgk_dmg = spell.generate_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            input(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            os.system("clear")
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "black":
            enemy.take_damage(mgk_dmg)
            print(bcolors.OKBLUE + "\n{0} deals {1} points of damage".format(spell.name, mgk_dmg) + bcolors.ENDC)
        elif spell.type == "white":
            player.take_damage(mgk_dmg)
            if player.hp > player.maxhp:
                player.hp = player.maxhp

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You win!" + bcolors.ENDC)
        break
    elif player.get_hp() == 0:
        input(bcolors.FAIL + bcolors.BOLD + "You lose!" + bcolors.ENDC)
        break
    else:
        input("\nPress Enter to continue")
        continue
