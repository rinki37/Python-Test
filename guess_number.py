import sys
import random

def guessing_game(name='PlayerOne'):
    game_count = 0 
    player_wins = 0

    def play_guessing_game():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guessing_game()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you chose {player}.")
        print(f"I was thinking about the number {computer}.")

        def is_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"\nSorry, {name}. Better luck next time. 😢"

        game_result = is_winner(player, computer)
        print(game_result)
        
        nonlocal game_count 
        game_count += 1
        print(f"\nGame count: {str(game_count)}")
        print(f"\n{name}'s wins: {str(player_wins)}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")       
        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guessing_game()
        else:
            print("\n🎉🎉🎉🎉")
            print(f"Thank you for playing {name}!\n")
            if __name__ == "__main__": 
                sys.exit(f"Bye {name}! 👋")
            else: # If this file is used as a module and used in other file this line will execute. 
                return

    return play_guessing_game  # Created the closure

if __name__ == "__main__": # This will execute if this is the main file. 
    import argparse 
    parser = argparse.ArgumentParser(description="Provides a personalized game experience.")
    parser.add_argument(
        "-n", "--name", metavar="name", 
        required=True, help="The name of the person playing the game."
    )
    
    args = parser.parse_args()
    guess_my_number = guessing_game(args.name)
    guess_my_number()