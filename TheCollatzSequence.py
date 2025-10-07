# Practice Projects: The Collatz Sequence
'''
number = int(input('Enter number:'))
def collatz(num):
    a = number // 2
    b = 3 * number + 1
    if number % 2 == 0:
        print(a)
    elif number % 2 == 1:
        print(b)
'''
def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)
inputNumber = int(input('Enter number:\n'))
collatz(inputNumber)