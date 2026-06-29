numbers = [12, 45, 7, 89, 23]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum number =", maximum)