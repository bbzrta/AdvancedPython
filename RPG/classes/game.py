import random


class bcolors:
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
        print(i, end="",)
    print("")


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.maxmp = mp
        self.hp = hp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

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

    def get_spell_mp_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print("{0}:{1}".format(i, item))
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print("{0}:{1}  (cost:{2})".format(i, spell["name"], spell["mp"]))
            i += 1

