#!/usr/bin/env python3

if __name__ == '__main__':
    for i in range(0,100,1):
        print(str(i) + ' ', end='')
        if (i%3) == 0:
            print('fizz', end='')
        if (i%5) == 0:
            print('buzz', end='')
        print('')
