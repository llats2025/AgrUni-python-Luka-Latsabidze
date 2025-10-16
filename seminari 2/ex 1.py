secret = 7
guess = int(input('guess the number'))
while guess != secret:
    print('wrong number')
    guess = int(input('try again'))

print('correct.')