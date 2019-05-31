import random

print('Hello, this is Rock, Paper & Scissors for you!')
namep1 = input('Whats your name? \n')
print("Hello", namep1, "!")
again_ = 1
while again_ == 1:

    player1error = 1
    tie_dummy = 0

    print(r"For Rock enter - '1'")
    print(r"For Scissors enter - '2'")
    print(r"For Paper enter - '3'")
    player1 = input('Please enter your choice: ')
    if not (player1 == '1' or player1 == '2' or player1 == '3'):
        player1error = 1
        while player1error == 1:
            print('Error message!')
            player1 = input('Please enter one of the following: Rock (1), Scissors (2), Paper(3): \n')
            if (player1 == '1' or player1 == '2' or player1 == '3'):
                player1error = 0
            else:
                continue

    if player1 == '1':
        player1 = 'Rock'
    elif player1 == '2':
        player1 = 'Scissors'
    else:
        player1 = 'Paper'
    print("You've picked", player1)

    #

    player2 = random.choice(['Rock', 'Scissors', 'Paper'])
    print('The Computer has chosen: ', player2)

    if player1 == player2:
        tie_dummy = 1
        while tie_dummy == 1:
            print('Its a tie! You guys have both chosen:', player1)
            player1 = input('Please enter one of the following: Rock (1), Scissors(2), Paper(3):\n')

            if not (player1 == '1' or player1 == '2' or player1 == '3'):
                player1error = 1
                while player1error == 1:
                    print('Error message!')
                    player1 = input('Please enter one of the following: Rock (1), Scissors (2), Paper(3): \n')
                    if (player1 == '1' or player1 == '2' or player1 == '3'):
                        player1error = 0
                    else:
                        continue

            if player1 == '1':
                player1 = 'Rock'
            elif player1 == '2':
                player1 = 'Scissors'
            else:
                player1 = 'Paper'
            print("You've picked", player1)

            player2 = random.choice(['Rock', 'Scissors', 'Paper'])
            print('The Computer has chosen: ', player2)

            if player1 == player2:
                tie_dummy = 1
                continue
            else:
                tie_dummy = 0
                break

    if player1 == 'Rock' and player2 == 'Scissors':
        print(' ')
        print(namep1, 'wins the game, since', player1, 'beats', player2)
        print(' ')
        print('Thank You', namep1, 'for playing with us! =)')

    if player1 == 'Paper' and player2 == 'Rock':
        print(' ')
        print(namep1, 'wins the game, since', player1, 'beats', player2)
        print(' ')
        print('Thank You', namep1, 'for playing with us! =)')

    if player1 == 'Scissors' and player2 == 'Paper':
        print(' ')
        print(namep1, 'wins the game, since', player1, 'beat', player2)
        print(' ')
        print('Thank You', namep1, 'for playing with us! =)')

    if player2 == 'Rock' and player1 == 'Scissors':
        print(' ')
        print('Computer wins the game, since', player2, 'beats', player1)
        print(' ')
        print('Thank You', namep1, 'for playing with us! =)')

    if player2 == 'Paper' and player1 == 'Rock':
        print(' ')
        print('Computer wins the game, since', player2, 'beats', player1)
        print(' ')
        print('Thank You', namep1, 'for playing with us! =)')

    if player2 == 'Scissors' and player1 == 'Paper':
        print(' ')
        print('Computer wins the game, since', player2, 'beat', player1)
        print(' ')
        print('Thank You', namep1, 'for playing with us! =)')
        print('')

    while True:
        again = input('Would you like to play once again?(yes/no)\n').lower()
        if (again == 'yes' or again == 'y'):
            again_ = 1
            print('Thank you', namep1, 'for staying with us, we do appreciate it! ;)')
            break
        elif (again == 'no' or again == 'n'):
            print('Thank you a lot for choosing us. It is more than appreciated! :)')
            again_ = 0
            break
