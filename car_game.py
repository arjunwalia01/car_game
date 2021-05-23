command=''
while True:
    command=input("<").lower()
    if command=='start':
        print('the car started ')
    elif command=='stop':
        print('the car stopped')
    elif command=='help':
        print("""
start- to start the car.
stop-to stop the car.
quit-to quit the game.
        """)
    elif command=='quit':
        break
    else:
        print("Sorry! i don't understand that")