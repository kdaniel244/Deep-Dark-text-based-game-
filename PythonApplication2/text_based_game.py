import random
from re import S
import time
from tkinter import END
from asyncio import shield
from os import name
from artwork import *

fast_slow("this game is required to be in full screen (press F11)\n")
input("press enter to start game")
title()
print("")
#get players name
name = input("Please enter your name:")
print("")
print("Hello",name,"\n")
slow("Welcome to the Deep Dark")
print("")

while True:
    print("type play to start the game")

    choice = input("").lower()

    if choice == "play" :
         slow("Here is some tips\n")
         slow("you will have to battle monsters to get to the exit\n")
         slow("if you die you will have to start from the begin again\n")
         time.sleep(2)
         break
    else:
       print("Invalid option")
       
goblin()
 
print("")
slow("you found a goblin\n")
print("")
input("press enter to talk to goblin\n")
slow(name)
slow(": Hello???\n")
slow("goblin:")
slow(name)
slow(" i have waited for you\n")
slow("goblin:")
slow("For you to pass my challange\n")
slow("goblin:")
slow("you have to win a game of rock paper scissors\n")
slow("every damage is 10\n")
slow("are you ready?\n")
time.sleep(1)
enter = input("Press enter to fight\n")

user_health = 100  # used underscore snake case love:)
goblin_health = 100  # I initialized both variables outside

def fight(user_health, goblin_health):  # according to PEP8 I guess. we shouldn't use shadow names. Still,not a big deal
    goblin = random.choice(["r", "p", "s"])
    user = input("Rock(r), Paper(p) or Scissors(s): \n").lower()
    print(goblin)
    if user == goblin:
        slow("You both missed your attacks!\n")
        return user_health, goblin_health
    elif is_win(user, goblin):
       
        goblin_health -= 20
        slow("You hit goblin! 10 DMG Done!!! \n")  
        print("                    Your health: " + str(user_health) + " HP")
        print("")
        print("                    goblin's health: " + str(goblin_health) + " HP")
        print("")
        return user_health, goblin_health
    else:
        slow("  Ow! You got hit by goblin. -10 HP \n")
        user_health -= 10
        print("                    Your health: " + str(user_health) + " HP")
        print("")
        print("                    goblin's health: " + str(goblin_health) + " HP")
        print("")
        return user_health, goblin_health
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (
            player == "p" and opponent == "r"):
        return True
# this function terminates game when someone is at 0 HP and prints output
def game_terminator(user_health, goblin_health):  # I continued with the shadow names to avoid confusion
    if user_health == 0:
        slow("  goblin killed you!\n")
        quit()
        return False
    elif goblin_health == 0:
        slow("  Thrashed goblin to dealth! YOU WON!\n")
        time.sleep(2)
        return False
    else:
        return True
game_is_on = True
# Use while loop for game to run until someone gets 0 HP
while game_is_on:  # game_is_on is a boolean variable
    user_health, goblin_health = fight(user_health, goblin_health)
    game_is_on = game_terminator(user_health, goblin_health)

skeleton()

print("")
slow("you found a skeleton\n") 
input("press enter to talk to skeleton\n")
slow("hello there ")
print(name)
slow("here is a dice for you\n")
slow("so you can roll\n")
slow("if i roll higher you take 10 damage\n")
slow("if you roll higher i take 10 damage\n")
slow("are you ready?\n")

player_hp= 100 
skeleton_hp= 100

def dice_battle(player_hp, skeleton_hp): # Generate random numbers between 1 and 6 for each player.
    input("press enter to roll your dice")
    print("you rolled...")
    time.sleep(2)
    player1_value = random.randint(1, 6)
    print("you rolled", player1_value)
    time.sleep(2)
    skeleton_value = random.randint(1, 6)

    # Display the values
    print("skeleton rolled...")
    time.sleep(2)
    print("skeleton rolled: ", skeleton_value)
    # Selection: based on comparison of the values, take the appropriate path through the code.
    if player1_value > skeleton_value:
        skeleton_hp -= 10
        print("")
        slow("skeleton -10 hp\n")
        print("player hp = ", player_hp)
        print("skeleton hp =", skeleton_hp)
    elif skeleton_value > player1_value:
        player_hp -= 10
        slow("")
        slow("player -10\n")
        print("                    player hp = ", player_hp)
        print("                    skeleton hp =", skeleton_hp)
    else:
     slow("It's a draw\n")

    if player_hp == 0:
        slow("hahahahah kinda weak\n")
        death()
        slow("lost\n")
        quit()
    elif skeleton_hp == 0:
        slow("CRITICAL DAMAGE\n")
        slow("i see\n")
        slow("you stronger than i thought\n")
        slow("you now have 2/3 keys\n")
        print("")
        print("")
        time.sleep(3)
    else: 
        return dice_battle(player_hp, skeleton_hp)
dice_battle(player_hp, skeleton_hp)

