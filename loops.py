

# Input data
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
    @brief:     Makes a list of of all negative numbers in a list

    @param:     numbers A list of integers to check
    @return:    A list of negative integers
    """
    cubeList = []
    for number in numbers:
        if number < 0:
            cubeList.append(number)
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

print(f"the sum of numbers with an absolute value over 10 is {absoluteSum(numbers)}")
print(negativeCubes(numbers))
absoluteRepeat(numbers)

