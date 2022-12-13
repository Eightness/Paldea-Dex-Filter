import csv

COL_ID = 0
COL_NAME = "Name"
COL_FORM = "Form"
COL_TYPE1 = "Type1"
COL_TYPE2 = "Type2"
COL_TOTAL = "Total"
COL_HP = "HP"
COL_ATTACK = "Attack"
COL_DEFENSE = "Defense"
COL_SPATK = 9
COL_SPDEF = 10
COL_SPEED = 11
COL_GEN = 12
COL_BANNED = 13

file = open("paldea_dex.csv")
# Abrimos cualquier archivo

csvreader = csv.reader(file)
# Leemos el archivo .csv

data = []
data = next(csvreader)

# paldea_dex = {}
# for pokemon in csvreader:
#     paldea_dex[str(pokemon[COL_ID])] = {}
#     for i in range(1, len(data)):
#         paldea_dex[str(pokemon[COL_ID])][data[i]] = pokemon[i]
# Diccionario de la Pokédex de Paldea

unbanned_pokemon_list = {}
for pokemon in csvreader:
    if pokemon[COL_BANNED] == 'true':
        continue

    unbanned_pokemon_list[str(pokemon[COL_ID])] = {}
    for i in range(1, len(data)):
        unbanned_pokemon_list[str(pokemon[COL_ID])][data[i]] = pokemon[i]
# Diccionario de la Pokédex de Paldea (excepto baneados)


