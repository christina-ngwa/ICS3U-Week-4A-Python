#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program shows the greatest number
#    with user input


def main():
    # This function shows the greatest number
    greatest_num = 0

    print("Welcome to the greatest number teller!")
    print("")
    first_num_as_string = input("Enter the first number: ")

    # process & output
    try:
        first_num = int(first_num_as_string)
        if first_num > greatest_num:
            greatest_num = first_num
        else:
            pass
        second_num_as_string = input("Enter the second number: ")
        try:
            second_num = int(second_num_as_string)
            if second_num > greatest_num:
                greatest_num = second_num
            else:
                pass
            third_num_as_string = input("Enter the third number: ")
            try:
                third_num = int(third_num_as_string)
                if third_num > greatest_num:
                    greatest_num = third_num
                else:
                    pass
                print("")
                print("The greatest number is", greatest_num, ".")
            except Exception:
                print("Wrong input. Try again.")
        except Exception:
            print("Wrong input. Try again.")
    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
