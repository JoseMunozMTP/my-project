for numero in range(0,101):

    if numero % 3 == 0 and numero % 5 == 0:
        print ('Fizz - Buzz')
    elif numero % 3 == 0:
        print ('Fizz')
    elif numero % 5 == 0:
        print('Buzz')
    else:
        print(numero)
