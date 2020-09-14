from room import Room
from player import Player


# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# make room variables instead

outside = Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")


# Link rooms together

outside.north_to = foyer
foyer.south_to = outside
foyer.north_to = overlook
foyer.east_to = narrow
overlook.south_to = foyer
narrow.west_to = foyer
narrow.north_to = treasure
treasure.south_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player()
player.current_room = outside


# Write a loop that:
while True:
    # * Prints the current room name
    print(player.current_room)
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    user_input = input('Where would you like to go?') 
    # If the user enters a cardinal direction, attempt to move to the room there.
    if user_input in {'north', 'south', 'east', 'west'}:
        # check if current room as a n_to attribute
        if hasattr(player.current_room, f'{user_input}_to'):
            # move the player to that room
            player.current_room = getattr(player.current_room, 
                                f'{user_input}_to')

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
