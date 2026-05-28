#Pokemon
#Angela M
#Pokemon Evolution Game

#Init
import random

pokemon_lvl = 0
pokemon_name = "Charmander"
day = 1

#Functions
def main():
    global day
    print("Welcome to Pokemon Evolution")
    while True:
        print("Choose an activity for Day: " + str(day))
        print("""1.Train
2. Gym Battle
3.Rest(Display Info)
4.Quit
5.Final Battle""")
        activity = int(input("Activity for the day: "))
        if activity == 1:
            train()
        elif activity == 2:
            battle()
            evolve()
        elif activity == 3:
            rest()
        elif activity == 4:
            break
        elif activity == 5:
            final_battle()
            break

        day = day + 1



def evolve():
    if pokemon_lvl >= 5:
        pokemon_name = "Charmeleon"
        print("Your pokemon evolved into Charmeleon")
    elif pokemon_lvl >= 10:
        pokemon_name = "Charizard"
        print("Your pokemon evolved into Charizard")

def train():
    global pokemon_lvl
    pokemon_lvl = pokemon_lvl + 1
    print("Your pokemon's level increased by 1" \
    "")
def rest():
    if pokemon_lvl < 5:
        pokemonlvl1()
        print("Name: Charmander")
        print("Level: " + str(pokemon_lvl))
    elif pokemon_lvl >= 5 and pokemon_lvl < 10:
        pokemonlvl2()
        print("Name: Charmeleon")
        print("Level: " + str(pokemon_lvl))
    elif pokemon_lvl >= 10:
        pokemonlvl3()
        print("Name:Charizard")
        print("Level: " + str(pokemon_lvl))


def battle():
    outcome = random.randint(1,2)
    if outcome == 1:
        global pokemon_lvl
        pokemon_lvl = pokemon_lvl + 2
        print("Congrats. Your Pokemon Won and increased its level by 2!")
    elif outcome == 2:
        print("Uh oh.. your Pokemon lost..level doesn't change.")

def final_battle():
    outcome = random.randint(1,15)
    while True:

        if pokemon_lvl <= 5:
            if outcome == 7:
                print("Congrats! Your Pokemon beat the Final Boss")

            else:
                print("Your Pokemon loses.. Game over")

        elif pokemon_lvl >=5 and pokemon_lvl <= 10:
            if outcome == 15 or outcome == 5 or outcome == 10:
                print("Congrats! Your Pokemon beat the Final Boss")

            else:
                print("Your Pokemon loses.. Game over")

        elif pokemon_lvl >= 10:
            if outcome == 3 or outcome == 6 or outcome == 9 or outcome == 12 or outcome == 15:
                print("Congrats! Your Pokemon beat the Final Boss")

            else:
                print("Your Pokemon loses.. Game over")
        break




def pokemonlvl1():
    print((r"             _.--\"\"`-..\n"))
    print((r"           ,'          `.\n"))
    print((r"         ,'          __  `.\n"))
    print((r"        /|          \" __   \\\n"))
    print((r"       , |           / |.   .\n"))
    print((r"       |,'          !_.'|   |\n"))
    print((r"     ,'             '   |   |\n"))
    print((r"    /              |`--'|   |\n"))
    print((r"   |                `---'   |\n"))
    print((r"    .   ,                   |                       ,\".\n"))
    print((r"     ._     '           _'  |                    , ' \\ `\n"))
    print((r" `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|\n"))
    print((r" |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\\n"))
    print(("-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .\n"))
    print((r" `,         \"\"\"\"'     `.              ,'         |   |  ',,\n"))
    print((r"   `.      '            '            /          '    |'. |/\n"))
    print((r"     `.   |              \\       _,-'           |       ''\n"))
    print((r"       `._'               \\   '\"\\                .      |\n"))
    print((r"          |                '     \\                `._  ,'\n"))
    print((r"          |                 '     \\                 .'|\n"))
    print((r"          |                 .      \\                | |\n"))
    print((r"          |                 |       L              ,' |\n"))
    print((r"          `                 |       |             /   '\n"))
    print((r"           \\                |       |           ,'   /\n"))
    print((r"         ,' \\               |  _.._ ,-..___,..-'    ,'\n"))
    print((r"        /     .             .      `!             ,j'\n"))
    print((r"       /       `.          /        .           .'/\n"))
    print((r"      .          `.       /         |        _.'.'\n"))
    print((r"       `.          7`'---'          |------\"'_.'\n"))
    print((r"      _,.`,_     _'                ,''-----\"'\n"))
    print((r"  _,-_    '       `.     .'      ,\\\n"))
    print((r"  -\" /`.         _,'     | _  _  _.|\n"))
    print((r"   \"\"--'---\"\"\"\"\"'        `' '! |! /\n"))
    print((r"                           `\" \" -' mh\n"))
    print(("\n"))
    print(("\n"))

