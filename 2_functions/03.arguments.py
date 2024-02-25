def greet_user(first_name, last_name): #two parameters
    print(f'Hi, {first_name} {last_name}!') 
    print('Welcome') 
print('start')
greet_user("John", "Smith") #positional arguments
greet_user(last_name ="Smith", first_name ="Amy") #keyword arguments
print('Finish')