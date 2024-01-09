weight =int( input('Weight:'))
wt = input('(l)bs or (k)bs:')

if wt.upper() == "L" : #it converts users input to uppercase.
    weight_in_lbs = weight * 0.45
    print(f"You are {weight_in_lbs} kilos")
else :
    weight_in_kbs =  weight/0.45
    print(f"You are {weight_in_kbs} pounds.")

