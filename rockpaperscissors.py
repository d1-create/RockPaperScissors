import random # import random library/module

computeravailablemoves = ["Rock","Paper","Scissors"]#store computer moves for them to be used in a later function

#print rules of game on startup
def printrules():
    print("The rules for this game are straightforward: Rock smashes scissors. Paper covers rock. Scissors cut paper, now the game will start")

#Get The PlayerInput and return it as a string
def PlayerInput():
    playermove = input(str("Rock,Paper or Scissors? ")).title()
    return playermove # return the players move


#get computer input
def ComputerInput(availablemoves):
    computermove = random.choice(availablemoves)
    return computermove # return the computers move after choosing a random value from a predetermined list

#Display the game and what each party has chosen with parameters for both of their inputs
def DisplayGame(playerinput,computerinput):
    print("The Player Has Chosen: ", playerinput, " And the computer has chosen:" , computerinput) #print what each part has chosen

#Find the winner and return the winner
def CheckWinner(playermove,computermove):
    winner = None
    winnerpossibilities = ["Computer", "Player", "Tie"]
    if(playermove == "Rock"):#if player chose rock you should...
        if(computermove == "Paper"):
            winner = winnerpossibilities[0]
        elif(computermove == "Rock"):
            winner = winnerpossibilities[2]
        elif(computermove == "Scissors"):
            winner = winnerpossibilities[1]
    elif(playermove == "Scissors"):#if player chose Scissors you should...
        if(computermove == "Paper"):
            winner = winnerpossibilities[0]
        elif(computermove == "Scissors"):
            winner = winnerpossibilities[2]
        elif(computermove == "Rock"):
            winner = winnerpossibilities[1]
    elif(playermove == "Paper"):#If player choose scissors you should...
        if(computermove == "Scissors"):
            winner = winnerpossibilities[0]
        elif(computermove == "Paper"):
            winner = winnerpossibilities[2]
        elif(computermove == "Rock"):
            winner = winnerpossibilities[1]
    return winner # return the winner of the game - essential for the game to run even if using inefficent nested if statements

#Complete Game with main function to run the entire game
def Main():
    #print rules once for the player
    printrules()
    playermove = None #determine the player move on startup to be nothing
    #loop the game until the player quits
    while(playermove != "Quit"):
        playermove = PlayerInput()
        computermove = ComputerInput(computeravailablemoves)
        DisplayGame(playermove, computermove)
        winner = CheckWinner(playermove,computermove)
        print("The Result is " , winner) #Print the winner and restart the loop if the player has not quit the game
Main()#Run main function including the loop inside without any parameters
