#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program calculates the circumference of a circle

import math
import constants


def main():
    pizza_size = int(input("What size of pizza do you want in inches?"))
    cost = 0.5 * (pizza_size) + 1.75
    print()
    print("Cost: ${:,.2f}".format(cost))
    print("HST: ${:,.2f}".format(cost * constants.HST))
    print("Cost: ${:,.2f}".format(cost + cost * constants.HST))


if __name__ == "__main__":
    main()
