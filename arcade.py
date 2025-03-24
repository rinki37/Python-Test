import sys
from guess_number import guessing_game
from rps import rps

def play_arcade(name='PlayerOne'):   
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"{name}, welcome back to the Arcade menu! \n")
       
        playerchoice = input(f"\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n")
        
        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_arcade(name)
        welcome_back = True
 
        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guessing_game(name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")
    

if __name__ == "__main__": # This will execute if this is the main file. 
    import argparse 
    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")
    parser.add_argument(
        "-n", "--name", metavar="name", 
        required=True, help="The name of the person playing the game."
    )
    
    args = parser.parse_args()

    playarcade = play_arcade(args.name)
    playarcade()
