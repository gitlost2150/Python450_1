import random
from colorama import Fore, Back, Style
import sys

#User balance
userBalance = 100

# User should input the age before entrance to next steps
# Here we check the age of user
def ageChecker():
    age = int(input(Fore.YELLOW + "How old you are?: "))
    if age >= 18:
        print(Fore.GREEN + "Proceed to place a bet please: ")
    else:
        print(Fore.RED + "You can't play if you're younger than 18 years old: ")
        sys.exit()

ageChecker()

#Teams list (tuple)
teamsTuple = (
    "Charlton Athletic", 
    "Bristol City" , 
    "Millwall", 
    "Sheffield United", 
    "Liverpool", 
    "Coventry City", 
    "Rotherham United", 
    "Portsmouth", 
    "Newport County", 
    "Plymouth Argyle")

#Odds generator
def oddsGenerator(minOdds, maxOdds):
    randomOdds = random.uniform(1.1, 10.9)
    return randomOdds

# Odds for different selections
oddsForTeamHome = round(oddsGenerator(1.1, 10.9), 2)
oddsForTeamDraw = round(oddsGenerator(1.1, 10.9), 2)
oddsForTeamAway = round(oddsGenerator(1.1, 10.9), 2)

#Random selection from teams tuple
teamHome = random.choice(teamsTuple)
teamAway = random.choice(teamsTuple)
teamDraw = "Draw"

# Messages and selections for betting
print(Fore.BLUE + "Your balance is", userBalance, "dollars")

print(Fore.YELLOW + "Choose a selection for bet ")
print(Fore.GREEN + "Enter 1 if you want to place Bet to", teamHome, "with Odd", oddsForTeamHome)
print(Fore.GREEN + "Enter 2 if you want to place Bet to", teamAway, "with Odd", oddsForTeamAway)
print(Fore.GREEN + "Enter 3 if you want to place Bet to", teamDraw, "with Odd", oddsForTeamDraw)

# User chose
def userChoose():
    global userSelection
    userSelection = int(input(Fore.LIGHTBLUE_EX + "Enter your chose: "))
    if userSelection == 1:
        print(Fore.YELLOW + "You chose a", teamHome, "and it has odds", oddsForTeamHome)
    elif userSelection == 2:
        print(Fore.YELLOW + "You chose a", teamAway, "and it has odds", oddsForTeamAway)
    elif userSelection == 3:
        print(Fore.YELLOW + "You chose a", teamDraw, "and it has odds", oddsForTeamDraw)
    else:
        print(Fore.RED + "You chose a wrong number. Try again please")
        sys.exit()

userChoose()

# How much user want to bet
def userBet():
    global userMoney
    userMoney = int(input(Fore.CYAN + "How much do you want to bet? "))
    if userMoney >= userBalance:
        print(Fore.RED + "You have insufficient funds to place this bet")
        sys.exit()
    if userMoney < userBalance:
        print(Fore.GREEN + "You have successfully placed this bet")
    global userBalanceNew    
    userBalanceNew = userBalance - userMoney
    return userBalanceNew
userBet()
print(Fore.GREEN + "Your new balance is", userBalanceNew, "dollars")

# Define win user or lose by random
winOrNotList = ("win", "lose")
gameResult = random.choice(winOrNotList)
if gameResult == "win":
    print(Fore.CYAN + "Congrats! You won!")
else:
    print(Fore.RED + "Sorry! You lose!")    



# counter for balance according to odds - win

def finalResult():
    global userWinBalance
    global userLoseBalance
    if gameResult == "win":
        if userSelection == 1:
            userWinBalance = float(userMoney * oddsForTeamHome)
            print(Fore.GREEN + "You are", gameResult, round(userWinBalance,2), "dollars")
            finalWinBalance = float(userBalance + userWinBalance)
            print(Fore.YELLOW + "Your new balance is", finalWinBalance, "dollars")
            return
        if userSelection == 2:
            userWinBalance = float(userMoney * oddsForTeamAway)
            print(Fore.GREEN + "You are", gameResult, round(userWinBalance,2), "dollars")
            finalWinBalance = float(userBalance + userWinBalance)
            print(Fore.YELLOW + "Your new balance is", finalWinBalance, "dollars")
            return    
        else:
            userWinBalance = float(userMoney * oddsForTeamDraw)
            print(Fore.GREEN + "You are", gameResult, round(userWinBalance,2), "dollars")
            finalWinBalance = float(userBalance + userWinBalance)
            print(Fore.YELLOW + "Your new balance is", finalWinBalance, "dollars")
            return
    else:
          userLoseBalance = float(userBalanceNew - userMoney)
          print(Fore.RED + "You are", gameResult, round(userMoney,2), "dollars")
          print(Fore.YELLOW + "Your new balance is", userBalanceNew, "dollars")
          return
finalResult()
