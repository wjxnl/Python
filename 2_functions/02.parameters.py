#parameters are placeholder that we define in our function for recieving information.
#arguments are the actual piece of information that we supply to these functions.

def greet_user(name): #defining a function ,, name is parameter
    print(f'Hi, {name}!') #this will only get executed when function is called.
    print('Welcome') 
print('start')
greet_user("John") #calling a function,, john is argument passed to the parameter name.
greet_user("Amyy") #reusing function
print('Finish')