import numpy as np

# define the race class
class Race:
    def __init__(self, name, desc, attrModifier):
        self.name = name
        self.desc = desc
        self.attrModifier = attrModifier

# define all the separate races
raceHuman = Race("Human", "Is p chill", [1, 1, 1, 1, 1, 1])
raceElf = Race("Elf", "Is p gay", [0, 2, 0, 0, 0, 0])
raceDwarf = Race("Dwarf", "Is dwarf", [0, 0, 2, 0, 0, 0])
races = [raceHuman, raceElf, raceDwarf]

print("--------------------")
print("- welcome          -")
print("- to my            -")
print("- character        -")
print("- creator          -")
print("--------------------")



characterName = input("What is your character's name? ")
print(characterName + " will for now be a human.")
print("")

print("Choose a race for your char: ")

for race in races:
    print(race.name + ": " + race.desc)

# defining the attributes and making an array
attrStrenght = input("Strength: ")
attrDexterity = input("Dexterity: ")
attrConstitution = input("Constitution: ")
attrWisodm = input("Wisdom: ")
attrIntelligence = input("Intelligence: ")
attrCharisma = input("Charisma: ")
attributes = [attrStrenght, attrDexterity, attrConstitution, attrWisodm, attrIntelligence, attrCharisma]

# test to sum arrays
a = np.array(attributes)
a = a.astype(float)
b = np.array(raceElf.attrModifier)
b = b.astype(float)
summm = a + b
print(summm)

for attribute in attributes:
    print(attribute)
