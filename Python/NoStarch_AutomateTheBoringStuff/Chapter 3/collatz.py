import sys

def collatz(number):
    if (number % 2) == 0:
        number = number // 2
        print(str(number))
        return number
    else:
        number = 3 * number + 1
        print(str(number))
        return number

while True:
    try:
        print('Type an integer')
        collatzNumber = input()
        try:
            collatzNumber = int(collatzNumber)
            while collatzNumber != 1:
                collatzNumber = collatz(collatzNumber)
        except ValueError:
            print('Please enter an integer')
    except KeyboardInterrupt:
        sys.exit()