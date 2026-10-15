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
        print("You see a", rooms[current_room]["item])
    print('----------------------------------------")
                  
        


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.

    # TODO: Set the player's starting room.

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
