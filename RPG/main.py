from classes.game import Person, bcolors, separator
import os

magic = [{"name": "Fire", "cost": 30, "dmg": 60},
         {"name": "Thunder", "cost": 15, "dmg": 50},
         {"name": "Blizzard", "cost": 15, "dmg": 50}]

player_name = input("Enter your name: ")
os.system("clear")

player = Person(460, 65, 60, 34, magic, name=player_name)
enemy = Person(1200, 65, 45, 25, magic, "Enemy")

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while True:
    print("{0} \nBattle {1}".format(bcolors.FAIL, bcolors.ENDC))
    enemy.status()
    player.status()
    print()
    separator("=")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKBLUE + "\nYou attacked for {0} points of damage.".format(dmg) + bcolors.ENDC)

    elif index == 1:
        player.choose_magic()
        mgk_choice = int(input("Choose Magic: "))
        mgk_choice -= 1
        mgk_dmg = player.generate_spell_damage(mgk_choice)
        mgk_spell = player.get_spell_name(mgk_choice)
        mgk_cost = player.get_spell_mp_cost(mgk_choice)

        current_mp = player.get_mp()
        if mgk_cost > current_mp:
            input(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            os.system("clear")
            continue

        player.reduce_mp(mgk_cost)
        enemy.take_damage(mgk_dmg)
        print(bcolors.OKBLUE + "\n{0} deals {1} points of damage".format(mgk_spell, mgk_dmg) + bcolors.ENDC)

    input("\nPress Enter to continue")
    os.system("clear")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You win!" + bcolors.ENDC)
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You lose!" + bcolors.ENDC)
