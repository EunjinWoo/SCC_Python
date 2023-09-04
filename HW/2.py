import random

rsp = {
    0: "rock",
    1: "scissor",
    2: "paper"
}

more = "y"
tot_result = [0, 0, 0] # 이긴 횟수, 진 횟수, 비긴 횟수
while True:
    com_result = random.randint(0,2) # 0: rock, 1: scissor, 2: paper
    player_input = input("Enter: ")
    print("computer: ", rsp[com_result])

    if player_input.lower() == "rock":
        if com_result == 0:
            tot_result[2] += 1
            print("비겼습니다")
        elif com_result == 1:
            tot_result[0] += 1
            print("이겼습니다")
        else:
            tot_result[1] += 1
            print("졌습니다")
    elif player_input.lower() == "scissor":
        if com_result == 1:
            tot_result[2] += 1
            print("비겼습니다")
        elif com_result == 2:
            tot_result[0] += 1
            print("이겼습니다")
        else:
            tot_result[1] += 1
            print("졌습니다")
    elif player_input.lower() == "paper":
        if com_result == 2:
            tot_result[2] += 1
            print("비겼습니다")
        elif com_result == 0:
            tot_result[0] += 1
            print("이겼습니다")
        else:
            tot_result[1] += 1
            print("졌습니다")
    else:
        print("Please Enter rock / scissor / paper")

    more = input("Wanna play more? [y/n]: ")
    if more == "n" or more == "N":
        print(f"이긴 횟수: {tot_result[0]}, 진 횟수: {tot_result[1]}, 비긴 횟수: {tot_result[2]}")
        break