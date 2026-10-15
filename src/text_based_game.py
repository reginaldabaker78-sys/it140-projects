"""Project Two starter for the student's text-based adventure game."""

# Reginald A. Baker


def show_instructions():
    """Display the game objective and available commands."""
    print("Road to the Knockout")
    print("Collect all six boxing items before entering the Championship Ring.")
    print("Move commands: go north, go south, go east, or go west")
    print("Get-item command: get item")
    print("----------------------------------------")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("You are in the", current_room)
    print("Inventory:", inventory)
    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])
    print("----------------------------------------")
                  
        


def main():
    """Run the main gameplay loop."""
    # Stores each room, available directions, and collectible items
    rooms = {
        "Locker Room": {
            "north": "Championship Ring",
            "west": "Training Gym"
        },
        "Training Gym": {
            "north": "Equipment Room",
            "east": "Locker Room",
            "item": "Boxing Gloves"
        },
        "Equipment Room": {
            "north": "Coach's Office",
            "south": "Training Gym",
            "item": "Hand Wraps"
        },
        "Coach's Office": {
            "south": "Equipment Room",
            "east": "Conditioning Room",
            "item": "Fight Strategy"
        },
        "Conditioning Room": {
            "west": "Coach's Office",
            "east": "Medical Room",
            "item": "Water Bottle"
        },
        "Medical Room": {
            "west": "Conditioning Room",
            "south": "Warm-Up Room",
            "item": "Mouthguard"
        },
        "Warm-Up Room": {
            "north": "Medical Room",
            "west": "Championship Ring",
            "item": "Boxing Shoes"
        },
        "Championship Ring": {
            "east": "Warm-Up Room",
            "south": "Locker Room"
        }    
    }

    # Set the player's starting room and empty inventory
    current_room = "Locker Room"

    inventory = []

    show_instructions()
    # Continue the game until the player wins or loses
    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your command: ").lower().strip()
        # Process movement commands and update the current room
        if command.startswith("go "):
            direction = command[3:]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way.") 
        # Add the current room's item to the player's inventory        
        elif command == "get item":
                if "item" in rooms[current_room]:
                    item = rooms[current_room]["item"]
                    inventory.append(item)
                    del rooms[current_room]["item"]
                    print(item, "added to your inventory.")
                else:
                    print("There is no item in this room.")     
        else:
             print("Invalid command.")
        # Determine wheather the player wins or loses in the Championship Ring        
        if current_room == "Championship Ring":
            if len(inventory) == 6:
                print("You collected all six items and defeated Victor \"The Hammer\" Kane!")
                print("Congratulations! You are the new champion!")
                break
            else:
                print("You entered the Championship Ring before collecting all six items.")
                print("Victor \"The Hammer\" Kane knocks you out. Game over!")
                break              
                
    


if __name__ == "__main__":
    main()
