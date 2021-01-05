#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a Nested Loops program.


def fahrenheit():

    userinput = input("Enter the degrees you want to transform ")
    print("")

    try:
        userinput = int(userinput)
        if userinput >= 0:
            final = userinput * 1.8 + 32
            print("{}°C is equral to {}°F".format(userinput, final))
        else:
            print("You are not enter a positive integer")
    except Exception:
        print("It is not an integer")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
