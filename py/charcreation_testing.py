# define the race class
class Race:
    def __init__(self, name, desc, attrModifier):
        self.name = name
        self.desc = desc
        self.attrModifier = attrModifier

class Class:
    def __init__(self, name, desc, level, profic, hd):
        self.name = name
        self.desc = desc
        self.level = level
        self.profic = profic
        self.hd = hd

classFighter = Class("Fighter", "Oonga boonga", 1, 2, "1d10")

# define all the race objects
raceHuman = Race("Human", "Is p chill", [1, 1, 1, 1, 1, 1])
raceElf = Race("Elf", "Is p gay", [0, 2, 0, 0, 0, 0])
raceDwarf = Race("Dwarf", "Is dwarf", [0, 0, 2, 0, 0, 0])
races = [raceHuman, raceElf, raceDwarf]

print("1. " + raceHuman.name + "\t" + raceHuman.desc)
print("2. " + raceElf.name + "\t\t" + raceElf.desc)
print("3. " + raceDwarf.name + "\t" + raceDwarf.desc)

raceSelection = input("Select a race (1, 2 or 3) ")

if raceSelection == "1":
    charRace = raceHuman
    print("You have chosen " + charRace.name)
elif raceSelection == "2":
    charRace = raceElf
    print("You have chosen " + charRace.name)
elif raceSelection == "3":
    charRace = raceDwarf
    print("You have chosen " + charRace.name)
else:
    print("lol")

