#Tasks1:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

#Tasks2:


numbers_greater_than_five = []
for number in numbers:
    if number > 5:
        numbers_greater_than_five.append(number)       
print(numbers_greater_than_five)


#Tasks3:

for number in numbers:
    if number == 7:
        print("Number seven in numbers list")