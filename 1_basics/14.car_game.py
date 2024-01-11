command = ""
started = False
while True :
    command = input('>').lower()
    if command == "help" :
        print ("""
start- to start the car
stop- to stop the car
quit- to exit
        """)
    elif command == "start" :
        if started:
            print ("car is already starteedddddddd.")           
        else:
            started = True
            print("car started...Ready to go.")
    elif command == "stop":
        if not started:
            print("car is already stopped.")
        else:
            started = False
            print("Car is stopped.")
    elif command =="quit":
        break
    else:
        print("Sorryyy, but i do not understand this.")

