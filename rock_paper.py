import random,getpass
options=["Rock","Scissor","Paper","Spock","Lizard"]
rules={"Rock":["Scissor","Lizard"],"Scissor":["Lizard","Paper"],
"Paper":["Spock","Rock"],"Spock":["Scissor","Rock"],"Lizard":["Spock","Paper"]}
def userinput():
    while True:
        print("1) Single player game: ")
        print("2) Two players game: ")
        print("3) User Guide")
        print("4) Know the rules ")
        print ("5) Quit")
        try: # To caputure any unwanted errors
            choice=int(input("Enter the number of your choice: "))
            if (choice==1):
                single() #calling single functiond
            if (choice==2):
                double() #calling double function
            if (choice==3):
                #prints the user guide
                print("User Guide\n\n")
                print("Choose the mode of play [single player/Multiplayer]")
                print("A menu is displayed for showing the number of options like shown below")
                menu()
                print("Enter number of the desired choice ")
                print("There you go\n\n ")
                print("Note: In multiplayer mode both player's input is hidden\n")
            
            if (choice==4):#Prints the Rules
                print ("\nRules are :\n")
                print("Rock smashes scissors and lizards")
                print("Paper covers rock and disproves Spock")
                print ("Scissors cuts paper and decapitates lizard")
                print("Lizard eats paper and poisons Spock")
                print("Spock smashes scissors and vaporizes rock\n\n")
            if (choice==5):
                print("Bye")
                break
            if (choice not in [1,2,3,4,5]):
                print("Not a valid option")
        except:
            print("Not a valid option")
def check(a,b):
    option1=rules[a] #Fetches the moves a can counter 
    option2=rules[b] #Fetches the moves b can counter
    if (a==b): #checks for the ties
        print("Its a tie")
    for i in option1:
        if (i == b): #checks whether b lies in list
            print("Player 1 wins\n") #declares player 1 i.e as winner
    for i in option2:
        if (i==a): #checks whether a lies in list
            print("Player 2 wins\n")#declares player 2 i.e as winner

def menu():
    counter=1 #Used to create the numbering
    print("\n")
    for i in options:
        print(counter,") ",i)
        counter+=1
    print("\n")

def single():
    
    try:
        while True:
            menu() #used to print menu for options
            print("Hit Enter to return to main menu\n")
            ch=int(input("Enter number of your choice"))
            b=options[random.randint(0,4)] #Generates a random integer between 0-4 both inclusive and use it as index to create a random input from list options
            while (ch not in [1,2,3,4,5]): #checks the user's input
                print("Not a valid option")
                ch=int(input("Enter number of your choice"))
            else:
                a=options[ch-1]
                print("\nYou played",a,"\nComputer played ",b)
                check(a,b)
    except:
        print("\n")
def double():
    try:
        while True:
            menu()
            print("Hit Enter to return to main menu\n")
            print ("Don't worry your input will be hidden so press enter after entering")
            p1=int(getpass.getpass("Player 1 Enter your choice: ")) #getpass hides the value entered hence makes it hidden
            p2=int(getpass.getpass("Player 2 Enter your choice: ")) #getpass hides the value entered hence makes it hidden
            while (p1 or p2) not in [1,2,3,4,5]: #checks the user's input
                if (p1  not in [1,2,3,4,5]): #checks each player's input
                    print("Not a valid option")
                    p1=int(getpass.getpass("Player 1 Enter your choice: "))
                if (p2  not in [1,2,3,4,5]): #checks each player's input
                    print("Not a valid option")
                    p2=int(getpass.getpass("Player 2 Enter your choice: "))

            print("\nPlayer 1 played",options[p1-1],"\nPlayer 2 played ",options[p2-1])
            check(options[p1-1],options[p2-1]) #calling check function with user's argument
    except:
        print ("going to main menu")
        print ("\n")
    
userinput() #calling the function
