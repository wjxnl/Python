secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the number:'))
    guess_count += 1
    if guess == secret_number:
        print('Your guess is correct.')
        break
else:
    print('Sorry, you failed.')
