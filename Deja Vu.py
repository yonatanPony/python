#Getting and checking the number from the user.
def getTheNum():
    while True:
        num1 = input("Enter your 5 digit num: \n")
        try:
            int(num1)
        except:
            print("Your num dosent follow the orders. please try again")
            continue

        if len(str(num1)) != 5:
            print("Your num dosent follow the orders. please try again")
            continue

        else:
            return num1

#Using the already checked number to print and calculate according to the mission
def PrintTheNum(num):
    print("You entered the number: ", num)
    sum1 = 0
    numList = []
    for i in range(5):
        sum1 = int(num[i]) + sum1
        numList.append(num[i])
    print(numList)
    print("the summery of your number is: ", sum1)

#the main Func which only calling the functions that we build.
def main():
    num = getTheNum()
    PrintTheNum(num)


if __name__ == '__main__':
    main()