def questions1():#sphinx ask 10 questions to the player
    sphinx()
    slow("sphinx:hello ")
    slow(name)
    slow(" didnt expect for you to be able to reach me\n")
    time.sleep(1)
    slow("sphinx:kinda impressed\n")
    slow ("sphinx:are you ready for my challenge\n")
    input("press enter to accept")
    slow("sphinx:there will be 10 questions\n")
    slow("sphinx:you only have one try for every question\n")
    slow("sphinx:if is wrong you will have to start from the beginnin\n")
    slow(name)
    slow(":lets start ")
    print("")
    slow("sphinx:lets beggin\n")
    time.sleep(3)
#question 1
    slow("sphinx:who owns PlayStation?\n")
    question_1 = input("").lower()
    if question_1 == "sony":
        slow("ok there is alot more still\n")
        slow("dont get ahead of yourself\n")
        slow("1/10 Ken Kutaragi was the creator of PlayStation\n")
        time.sleep(2)
        slow("sphinx:what is mario's job?\n")
    else :
        slow("already hahahah\n")
        slow("i was expecting more from you\n")
        slow("the right answer is:sony\n")
        quit()
questions1()
#question 2
def questions2():
    question_2 = input("").lower()
    if question_2 == "plumber":
        slow("2/10 fun fact mario was a carpenter before becoming a plamber\n")
        time.sleep(2)
        slow("ok lets go for the other one\n")
    else :
        slow("on the second one really\n")
        slow("your so dumb HAHAHA\n")
        slow("the right answer is:plumber\n")
        quit()
questions2()
#questions3
def questions3():
    slow("who is sub-zero enemy in mortal combat:?\n")
    question_3 = input("").lower()
    if question_3 == "scorpion":
        slow("ok doing well so far\n")
        slow("3/10 scorpions real name is acctually Hanzo Hasash\n")
        time.sleep(2)
        slow("ok lets go for the other one\n")
    else :
        slow("WOW\n")
        slow("you dont even know basics about mortal kombat\n")
        slow("the right answer is:scorpion\n")
        quit()
questions3()
#questions4
def questions4():
    slow("who was the protagonist of gta 4?\n")
    question_4 = input("").lower()
    if question_4 == "niko bellic":
        slow("now i understand how you reached me \n")
        slow("4/10 niko was  an Eastern European ex-soldier\n")
        time.sleep(2)
        slow("ok lets go for the other one\n")
    else :
        slow("you have to start the game again\n")
        slow("the right answer is:niko bellic\n")
        quit()
questions4()
#question5
def questions5():
    slow("what gaming company started by selling playing cards\n")
    question_5 = input("").lower()
    if question_5 == "nintendo":
        slow("half way there\n")
        slow("5/10 nintendo was founded in 1889\n")
        time.sleep(2)
        slow("lets go to question 6\n")
    else :
        slow("that one was kinda hard\n")
        slow("the right answer is:nintendo\n")
        quit()
questions5()
#questions6
def questions6():
    slow("what is the best selling video game of all time\n")
    question_6 = input("").lower()
    if question_6 == "minecraft":
        slow("that was was ez come on\n")
        slow("6/10 early versions of Minecraft, you could spawn Steve by pressing the G\n")
        time.sleep(2)
        slow("ok you are on question 7 now\n")
    else :
        slow("more than half way but still didnt win\n")
        slow("the right answer is:minecraft\n")
        quit()
questions6()
#questions7
def questions7():
    slow("how much is worth the video gaming industry in 2023?\n124 billion\n467 billion\n853 million\n242 billion\n")
    question_7 = input("").lower()
    if question_7 == "242 billion":
        slow("is a little more now days \n")
        slow("7/10 is expected to reach 682 billion by 2030\n")
        time.sleep(2)
        slow("doing better than expected\n")
    else :
        slow("you went far acctually\n")
        slow("the right answer is:242 billion\n")
        quit()
questions7()
#questions8
def questions8():
    slow("what was the first video game console played in space?\n")
    question_8 = input("").lower()
    if question_8 == "gameboy":
        slow("impressed you know that\n")
        slow("your doing so well \n")
        time.sleep(2)
        slow("ok lets go for the other one\n")
    else :
        slow("already hahahah\n")
        slow("i was expecting more from you\n")
        slow("the right answer is:gameboy\n")
        quit()
questions8()
#questions9
def questions9():
    slow("how many years old was the yougest professional gamer?\n")
    question_9 = input("").lower()
    if question_9 == "11":
        slow("he is probably younger that you\n")
        slow("nice\n")
        time.sleep(2)
    else :
        slow("probably younger than you\n")
        slow("the right answer is:11\n")
        quit()
questions9()
#questions10
def questions10():
    slow("what was pack-man supposed to be named\n")
    question_10 = input("").lower()
    if question_10 == "puck man":
        slow("well done you did it\n")
        slow("you went 10/10\n")
        time.sleep(2)
        slow("you got all your 3 keys\n")
        slow("you can now leave\n")
    else :
        slow("Hahahah\n")
        slow("you lost on the last one\n")
        slow("the right answer is:puck man\n")
        quit()
questions10()

print("")
door_blocked()
print("")
input("press enter to put keys and leave")
print("")
door_opened()
print("")
end()
