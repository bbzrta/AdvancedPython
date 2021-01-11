from classes.game import Person, Bcolors, separator
from classes.magic import Spell
from classes.inventory import Item
import os

# Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 120, "black")
blizzard = Spell("Blizzard", 11, 110, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 13, 300, "black")

# White Magic
cure = Spell("Cure", 12, -120, "white")
cura = Spell("Cura", 18, -200, "white")

# Items in the game
potion = Item("potion", "potion", "Heals 50 HP", -50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", -100)
superpotion = Item("SuperPotion", "potion", "Heals 500 HP", -500)
elixer = Item("Elixer", "potion", "Fully restores HP/MP", -9999)
hielixer = Item("Elixer", "potion", "Fully restores party's HP/MP", -9999)

grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hipotion, superpotion, elixer,hielixer, grenade]


# Init the player and enemy
player_name = input("Enter your name: ")
os.system("clear")

player = Person(460, 65, 60, 34, player_spells, player_items, name=player_name)
enemy = Person(1200, 65, 45, 25, [], [], "Enemy")

# Start of the Battle
print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

# Battle Loop until either opponent dies
while True:

    # Clear the terminal and output opponents' information
    os.system("clear")
    print("{0} \nBattle {1}".format(Bcolors.FAIL, Bcolors.ENDC))
    enemy.status()
    player.status()

    # Displaying available action categories
    print()
    separator("=")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    # Displaying available actions based on the category chosen by the player
    # If the player chose to Attack
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(Bcolors.OKBLUE + "\nYou attacked for {0} points of damage.".format(dmg) + Bcolors.ENDC)
    # If the player chose to use magic
    elif index == 1:
        player.choose_magic()
        mgk_choice = int(input("Choose Magic: ")) - 1
        if mgk_choice == -1:
            continue

        spell = player.magic[mgk_choice]
        mgk_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        # If not enough magic point, block the execution.
        if spell.cost > current_mp:
            input(Bcolors.FAIL + "\nNot enough MP\n" + Bcolors.ENDC)
            os.system("clear")
            continue

        player.reduce_mp(spell.cost)

        # Conditioning on the type of spell for healing and damaging spells
        if spell.type == "black":
            enemy.take_damage(mgk_dmg)
            print("{0}\n{1} deals {2} damage points.{3}".format(Bcolors.OKBLUE, spell.name, abs(mgk_dmg), Bcolors.ENDC))
        elif spell.type == "white":
            player.take_damage(mgk_dmg)
            print(
                "{0}\n{1} deals {2} healing points.{3}".format(Bcolors.OKGREEN, spell.name, abs(mgk_dmg), Bcolors.ENDC))

    # If the player chose to use an item
    elif index == 2:
        player.choose_item()
        itm_choice = int(input("Choose Item: ")) - 1
        if itm_choice == -1:
            continue

        item = player.items[itm_choice]

        if item.type == "potion":
            player.take_damage(item.prop)
            if item.prop > -9999:
                print("{0}You have healed yourself by {1} points{2}"
                      .format(Bcolors.OKGREEN, abs(item.prop), Bcolors.ENDC))
            elif item.prop <= -9999:
                print("{0}You have fully healed yourself!{1}".
                      format(Bcolors.OKGREEN, Bcolors.ENDC))




    # Stopping the player HP from overloading
    if player.hp > player.maxhp:
        player.hp = player.maxhp

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("enemy has done {0} damage to you!".format(enemy_dmg))

    # In case of a winner do:
    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + Bcolors.BOLD + "You win!" + Bcolors.ENDC)
        break
    elif player.get_hp() == 0:
        input(Bcolors.FAIL + Bcolors.BOLD + "You lose!" + Bcolors.ENDC)
        break
    # If no winners yet:
    else:
        input("\nPress Enter to continue")
        continue
