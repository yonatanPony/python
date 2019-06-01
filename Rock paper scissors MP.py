def get_names():
    name = input('Whats your name? \n')
    print("Hello", name, "!")
    return name

#getting player choice and return the usable value
def player_choice():
    player = input('Please enter your choice: ')
    if not (player == '1' or player == '2' or player == '3'):
        player1error = 1
        while player1error == 1:
            print('Error message!')
            player = input('Please enter one of the following: Rock (1), Scissors (2), Paper(3): \n')
            if (player == '1' or player == '2' or player == '3'):
                player1error = 0
            else:
                continue
    if player == '1':
        player = 'Rock'
    elif player == '2':
        player = 'Scissors'
    else:
        player = 'Paper'
    print("You've picked", player)
    return player


#in case of a tie
def its_tie(num1,name1,name2):
    print('Its a tie! You guys have both chosen:', num1)
    print(name1+"'s", "turn")
    num1 = player_choice()
    print(name2+"'s", "turn")
    num2 = player_choice()
    return num1, num2

#check to see which player has won and print it
def who_win(player1, player2, namep1, namep2):
    if player1 == 'Rock' and player2 == 'Scissors':
        print(' ')
        print(namep1, 'wins the game, since', player1, 'beats', player2)
        print(' ')
        print('Thank You', namep1, "and", namep2, 'for playing with us! =)')

    elif player1 == 'Paper' and player2 == 'Rock':
        print(' ')
        print(namep1, 'wins the game, since', player1, 'beats', player2)
        print(' ')
        print('Thank You', namep1, "and", namep2, 'for playing with us! =)')

    elif player1 == 'Scissors' and player2 == 'Paper':
        print(' ')
        print(namep1, 'wins the game, since', player1, 'beat', player2)
        print(' ')
        print('Thank You', namep1, "and", namep2, 'for playing with us! =)')

    elif player2 == 'Rock' and player1 == 'Scissors':
        print(' ')
        print(namep2, 'wins the game, since', player2, 'beats', player1)
        print(' ')
        print('Thank You', namep1, "and", namep2, 'for playing with us! =)')

    elif player2 == 'Paper' and player1 == 'Rock':
        print(' ')
        print(namep2, 'wins the game, since', player2, 'beats', player1)
        print(' ')
        print('Thank You', namep1, "and", namep2, 'for playing with us! =)')

    elif player2 == 'Scissors' and player1 == 'Paper':
        print(' ')
        print(namep2, 'wins the game, since', player2, 'beats', player1)
        print(' ')
        print('Thank You', namep1, "and", namep2, 'for playing with us! =)')
        print('')


# the stractur of the game himself. work as a recursion if player want a rematch
def game_play(namep1, namep2):
    print(r"For Rock enter - '1'")
    print(r"For Scissors enter - '2'")
    print(r"For Paper enter - '3'")
    print(namep1+"'s", "turn")
    player1 = player_choice()
    print(namep2+"'s", "turn")
    player2 = player_choice()
    while (player1 == player2):
        player1, player2 = its_tie(player1, namep1, namep2)
    who_win(player1, player2, namep1, namep2)
    while True:
        again = input('Would you like to play once again?(yes/no)\n').lower()
        if (again == 'yes' or again == 'y'):
            print('Thank you', namep1, 'for staying with us, we do appreciate it! ;)')
            game_play(namep1,namep2)
        elif (again == 'no' or again == 'n'):
            print('Thank you a lot for choosing us. It is more than appreciated! :)')
            again = 0
            if again == 0:
                return 0
            return 0
def main():
    print('Hello, this is Rock, Paper & Scissors for you!')
    namep1 = get_names()
    print("Now player 2 ")
    namep2 = get_names()
    while True:
        again = game_play(namep1, namep2)
        if again == 0:
            break


if __name__ == '__main__':
    main()
