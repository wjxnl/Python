numbers = [3, 2, 5, 6, 5, 9]

numbers2 = numbers.copy() #copied the number so original list is not affected.
print(numbers2)

numbers.append(20) #add an element
print(numbers)

numbers.insert(2, 10) #here, 2 is the index and 10 is the object you want to insert
print(numbers)

numbers.remove(3) #remove the element
print(numbers)

numbers.pop() #removes last element from the list
print(numbers)

print(50 in numbers)

print(numbers.count(5)) #counts the number of 5 in list

numbers.sort() #sorts in ascending order
numbers.reverse() #sorts in descending order
print(numbers)

numbers.clear() #removes all elements
print(numbers)