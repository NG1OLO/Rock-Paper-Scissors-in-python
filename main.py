import random

scf_it = ["Sasso", "Carta", "Forbici"]
scf_en = ["Rock", "Paper", "Scissors"]

player_score = 0
bot_score = 0

language = input("Seleziona una lingua/Choose a language:\n1) Italiano\n2) English ")
if language == "1":
    play = input("Vuoi giocare a Sasso, Carta, Forbici? (Y/n) ").capitalize()
    if play == "Y":
        while player_score <= 2 and bot_score <= 2:
            player = input("scegli tra Sasso, Carta e Forbici: ").capitalize()
            if player in scf_it:
                print("Hai scelto " + str(player) + "!!!")
                bot = random.choice(scf_it)
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
elif language == "2":
    play = input("Wanna play Rock, Paper, Scissors? (Y/n) ").capitalize()
    if play == "Y":
        while player_score <= 2 and bot_score <= 2:
            player = input("Choose between Rock, Paper and Scissors: ").capitalize()
            if player in scf_en:
                print("You choose " + str(player) + "!!!")
                bot = random.choice(scf_en)
                print("CPU choose " + str(bot) + "!!!")
                if player == "Rock" and bot == "Scissors" or player == "Scissors" and bot == "Paper" or player == "Paper" and bot == "Rock":
                    print("Round WIN!!! 1+ point for you")
                    player_score += 1
                    print("(YOU: " + str(player_score) + " | CPU: " + str(bot_score) + ")")
                elif player == "Rock" and bot == "Rock" or player == "Scissors" and bot == "Scissors" or player == "Paper" and bot == "Paper":
                    print("Tie...")
                else:
                    print("Round Lost....1+ point for CPU")
                    bot_score += 1
                    print("(You: " + str(player_score) + " | CPU: " + str(bot_score) + ")")

if language == "1":
    if player_score == 3:
        print("HAI VINTO!!!")
    elif bot_score == 3:
        print("HAI PERSO.....")
elif language == "2":
    if player_score == 3:
        print("YOU WIN!!!")
    elif bot_score == 3:
        print("YOU LOST.....")
