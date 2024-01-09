course = 'This course name is python'
print (course[5]) # space also takes index.
print (course[-1]) # negative index gives character from the end.
print (course[0]) # index of the first character is zero. 
print (course[0:1]) # it returns all the characters starting with the first index all the way to second index, but it doesnt return thr character at second index.
print (course[:]) #it clones the string.
print (course[2:]) # it will return all the characters to the last index.
print (course[:3]) # if we dont supply starting index, it will assume zero.
print (course[1:-1]) 

print(len(course))
print(type(course))