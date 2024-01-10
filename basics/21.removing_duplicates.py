numbers= [2, 5, 5, 3, 5, 6, 2, 1, 5]
uniques = [] #new list
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)