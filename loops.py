

# Input data
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4] 


# ----------[FUNCTIONS]----------
def absoluteSum(numbers:list[int]) -> int:
    sum = 0
    for number in numbers:
        if abs(number) >= 10:
            sum += number
    return sum

def negativeCubes(numbers:list[int]) -> list[int]:
    cubeList = []
    for number in numbers:
        if number < 0:
            cubeList.append(number)
    return cubeList

def absoluteRepeat(numbers:list[int]) -> None:
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

