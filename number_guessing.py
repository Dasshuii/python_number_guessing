import random

def main():
    prompt = 'Guess the number between 1 and 100: '
    number_to_guess = random.randint(1, 100)
    guessed = False
    while (not guessed):
        number = get_user_input(prompt)
        if number == number_to_guess:
            print('Congratulations! You guessed the number!')
            guessed = True
        elif number > number_to_guess:
            print('Too high!')
        else:
            print('Too low!')

def get_user_input(prompt) -> int:
    try:
        print(prompt)
        number = int(input())
        return number
    except:
        print('Please type a number.')
        get_user_input(prompt)

if __name__ == '__main__':
    main()