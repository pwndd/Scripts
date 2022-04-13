import time

timer = int(input('How many seconds do you want to count? '))
h = timer

for i in range(timer):
    print('Seconds left: ' + str(h))
    h -= 1
    time.sleep(1)

print('Done!')