def pokemonlvl2():
    print((r"                     ,-'`\\\n"))
    print((r"                 _,\"'    j\n"))
    print((r"          __....+       /               .\n"))
    print((r"      ,-'\"             /               ; `-._.'.\n"))
    print((r"     /                (              ,'       .'\n"))
    print((r"    |            _.    \\             \\   ---._ `-.\n"))
    print((r"    ,|    ,   _.'  Y    \\             `- ,'   \\   `.`.\n"))
    print((r"    l'    \\ ,'._,\\ `.    .              /       ,--. l\n"))
    print((r" .,-        `._  |  |    |              \\       _   l .\n"))
    print((r"/              `\"--'    /              .'       ``. |  )\n"))
    print((".\\    ,                 |                .        \\ `. '\n"))
    print(("`.                .     |                '._  __   ;. \\'\n"))
    print((r" `-..--------...'       \\                  `'  `-\"'.  \\\n"))
    print((r"     `......___          `._                        |  \\\n"))
    print((r"              /`            `..                     |   .\n"))
    print((r"             /|                `-.                  |    L\n"))
    print((r"            / |               \\   `._               .    |\n"))
    print((r"          ,'  |,-\"-.   .       .     `.            /     |\n"))
    print((r"        ,'    |     '   \\      |       `.         /      |\n"))
    print((r"      ,'     /|       \\  .     |         .       /       |\n"))
    print((r"    ,'      / |        \\  .    +          \\    ,'       .'\n"))
    print((r"   .       .  |         \\ |     \\          \\_,'        / j\n"))
    print((r"   |       |  L          `|      .          `        ,' '\n"))
    print((r"   |    _. |   \\          /      |           .     .' ,'\n"))
    print((r"   |   /  `|    \\        .       |  /        |   ,' .'\n"))
    print((r"   |   ,-..\\     -.     ,        | /         |,.' ,'\n"))
    print((r"   `. |___,`    /  `.   /`.       '          |  .'\n"))
    print((r"     '-`-'     j     ` /.\"7-..../|          ,`-'\n"))
    print((r"               |        .'  / _/_|          .\n"))
    print((r"               `,       `\"'/\"'    \\          `.\n"))
    print((r"                 `,       '.       `.         |\n"))
    print((r"            __,.-'         `.        \\'       |\n"))
    print((r"           /_,-'\\          ,'        |        _.\n"))
    print((r"            |___.---.   ,-'        .-':,-\"`\\,' .\n"))
    print((r"                 L,.--\"'           '-' |  ,' `-.\\\n"))
    print((r"                                       `.' mh\n"))

def pokemonlvl3():

    print((r"                .\"-,.__\n"))
    print((r"                `.     `.  ,\n"))
    print((r"             .--'  .._,'\"-' `.\n"))
    print((r"            .    .'         `'\n"))
    print((r"            `.   /          ,'\n"))
    print((r"              `  '--.   ,-\"'\n"))
    print((r"               `\"`   |  \\\n"))
    print((r"                  -. \\, |\n"))
    print((r"                   `--Y.'      ___.\n"))
    print((r"                        \\     L._, \\\n"))
    print((r"              _.,        `.   <  <\\                _\n"))
    print((r"            ,' '           `, `.   | \\            ( `\n"))
    print((r"         ../, `.            `  |    .\\`.           \\ \\_\n"))
    print((r"        ,' ,..  .           _.,'    ||\\l            )  '\".\n"))
    print((r"       , ,'   \\           ,'.-.`-._,'  |           .  _._`.\n"))
    print((r"     ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\\n"))
    print((r"   .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.\n"))
    print((r"   |  '          ..         `-...-\"  |  `-'      / /        . `.\n"))
    print((r"   | /           |L__           |    |          / /          `. `.\n"))
    print((r"  , /            .   .          |    |         / /             ` `\n"))
    print((r" / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\\n"))
    print((r"/ .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.\n"))
    print((".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\\n"))
    print(("' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`\n"))
    print(("|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\\n"))
    print(("||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|\n"))
    print(("||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||\n"))
    print(("|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||\n"))
    print(("||/            _,-------7 '              . |  `-'    l         /    `||\n"))
    print((". |          ,' .-   ,' ||               | .-.        `.      .'     ||\n"))
    print((r"`'        ,'    `\".'    |               |    `.        '. -.'       `'\n"))
    print((r"         /      ,'      |               |,'    \\-.._,.'/'\n"))
    print((r"         .     /        .               .       \\    .''\n"))
    print((r"       .`.    |         `.             /         :_,'.'\n"))
    print((r"         \\ `...\\   _     ,'-.        .'         /_.-'\n"))
    print((r"          `-.__ `,  `'   .  _.>----''.  _  __  /\n"))
    print((r"               .'        /\"'          |  \"'   '_\n"))
    print((r"              /_|.-'\\ ,\".             '.'`__'-( \\\n"))
    print((r"                / ,\"'\"\\,'               `/  `-.|\" mh\n"))

#Main
main()