def main():

    cmd = None
    filtered_pkm_list = unbanned_pokemon_list.copy()

    print("")
    print("Welcome to the Paldea Dex filter!")
    print("Made by Bertus :)")
    print("")
    print("Use the commands 'filter' or 'search'.")
    print("You can filter by stats or/and types.")
    print("Enjoy.")
    print("")

    while cmd != "exit":

        cmd = input(">")
        cmd_list = list(cmd.split(" "))

        if cmd_list[0] == "filter":
            if cmd_list[1] == "total_stats":
                filtered_pkm_list = pkm_total_stats(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "attack":
                filtered_pkm_list = pkm_attack(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "spattack":
                filtered_pkm_list = pkm_spattack(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "spdefense":
                filtered_pkm_list = pkm_spdefense(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "defense":
                filtered_pkm_list = pkm_defense(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "speed":
                filtered_pkm_list = pkm_speed(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "spatk_speed":
                filtered_pkm_list = pkm_speed(filtered_pkm_list, int(cmd_list[2]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "atk_speed":
                filtered_pkm_list = pkm_atk_speed(filtered_pkm_list, int(cmd_list[2]), int(cmd_list[3]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "spdef_hp":
                filtered_pkm_list = pkm_spdef_hp(filtered_pkm_list, int(cmd_list[2]), int(cmd_list[3]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "def_hp":
                filtered_pkm_list = pkm_def_hp(filtered_pkm_list, int(cmd_list[2]), int(cmd_list[3]))
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "type":
                filtered_pkm_list = pkm_type(filtered_pkm_list, cmd_list[2])
                print_pokemon(filtered_pkm_list)
                print("")

            if cmd_list[1] == "types":
                filtered_pkm_list = pkm_types(filtered_pkm_list, cmd_list[2], cmd_list[3])
                print_pokemon(filtered_pkm_list)
                print("")

        if cmd_list[0] == "search":
            pkm_namefilter(filtered_pkm_list, cmd_list[1])
            print_pokemon(filtered_pkm_list)
            print("")

        if cmd_list[0] == "team":
            if cmd_list[1] == "add":
                pkm_teambuilder_add(filtered_pkm_list, cmd_list[2])

            if cmd_list[1] == "remove":
                pkm_teambuilder_remove(filtered_pkm_list, cmd_list[2])

            if cmd_list[1] == "show":
                pkm_teambuilder_show(filtered_pkm_list)

            if cmd_list[1] == "reset":
                pkm_teambuilder_reset(filtered_pkm_list, cmd_list[2])

        if cmd_list[0] == "reset":
            filtered_pkm_list = unbanned_pokemon_list.copy()
            print("")
            print("Pokemon list reseted, you can filter/search again.")
            print("")
            
        if cmd_list[0] == "save":
            with open(f"{cmd_list[1]}.csv", "w+") as f:
                for id, attributes in filtered_pkm_list.items():
                    f.write("%s:%s\n" % (id, attributes))

            print("")
            print(f"List successfully saved as {cmd_list[1]}.csv")
            print("")


# A pesar de la nomenclatura de "pkm_list", se trata de un diccionario, no de una lista

def print_pokemon(pkm_list):
    for id, attributes in pkm_list.items():
        print(attributes[COL_NAME] + " | Form: " + attributes["Form"] + " | Types: " + attributes["Type1"] + ", " + attributes["Type2"] + " | Total stats: " +  attributes["Total"] + " | Sp. Atk: " +  attributes["Sp. Atk"] + " | Attack: " +  attributes["Attack"] + " | Sp. Def: " +  attributes["Sp. Def"] + " | Defense: " +  attributes["Defense"] + " | Speed: " +  attributes["Speed"])

def pkm_teambuilder_add(pkm_list, added_pokemon):
    team_list = []
    for id, attributes in pkm_list.items():
        if added_pokemon.lower() in attributes["Name"].lower():
            team_list.append(attributes)

    team_list_final = team_list.copy()

    print("")
    print(f"Added {team_list_final}.")
    print("")

    return team_list

def pkm_teambuilder_show(team_list):

    print(team_list)

def pkm_total_stats(pkm_list, total):
    print("")
    print(f"Pokemon Total stats >= {total}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Total"]) < total:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_attack(pkm_list, attack):
    print("")
    print(f"Pokemon Attack >= {attack}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Attack"]) < attack:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_spattack(pkm_list, spattack):
    print("")
    print(f"Pokemon Sp. Attack >= {spattack}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Sp. Atk"]) < spattack:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list
    
def pkm_defense(pkm_list, defense):
    print("")
    print(f"Pokemon Defense >= {defense}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Defense"]) < defense:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_spdefense(pkm_list, spdefense):
    print("")
    print(f"Pokemon Sp. Defense >= {spdefense}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Sp. Def"]) < spdefense:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_speed(pkm_list, speed):
    print("")
    print(f"Pokemon Speed >= {speed}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Speed"]) < speed:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)
    
    return pkm_list

def pkm_spatk_speed(pkm_list, spatk, speed):
    print("")
    print(f"Pokemon with Sp. Attack >= {spatk} and Speed >= {speed}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Sp. Atk"]) < spatk or int(attributes["Speed"]) < speed:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_atk_speed(pkm_list, attack, speed):
    print("")
    print(f"Pokemon with Attack >= {attack} and Speed >= {speed}: ")
    print("")

    to_delete=[]
    for id, attributes in pkm_list.items():
        if int(attributes["Attack"]) < attack and int(attributes["Speed"]) < speed:
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_spdef_hp(pkm_list, spdef, hp):
    print("")
    print(f"Pokemon with Sp. Defense >= {spdef} and HP >= {hp}: ")
    print("")

    to_delete = []
    for id, attributes in unbanned_pokemon_list.items():
        if int(attributes["Sp. Def"]) < spdef and int(attributes["HP"]) < hp:
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_def_hp(pkm_list, defense, hp):
    print("")
    print(f"Pokemon with Defense >= {defense} and HP >= {hp}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if int(attributes["Defense"]) < defense and int(attributes["HP"]) < hp:
            to_delete.append(id)
    
    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list


def pkm_type(pkm_list, type1):
    print("")
    print(f"Pokemon with type {type1}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if attributes["Type1"].lower() != type1.lower():
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_types(pkm_list, type1, type2):
    print("")
    print(f"Pokemon with types {type1} {type2}: ")
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if attributes["Type1"].lower() != type1.lower() or attributes["Type2"].lower() != type2.lower():
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list

def pkm_namefilter(pkm_list, name):
    print("")

    to_delete = []
    for id, attributes in pkm_list.items():
        if name.lower() in attributes["Name"].lower():
            continue
        else:
            to_delete.append(id)

    for id in to_delete:
        pkm_list.pop(id)

    return pkm_list


main()