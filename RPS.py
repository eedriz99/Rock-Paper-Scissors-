from random import choice

values = [ "R", "P", "D"]




#while not win, continue game, else break and print winner

noWinner = True

while noWinner:
    
    
    #take user anf computer inputs
    
    compInput = choice(values)
    userInput = input(" Enter R for Rock, P for Paper, and S for Scissors and Q to Quit the game: \n").upper()
    
    # define a function to check for wins
    
    def winChecker(userInput, compInput):
        
        # check for possible win scenerios.
        
        if (userInput == "S" and compInput == "P") or (userInput == "P" and compInput == "R") or (userInput == "R" and compInput == "S"):
            noWinner = False
            return ("User Wins!!!")
        elif (compInput == "S" and userInput == "P") or (compInput == "P" and userInput == "R") or (compInput == "R" and userInput == "S"):
            noWinner = False
            return ("Computer Wins!!!")
        elif userInput == "Q":
            noWinner = False
        else:
            return(" Game is a tie, continue")
                

    #check for wins
    print(winChecker(userInput, compInput))