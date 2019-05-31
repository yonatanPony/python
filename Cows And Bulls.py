import random


def UserNum():
    while True:
        user = input("Enter your 4 digit num: \n")
        try:
            int(user)
        except:
            print("Wrong input. please try again.")
            continue
        user = int(user)
        if 999 < user < 10000:
            return user
        else:
            print("Wrong input. please try again.")
            continue


def scoore(com, user):
    com1 = str(com)
    user1 = str(user)
    cow = 0
    for i in range(4):
        if user1[i] == com1[i]:
            cow = cow + 1
    return cow


def main():
    com = random.randint(1000, 10000)
    user = UserNum()
    cows = scoore(com, user)
    print("Your number is: ", user)
    print("The computer number is: ", com)
    print("You have got:", cows, "cows and:", (4 - cows), "bulls")


if __name__ == '__main__':
    main()
