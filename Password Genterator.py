import random
import string


def GetLevel():
    while True:
        level = input("Enter the security level between 1 to 6: \n")
        try:
            int(level)
        except:
            print("Try again")
            continue
        level = int(level)
        if 0 < level <= 6:
            return level
        else:
            print("Try again")
            continue


def level_1():
    passwd = []
    for i in range(6):
        passwd.append(random.randint(0, 10))
    return passwd


def level_2():
    passwd = []
    for i in range(2):
        passwd.append(random.choice(string.ascii_letters))
    for i in range(6):
        passwd.append(random.randint(0, 10))
    return passwd


def level_3():
    passwd = []
    for i in range(4):
        passwd.append(random.choice(string.ascii_letters))
        passwd.append(random.randint(0, 10))
    return passwd


def level_4():
    passwd = []
    for i in range(3):
        passwd.append(random.choice(string.ascii_letters))
        passwd.append(random.randint(0, 10))
        passwd.append(random.choice(string.punctuation))
    return passwd


def level_5():
    passwd = []
    for i in range(12):
        passwd.append(random.choice(string.ascii_letters + string.punctuation + string.digits))
    return passwd


def level_6():
    passwd = []
    while True:
        num = input("Enter password length in digits: \n")
        try:
            int(num)
            break
        except:
            print("I said *IN DIGITS*!")
            continue
    num = int(num)
    for i in range(num):
        passwd.append(random.choice(string.ascii_letters + string.punctuation + string.digits))
    return passwd


def WhichLevel(level):
    if level == 1:
        password = level_1()
        return password
    if level == 2:
        password = level_2()
        return password
    if level == 3:
        password = level_3()
        return password
    if level == 4:
        password = level_4()
        return password
    if level == 5:
        password = level_5()
        return password
    if level == 6:
        password = level_6()
        return password


def main():
    level = GetLevel()
    password = WhichLevel(level)
    password = ''.join(str(x) for x in password)
    print("Your password is: <> ", password, " <>")


if __name__ == '__main__':
    main()