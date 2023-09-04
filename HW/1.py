# Up Down game

import random
cnt = 0

while True:
    print("Your last game's num of attempts:", cnt)
    cnt = 0

    random_number = random.randint(1, 100)
    print("Randint is set. Please Start the game!")

    # Game
    while True:
        player_num = int(input())
        cnt += 1
        
        if (player_num >= 1) and (player_num <= 100):
            if player_num == random_number:
                print("correct! Your num of attempts is", cnt)
                break
            elif player_num > random_number:
                print("Down")
            else:
                print("Up")
        else:
            print("Please enter a number within a valid range")

    more = input("Wanna play more? [y/n]: ")
    if more == "n" or more == "N":
        break
