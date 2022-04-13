import random, sys

#score keeping
wins = 0
losses = 0
ties = 0

while True: #main loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #quit program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')

    #display input
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus...')

    #display computer choice
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    #display and record result
    if playerMove == computerMove:
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose')
        losses = losses + 1