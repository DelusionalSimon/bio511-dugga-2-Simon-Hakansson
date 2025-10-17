

# Input data
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4] 



def absoluteSum(numbers:list[int]) -> int:
    sum = 0
    for number in numbers:
        if abs(number) >= 10:
            sum += number
    return sum

print(f"the sum of numbers with an absolute value over 10 is {absoluteSum(numbers)}")