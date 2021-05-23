command = ''
started = False
stopped = True

while True:
    command = input("<").lower()
    if command == 'start':
        if started:
            print("Car is already started.")
        else:
            started = True
            stopped = False
            print('the car started ')
    elif command == 'stop':
        if stopped:
            print("Car is already stopped.")
        else:
            started = False
            stopped = True
            print('the car stopped')
    # elif command == 'help':
    elif "help" in command:
        print("""
start- to start the car.
stop-to stop the car.
quit-to quit the game.
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry! i don't understand that")