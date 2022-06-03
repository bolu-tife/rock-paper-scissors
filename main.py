from random import choice

def is_valid(user_input):
    return user_input == "R" or user_input == "P" or user_input == "S"

    

def determine_winner(user_option, computer_option):
    if user_option == "R":
        if computer_option == "P":
            print("You lose! Paper covers rock")
        else:
            print("You win! Rock smashes scissors")

    elif user_option == "P":
        if computer_option == "R":
            print("You win! Paper covers rock")
        else:
            print("You lose! Scissors cuts paper")
    
    elif user_option == "S": 
        if computer_option == "R":
            print("You lose! Rock smashes scissors")
        elif computer_option == "P":
            print("You win! Scissors cuts paper")

     

def game():
    options = ["R", "P", "S"]
    option_meaning = {"R":"Rock", "P": "Paper", "S": "Scissor"}
    message = "Pick an option: \nR - Rock \nP - Paper \nS-Scissors \n"

    computer_move = None
    user_input = None
    tie = True


    while tie:
        user_input = input(message).upper()

        while not is_valid(user_input):
            print("Error: You entered an invalid option, please try again")
            user_input = input(message).upper()

        computer_move = choice(options)

        print("Player({player}) : CPU({cpu})".format(player=option_meaning[user_input], cpu=option_meaning[computer_move]))
        if user_input == computer_move:
            print("Tie")
        else:
            determine_winner(user_input, computer_move)
            tie = False


game()        
