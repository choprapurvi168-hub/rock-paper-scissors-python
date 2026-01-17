import random

while True:
    player1 = input("Enter your choice (rock/paper/scissors/exit): ").lower()

    if player1 == "exit":
        print("Game exited.")
        break   

    player2 = random.choice(['rock', 'paper', 'scissors'])

    print("Player 1 choice:", player1)
    print("Player 2 choice:", player2)

    if player1 == player2:
        print("It's a tie")
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'paper' and player2 == 'rock') or \
         (player1 == 'scissors' and player2 == 'paper'):
        print("You Win!")
    else:
        print("Computer Wins!")

