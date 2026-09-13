import random

scf = ["Sasso", "Carta", "Forbici"]
player_score = 0
bot_score = 0

play = input("Vuoi giocare a Sasso, Carta, Forbici? (Y/n) ")
if play == "y" or play == "Y":
    while player_score <= 2 and bot_score <= 2:
        player = input("scegli tra Sasso, Carta e Forbici ")
        if player in scf:
            print("Hai scelto " + str(player) + "!!!")
            bot = random.choice(scf)
            print("il bot ha scelto " + str(bot) + "!!!")
            if player == "Sasso" and bot == "Forbici" or player == "Forbici" and bot == "Carta" or player == "Carta" and bot == "Sasso":
                print("Round vinto!!! 1+ punto per te")
                player_score += 1
                print("(TU: " + str(player_score) + " | Bot: " + str(bot_score) + ")")
            elif player == "Sasso" and bot == "Sasso" or player == "Forbici" and bot == "Forbici" or player == "Carta" and bot == "Carta":
                print("Pareggio...")
            else:
                print("Round perso....1+ punto per CPU")
                bot_score += 1
                print("(TU: " + str(player_score) + " | Bot: " + str(bot_score) + ")")
else:
    print("scelta errata, riprova")

if player_score == 3:
    print("HAI VINTO!!!")
elif bot_score == 3:
    print("HAI PERSO.....")
