def greet_user(first_name, last_name): #two parameters
    print(f'Hi, {first_name} {last_name}!') 
    print('Welcome') 
print('start')
greet_user("John", "Smith") #positional arguments
greet_user(last_name ="Smith", first_name ="Amy") #keyword arguments
greet_user("kim", last_name ="hyeri") # to mix positional and keyword arguments, we should always use positional arguments first and then keyword arguments
print('Finish')

