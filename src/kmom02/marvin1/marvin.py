#!/usr/bin/env python3
# ruff: noqa
# -*- coding: utf-8 -*-
"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""


def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
                    Θ
                   ╞|╡
                   ╞|╡
                Θ==[Φ]==Θ
                   |||
                   |||
                   |||
                   |||
                   |||
                   \|/

         _.--~~.--._ _.--~~.--._
        |-.~_--.~.._╪-.~_--.~..~|
        |..--~~--..~╪..--~~--..-|
        |.-~~~.-.--\|/.-~~~.-.~-|
        └=========\\|//=========┘
    """


def menu():
    """
    Display the menu with the options that the entity can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage())
    print("Hi, I'm the entity. I know it all. What can I do you for?")
    print("1) Present yourself to the entity.")
    print("2) Celcius to farenheit")
    print("3) Calculate grade.")
    print("4) Is smaller, bigger or equal.")
    print("5) Check SSN")
    print("6) rovarspraket")
    print("A1) Check if all letters in a word.")
    print("A2) Match brackets.")
    print("q) quit.")


def myNameIs():
    """
    Read the users name and say hello to the entity.
    """
    name = input("What is your name? ")
    print("\nThe entity says:\n")
    print("Hello %s - a pleasure to encounter you!" % name)
    print("Know the answere to the magic question 1+1, and i will grant you knowledge if asked!")


def quitIt():
    """
    function for quitting the entity
    """
    print("Bye, bye - and welcome back anytime!")


def invalid():
    """
    function for invalidating the input
    """
    print("That is not a valid choice. You can only choose from the menu.")


def celToFar():
    """
    converts celcius to farenheit
    """
    celc = input("Tell me the real temperature and i shall return the pretend temperature... ")
    farenheit = round(float(celc) * 9 / 5 + 32, 2)
    print("The make believe temperature(farenheit) is {0} degrees".format(farenheit))


def gradesConv():
    """
    converts points to grades
    """
    maxP = input("Enter the max point")
    currP = input("Enter your points... ")
    grade = ""
    maxP = int(maxP)
    currP = int(currP)

    if currP > maxP:
        grade = "F, because you failed to type in your points correctly!"
    elif currP >= maxP * 0.9:
        grade = "A"
    elif currP >= maxP * 0.8:
        grade = "B"
    elif currP >= maxP * 0.7:
        grade = "C"
    elif currP >= maxP * 0.6:
        grade = "D"
    else:
        grade = "F"
    print("You will recieve the score: {0}".format(grade))


def nextNr():
    """
    tells comparson of number to previous number
    """
    currNr = 0
    lastNr = None
    lastNr = int(input("Feed me a number, or write done... "))
    while True:
        inp = input("Feed me a number, or write done... ")
        try:
            currNr = int(inp)
            if currNr > lastNr:
                print("{0} is larger! than {1}".format(str(currNr), str(lastNr)))
            elif currNr < lastNr:
                print("{0} is smaller! than {1}".format(str(currNr), str(lastNr)))
            else:
                print("{0} is same! to {1}".format(str(currNr), str(lastNr)))
            lastNr = currNr
        except ValueError:
            if inp == "done":
                break
            elif lastNr is None and int(currNr):
                lastNr = currNr
            else:
                print("Thats not a number!")


def validate_ssn():
    """
    luhan 10 algo
    """
    nrs = input("Enter ssn to validate: ")
    nrs = nrs.replace("-", "")
    multiplicative = 2
    total = 0
    for n in nrs:
        tmp = int(n) * multiplicative
        if tmp > 9:
            total += int(str(tmp)[0]) + int(str(tmp)[1])
        else:
            total += tmp
        multiplicative = 1 if multiplicative == 2 else 2
    if not total % 10:
        print("Valid")
    else:
        print("Not valid")


# def rovarsprak():
#     """
#     Turn word into rovarspraket
#     """
#     woworordod = str()
#     original = input("Skriv in ett ord > ")

#     if len(original) > 0 and original.isalpha():
#         word = original.lower()

#         letter_index = 0

#         while letter_index <= len(word) - 1:
#             letter = word[letter_index]

#             if letter in "aeiouy":
#                 woworordod = woworordod + letter
#                 letter_index = letter_index + 1

#             else:
#                 woworordod = woworordod + letter + "o" + letter
#                 letter_index = letter_index + 1
#     print(woworordod)


# def A1():
#     """
#     Check if all letters from input is in other string
#     """
#     word = input("Give me a word: ").lower()
#     letters = input("Give letters to check for in word: ")
#     for l in letters:
#         if word.count(l) < letters.count(l):
#             print("No match!")
#             return
#     print("Match!")
#     return


# def A2():
#     """_"""
#     number = int(input("Enter a number: "))
#     no_mult = int(input("Enter the number of times to multiply: "))
#     match = False
#     product = number
#     count = 0
#     while not match and count < no_mult:
#         for i in range(0, 10, 1):
#             if str(i) in str(product):
#                 match = True
#             else:
#                 match = False
#                 break
#         if not match:
#             count += 1
#             product = product * 2
#     if count == no_mult:
#         print("\nMarvin says: -1 times")
#     else:
#         print("\nMarvin says: " + str(count) + " times (" + str(product) + ")")


# def A3():
#     """A4"""
#     name1 = input("Enter the first name: ")
#     name2 = input("Enter the second name: ")
#     new_name = ""
#     vowels = "aeiouy"
#     for letter in name1:
#         if letter in vowels:
#             place = name1.find(letter)
#             new_name = name1[:place]
#             break
#     for letter in name2:
#         if letter in vowels:
#             place = name2.find(letter)
#             new_name += name2[place:]
#             break

#     print("\nMarvin says: " + new_name)


# def A4():
#     """A5"""
#     point_string = input("Input a string: ")  # "a2b4A5s3B1"
#     final_str = ""
#     used_letters = ""
#     lowercase = point_string.lower()

#     for letter in lowercase:
#         result = 0
#         if letter in used_letters or letter.isdigit():
#             continue
#         used_letters += letter
#         for i, char in enumerate(point_string):
#             if char == letter:
#                 point = int(point_string[i + 1])
#                 result += point
#             elif char == letter.upper():
#                 point = -int(point_string[i + 1])
#                 result += point
#         final_str += letter + " " + str(result) + ", "
#     print(final_str[:-2])


# while True:
#     menu()
#     choice = input("--> ").lower()

#     if choice == "q":
#         quitIt()
#         break

#     elif choice == "1":
#         myNameIs()

#     elif choice == "2":
#         celToFar()

#     elif choice == "3":
#         gradesConv()

#     elif choice == "4":
#         nextNr()
#     elif choice == "5":
#         validate_ssn()
#     elif choice == "6":
#         rovarsprak()

#     elif choice == "a1":
#         A1()

#     elif choice == "a2":
#         A2()

#     elif choice == "a3":
#         A3()

#     elif choice == "a4":
#         A4()

#     elif choice == "a5":
#         A5()

#     else:
#         invalid()

#     input("\nThe knowledge has been granted. Now go bother someone else...")
