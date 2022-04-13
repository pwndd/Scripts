import sys
import time

def spinning_cursor():
    while True:
        for cursor in '/-\|':
            yield cursor

spinner = spinning_cursor()

timer = int(input('How many seconds do you want to count? '))
h = timer

for i in range(timer):
    print('Seconds left: ' + str(h))
    h -= 1
    for a in range(10):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

print('Done!')