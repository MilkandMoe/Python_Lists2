#Tasks1:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]


extract_temp_from_week2 = temperatures[6:13]
print(extract_temp_from_week2)


#Tasks2:

for temperature in temperatures:
    if temperature > 100:
        print(temperature)

#Tasks3:

reversed_temperatures = temperatures[::-1]
extract_temp_from_fifth_to_tenth_day = reversed_temperatures[4:11]
print(extract_temp_from_fifth_to_tenth_day)