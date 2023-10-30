# Importing the time and random modules.
import time
import random


# Everything about the game play is in this function.
def game_program():

    # A list of possible attackers selected at random!
    attackers = ["Pirate", "Dragon", "troll", "wicked fairie",
                 "gorgon", "crocodile", "Lion",
                 "Tiger", "Snake", "Shark", "One-eyed Beast"]
    attacker = random.choice(attackers)

    # A list of possible damages on player selected at random.
    damages = [f"The {attacker} pin's you to the ground",
               f"The {attacker} kills you brutally!",
               f"Ouch! You received 100% damage from the {attacker}",
               f"In the blink of an eye, the {attacker} consumes you!"
               ]

    # A lists of strikes made by player selected at random.
    user_strikes = [f"You tried to stab the {attacker}"
                    "but your trusty dagger broke!",
                    f"You became frightened and tried to run...",
                    f"Oh please!, you screamed!",
                    f"Pooch! Pooch!, You came at the {attacker}"
                    ]

    # Players weapons
    weapons = []

    ## COmment
    # Prints messages slower by 2 seconds.
    def print_pause(message):
        print(message)
        time.sleep(2)

    ''' The two functions below checks if the user's input is valid
    the threeOption_valid_input function checks for valid responses
    given three options while the twoOption_valid_input function
    checks for valid responses given two options.
    '''

    def twoOption_valid_input(prompt, option1, option2):
        if prompt == option1 or prompt == option2:
            return True
        else:
            return False

    def threeOption_valid_input(prompt, option1, option2, option3):
        if prompt == option3:
            return True
        elif prompt == option1 or prompt == option2:
            return True
        else:
            return False

    # Things that happens when the players wants to play again.
    def play_Again():
        replay = input("Would you like to play again? (y/n)\n").lower()
        while not twoOption_valid_input(replay, "y", "n"):
            print_pause("Invalid response!")
            replay = input("Would you like to play again? (y/n)\n").lower()
            if replay == "y" or replay == "n":
                break
        if replay == "y":
            print_pause("Excellent! Restarting the game ...")
            game_program()
        else:
            print_pause("Thanks for playing! See you next time.")

    # This function plays the  introduction when the game starts.
    def intro():
        print_pause("You find yourself standing in an open field, "
                    "filled with grass and yellow wildflowers.")
        print_pause(f"Rumor has it that a {attacker} is somewhere around here,"
                    " and has been terrifying the nearby village.")
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause(
            "In your hand you hold your trusty "
            "(but not very effective) dagger.\n")

    # This function confirms if the user would like to quit.
    def user_quit():
        confirm_quit = input("Are you sure you want to quit? (y/n)\n").lower()
        while not twoOption_valid_input(confirm_quit, "y", "n"):
            print_pause("Invalid response!")
            confirm_quit = input('Enter "y" to confirm quit '
                                 'or "n" to stay in game\n').lower()
            if confirm_quit == "y" or confirm_quit == "n":
                break
        if confirm_quit == "y":
            print_pause("So sad to see you go.")
            print_pause("Hope to see you play again soon!")
        else:
            print_pause("Awesome! You chose to stay!")
            print_pause("Restarting the game...")
            game_program()

    # Things that happen when the player fights
    def fight():
        if "sword" not in weapons:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {attacker}.")
            print_pause(random.choice(user_strikes))
            print_pause(random.choice(damages))
            print_pause("You have been defeated!\n")
            print_pause("GAME OVER!\n")
            play_Again()
        else:
            print_pause(
                f"As the {attacker} moves to attack, "
                "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines "
                        "brightly in your hand as you "
                        "brace yourself for the attack.")
            print_pause(f"But the {attacker} takes one"
                        " look at your shiny new toy "
                        "and runs away!")
            print_pause(f"You have rid the town of the {attacker}."
                        "You are victorious!\n")
            print_pause("GAME OVER!\n")
            play_Again()

    # Asks the user to fight or run.
    def fight_or_run():
        response = input("What would you like to do?\n"
                         "(1) fight\n"
                         "(2) run away\n"
                         "(q) quit game\n").lower()
        while not threeOption_valid_input(response, "1", "2", "q"):
            print_pause("Invaid response!\n")
            response = input("What would you like to do?\n"
                             "(1) fight\n"
                             "(2) run away\n"
                             "(q) quit game\n").lower()
            if response == "q":
                break
            elif response == "1" or response == "2":
                break
        if response == "1":
            fight()
        elif response == "2":
            runAway()
        else:
            user_quit()

    ''' Things that happens when the player
    approaches the house.
    '''
    def KnockDoor():
        if "sword" not in weapons:
            print_pause("You approach the door of the house.")
            print_pause(
                "You are about to knock when the door "
                f"opens and out steps a {attacker}.")
            print_pause(f"Eep! This is the {attacker}'s house!")
            print_pause(f"The {attacker} attacks you!")
            print_pause("You feel a bit under-prepared for this, "
                        "what with only having a tiny dagger.\n")
        else:
            print_pause("You approach the door of the house.")
            print_pause(
                "You are about to knock when the door"
                f" opens and out steps a {attacker}.")
            print_pause(f"Eep! This is the {attacker}'s house!")
            print_pause(f"The {attacker} attacks you!\n")

        fight_or_run()

    # Things that happen to the player goes in the cave.
    def enterCave():
        if "sword" not in weapons:
            print_pause("You peer cautiously into the cave.")
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause("You have found the magical Sword of Ogoroth!")
            print_pause(
                "You discard your silly old dagger "
                "and take the sword with you.")
            print_pause("You walk back out to the field.\n")
            weapons.append("sword")
        else:
            print_pause("You peer cautiously into the cave.")
            print_pause("You've been here before, "
                        "and gotten all the good stuff."
                        "It's just an empty cave now.")
            print_pause("You walk back out to the field.\n")

        next_move()

    # Things that happens when the player runs away.
    def runAway():
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        next_move()

    # Ask's the player his next move.
    def next_move():
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause('Enter "q" to exit game.')
        choice = input("What would you like to do?\n").lower()
        while not threeOption_valid_input(choice, "1", "2", "q"):
            choice = input('Please enter "1", "2" or "q").\n').lower()
            if choice == "q":
                break
            elif choice == "1" or choice == "2":
                break
        if choice == "1":
            KnockDoor()
        elif choice == "2":
            enterCave()
        else:
            user_quit()

    # Things that happen when the game starts.
    def play_game():
        intro()
        next_move()

    # The function call below starts the game play.
    play_game()


# This function call starts the game program.
game_program()
