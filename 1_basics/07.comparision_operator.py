name = input('Enter a name::')
length_of_name = len(name)

if length_of_name<3 :
    print('Name must be at least three characters long.')

elif length_of_name>50 :
    print("Name can be of maximum 50 characters.")

else:
    print('Name looks good!')
