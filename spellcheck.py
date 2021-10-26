# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import math # Needed for binary search function
import time # Needed to determine how long the program takes to run


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    while True:
        selection = Menu()
        if selection == 1: # Linear search on inputted word
            word = input("Please enter a word: ")
            print("")
            print("Linear Search starting...")

            startTime = time.time()
            index = LinearSearch(dictionary, word)
            endTime = time.time() - startTime

            if index == -1:
                print(f"{word} is not in the dictionary. ({endTime}) seconds.\n")
            else:
                print(f"{word} is in the dictionary at position {index}. {endTime} seconds.\n")
            continue

        elif selection == 2: # Binary search on inputted word
            word = input("Please enter a word: ")
            print("")
            print("Binary Search starting...")
            startTime = time.time()
            index = BinarySearch(dictionary, word)
            endTime = time.time() - startTime

            if index == -1:
                print(f"{word} is not in the dictionary. ({endTime}) seconds.\n")
            else:
                print(f"{word} is in the dictionary at position {index}. ({endTime}) seconds.\n")
            continue

        elif selection == 3: # Linear Search on Alice in Wonderland
            print("")
            print("Linear Search starting...")

            wordsNotInDic = 0
            startTime = time.time()
            for i in range(len(aliceWords)):
                result = LinearSearch(dictionary, aliceWords[i].lower())
                if result == -1:
                    wordsNotInDic += 1
            
            endTime = time.time() - startTime
            print(f"Number of words not found in dictionary: {wordsNotInDic}. ({endTime}) seconds.\n")
            continue
            
        elif selection == 4: # Binary Search on Alice in Wonderland
            print("")
            print("Binary Search starting...")

            wordsNotInDic = 0
            startTime = time.time()
            for i in range(len(aliceWords)):
                if BinarySearch(dictionary, aliceWords[i].lower()) == -1:
                    wordsNotInDic += 1
            
            endTime = time.time() - startTime
            print(f"Number of words not found in dictionary: {wordsNotInDic}. ({endTime}) seconds.\n")
            continue

        elif selection == 5: # Ends the program
            return 1

        else:
            selection = input("Enter a number between 1 and 5.")
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def Menu():
    print("Main Menu")
    print("1: Spell Check a Word (Linear Search)")
    print("2: Spell Check a Word (Binary Search")
    print("3: Spell Check Alice in Wonderland (Linear Search)")
    print("4: Spell Check Alice in Wonderland (Binary Search")
    print("5: Exit")
    selection = input("Enter Menu Selection (1-5): ")
    return int(selection)
# End of Menu

def LinearSearch(anArray, item):
    for i in range(len(anArray)):
        if item == anArray[i]:
            return i
    return -1
# End of LinearSearch

def BinarySearch(anArray, item):
    lowerBound = 0
    upperBound = len(anArray) - 1

    # Stayed close to the pseudocode.
    while(lowerBound <= upperBound):
        middleIndex = (lowerBound + upperBound) // 2
        if item == anArray[middleIndex]:
            return middleIndex
        elif item < anArray[middleIndex]:
            upperBound = middleIndex - 1
        else:
            lowerBound = middleIndex + 1

    return -1
# End of BinarySearch

# def BinarySearch(anArray, item):
#     lowerBound = 0
#     upperBound = len(anArray) - 1

#     # Stayed close to the pseudocode.
#     while(True):
#         middleIndex = math.floor((lowerBound + upperBound) / 2)
#         if item == anArray[middleIndex]:
#             return middleIndex
#         elif lowerBound >= upperBound:
#             break
#         elif item < anArray[middleIndex]:
#             upperBound = middleIndex - 1
#         else:
#             lowerBound = middleIndex + 1

#     return -1
# # End of BinarySearch

# Call main() to begin program
main()