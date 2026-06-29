numbers = input("Enter numbers separated by space: ")

numbers = numbers.split()

unique = set(numbers)

print("Without duplicates:", unique)