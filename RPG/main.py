from classes.game import Person, bcolors, separator

magic = [{"name": "Fire", "cost": 30, "dmg": 60},
         {"name": "Thunder", "cost": 15, "dmg": 50},
         {"name": "Blizzard", "cost": 15, "dmg": 50}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while True:
    separator("=")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        input("\nYou attacked for {0} points of damage. Enemy HP: {1}".format(dmg, enemy.get_hp()))

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You win!" + bcolors.ENDC)
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You lose!" + bcolors.ENDC)
    
