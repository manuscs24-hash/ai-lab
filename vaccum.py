
room_A = input("Enter Room A status (Dirty/Clean): ").capitalize()
room_B = input("Enter Room B status (Dirty/Clean): ").capitalize()
location = input("Enter starting location (A/B): ").upper()

while True:

    if location == "A":

        if room_A == "Dirty":
            print("Room A is Dirty")
            print("Cleaning Room A")
            room_A = "Clean"
        else:
            print("Room A is Clean")
            print("Moving to Room B")
            location = "B"

    else:

        if room_B == "Dirty":
            print("Room B is Dirty")
            print("Cleaning Room B")
            room_B = "Clean"
        else:
            print("Room B is Clean")
            print("Moving to Room A")
            location = "A"

    if room_A == "Clean" and room_B == "Clean":
        print("Both rooms are Clean")
        print("Goal Achieved!")
        break
    