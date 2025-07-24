from  random import randint
from sys import argv


def main():
    if (len(argv) == 3):
        min = int(argv[1])
        max = int(argv[2])
        generated_number = randint(min, max)
        while (1):
            try:
                number = int(input(f'enter your number between {min} and {max}: '))
                if not(min <= number <= max ):
                    print(f'Error: The number must be between {min} and {max}.')
                    continue
            except ValueError:
                print('enter a valid number')
                continue

            if (number == generated_number)  :
                print("congratulation you guess is correct")
                break
            else:
                print(f'wrong gess the random number is {generated_number} and the you number is {number}')

if (__name__ == "__main__"):
    main()
