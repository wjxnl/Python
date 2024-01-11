customer= {
    "name": "anusha",
    "age": 19,
    "is_verified": True 
    #name, age etc is key value pairs and it should be unique
}
print(customer["name"]) 

print(customer.get("birthdate")) #it displays none, cause theres no such key pairs
print(customer.get("phone", "1234" )) #theres no such key, so we can supply default value to it.

customer["gender"] = "female" #using dictionary, we can easily add key value pairs.
print(customer["gender"])