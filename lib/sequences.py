#!/usr/bin/env python3

def print_fibonacci(length):

    fib_list = [0,1]

    if (length == 0):
        fib_list.clear()
    elif (length == 1):
        del(fib_list[1])
    elif (length == 2):
        fib_list
    else:
        i = 1
        while i <= (length-2):
            fib_list.append(fib_list[i]+fib_list[i-1])
            i += 1 

    print (fib_list)

