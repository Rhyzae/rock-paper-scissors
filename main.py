import random
import time

choices = ['rock', 'paper', 'scissors']

print("------------------------------------------------------\nThis is a rock / paper / scissors game against a computer\n------------------------------------------------------")

while True:
    computer_choice = choices[random.randint(0,2)]
    while True:
        player_choice = input("\nWhat will you choose? (rock/paper/scissors) ").lower()
        if player_choice in choices:
            break
        else:
            print("Please choose on of the three options.")
    time.sleep(1)
    print(f"\nPlayer: {player_choice.title()}")
    time.sleep(1)
    print("\nCalculating response...")
    time.sleep(3)
    print(f"\nComputer: {computer_choice.title()}")
    time.sleep(1)
    if player_choice == computer_choice:
        print("\nGame Tied")
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("\nYou Win")
    elif player_choice == 'rock' and computer_choice == 'paper':
        print("\nYou Lose")
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("\nYou Win")
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print("\nYou Lose")
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("\nYou Win")
    else:
        print("\nYou Lose")
    response = input("\nWould you like to quit? (type 'quit' to exit) ").lower()
    if response == 'quit':
        break

print("\nThank you for using this program!")