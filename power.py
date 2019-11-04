#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Oct 2019
# This programe calculates the square (power of 2) of each integer
# from 0 to this number

import math


def main():
    # This program squares the number from 0-your number

    print("This programe calculates the square (power of 2) of each integer"
          "from 0 to this number: ")

    # input
    number = int(input("Please put in number: "))
    counter = 0
    total = 0

    # process and output
    for counter in range(number+1):
        total = counter**2
        print("{0}²={1}".format(counter, total))


if __name__ == "__main__":
    main()
