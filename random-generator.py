import random
import sys
import string
import time
from faker import Faker

ex = Faker()
ip = ex.ipv4()

def spinning_cursor():
    while True:
        for cursor in '/-\|':
            yield cursor

spinner = spinning_cursor()

choice = input('Do you want to generate numbers, numbers + characters or fake IPs? (n/nc/ip): ')

if choice == 'n':
    num = int(input('How many numbers do you want to generate? '))
    st = int(input('What is the starting number? '))
    en = int(input('What is the ending number? '))
    times = int(input('How long do you want to wait after generating each number? '))

    for x in range(num):
        print('Number ' + str(x+1) + ': ' + str(random.randint(st,en)))
        x+=1
        for i in range(times):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
    print('Done!')

elif choice == 'nc':
    len = int(input('How many characters in the structure? '))
    how = int(input('How many structures? '))
    timez = int(input('How long do you want to wait after generating each structure? '))
    S = len

    for i in range(how):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        print('Structure ' + str(i+1) + ': ' + str(ran)) 
        i+=1

        for x in range(timez):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
    print('Done!')

elif choice == 'ip':
    num = int(input('How many IPs do you want to generate? '))
    times = int(input('How long do you want to wait after generating each number? '))

    for x in range(num):
        print(".".join(str(random.randint(0, 255)) for _ in range(4)))
        x+=1
        for _ in range(times):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
    print('Done!')

else:
    print('Something went wrong. Please try again.')
    sys.exit()