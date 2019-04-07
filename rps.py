from random import randint

play = True
while play == True:
    player = input('rock (r), paper(p), or scissors(s)? \n')
    if player == 'r':
        print('0', end=' ')
    elif player == 'p':
        print('__', end=' ')
    elif player == 's':
        print('>8', end=' ')

    print(player, 'vs', end=' ')

    chosen = randint(1,3)

    if chosen == 1:
        computer = 'r'
        print('0', end=' ')
    elif chosen == 2:
        computer = 'p'
        print('__', end=' ')
    else:
        computer = 's'
        print('>8', end=' ')

    print(computer)

    if player == computer:
        print('DRAW!')
    elif player == 'r' and computer == 's':
        print('Player wins!')
    elif player == 'r' and computer == 'p':
        print('Computer wins!')
    elif player == 'p' and computer == 'r':
        print('Player wins!')
    elif player == 'p' and computer == 's':
        print('Computer wins!')
    elif player == 's' and computer == 'p':
        print('Player wins!')
    elif player == 's' and computer == 'p':
        print('Computer wins!')

    play_again = input("Would you like to play again?\n> ")
    if play_again == "no" or "No" or "NO" or 'n':
        play = False
        print("Bye!")
