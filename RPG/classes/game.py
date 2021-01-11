import random
from .magic import Spell


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def separator(i):
    for item in range(20):
        print(i, end="", )
    print("")


class Person:
    def __init__(self, hp, mp, atk, df, magic, items, name):
        self.maxhp = hp
        self.maxmp = mp
        self.hp = hp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxhp

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

# ----------Actions----------
    def choose_action(self):
        i = 1
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Actions" + Bcolors.ENDC)
        for item in self.actions:
            print("{0}:{1}".format(i, item))
            i += 1

    def choose_magic(self):
        i = 1
        print("{0}\nMagic{1}".format(Bcolors.OKBLUE, Bcolors.ENDC))
        for x in self.magic:
            print("{0}:{1}  (cost:{2})".format(i, x.name, x.cost, x.type))
            i += 1
        print("\n{0}{1}0: Main Menu{2}".format(Bcolors.FAIL, Bcolors.BOLD, Bcolors.ENDC))
        
    def choose_item(self):
        i = 1
        print("{0}\nItems{1}".format(Bcolors.OKBLUE, Bcolors.ENDC))
        for x in self.items:
            print("{0}:{1}  \n{2}\n".format(i, x.name, x.description, x.prop))
            i += 1
        print("\n{0}{1}0: Main Menu{2}".format(Bcolors.FAIL, Bcolors.BOLD, Bcolors.ENDC))
# ---------------------------

    def reduce_mp(self, i):
        self.mp -= i

    def status(self):
        separator("_")
        print("{0} HP: {1} {2} / {3} {4}".format(self.name, Bcolors.FAIL, self.get_hp(), self.maxhp, Bcolors.ENDC))
        print("{0} MP: {1} {2} / {3} {4}".format(self.name, Bcolors.FAIL, self.get_mp(), self.maxmp, Bcolors.ENDC))
