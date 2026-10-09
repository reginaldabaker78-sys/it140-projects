"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# The player begins the gane in the Great Hall.
current_room = "Great Hall"
# Keep the game running until the player chooses exit.
while current_room != "exit":
    # Display the player's current location.
    print("You are in the", current_room)
    # Ask for direction and standardize the input.
    command = input("Enter a direction (north, south, east, west) or exit: ") .lower().strip()
    # End the game when the player chooses to exit.
    if command == "exit":
        current_room = "exit"
    # Move the player only if the direction is valid.
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
    # Keep the player in the room for invald input.
    else:
        print("Invalid direction. Please try again.")



