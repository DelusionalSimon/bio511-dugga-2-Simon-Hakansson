"""!
@file       loops.py
@author     Simon Håkansson
@date       2025-10-17
@brief      A Module containing three functions that operate on a list of integers 

@details    This module was created to complete the second Dugga of the BIO511
            It contains functions that operate on a list on integrers 
"""


# ----------[INPUT]----------
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4] 


# ----------[FUNCTIONS]----------
def absoluteSum(numbers:list[int]) -> int:
    """!
    @brief:     Calculates the sum of numbers with an absolute value over 10

    @param:     numbers A list of integers to check
    @return:    The sum of integers with an absolute value over 10
    """
    sum = 0
    for number in numbers:
        if abs(number) >= 10:
            sum += number
    return sum

def negativeCubes(numbers:list[int]) -> list[int]:
    """!
    @brief:     Makes a list of of the cube of all negative numbers

    @param:     numbers A list of integers to check
    @return:    A list of cubed negative integers
    """
    cubeList = []
    for number in numbers:
        if number < 0:
            cubedNumber = number ** 3
            cubeList.append(cubedNumber)
    return cubeList

def absoluteRepeat(numbers:list[int]) -> None:
    """!
    @brief:     Prints the first occurence of an absolute repeat

    @details:   Takes a list of integers as input and checks for
                absolute repeats. Once a repeat is found its
                value is printed and the function exits. if no 
                repeats are found it prints "No repeats"


    @param:     numbers A list of integers to check
    """
    checked = []
    numberFound = False
    for number in numbers:
        if abs(number) in checked and not numberFound:
            print(number)
            numberFound = True
        else:
            checked.append(abs(number))
    # If no repeats found 
    if not numberFound:
        print("No repeats")



# ----------[MAIN]----------
if __name__ == "__main__":

    print(f"the sum of numbers with an absolute value over 10 is {absoluteSum(numbers)}")

    print(f"These are the cubes of all negative numbers in the input: \n{negativeCubes(numbers)}")

    print("This is the first occurence of a repeat of an absolute value:")
    absoluteRepeat(numbers)

