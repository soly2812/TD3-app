# app.py
import time
import os

# Set up the pony
pony_width, pony_height = 34, 14
pony_x, pony_y = 0, 5
pony_speed = 1

# Set up the terminal size
try:
    width, height = os.get_terminal_size().columns, os.get_terminal_size().lines
except OSError:
    # Default values if running inside a container without a terminal
    width, height = 80, 24

# Main game loop
while True:
    # Update pony position
    pony_x += pony_speed

    # Wrap around the terminal
    if pony_x > width:
        pony_x = -pony_width

    # Clear the terminal
    os.system('clear' if os.name == 'posix' else 'cls')

    # Draw the pony with color
    pony = [
        "                                 |\\    /|",
        "                              ___| \\,,/_/",
        "                           ---__/ \\/    \\",
        "                          __--/     (D)  \\",
        "                          _ -/    (_      \\",
        "                         // /       \\_ /  -\\",
        "   __-------_____--___--/           / \\_ O o)",
        "  /                                 /   \\__/",
        " /                                 /",
        "||          )                   \\_/\\",
        "||         /              _      /  |",
        " |      /--______      ___\\    /\\  :",
        "| /   __-  - _/   ------    |  |   \\ \\",
        " |   -  -   /                | |     \\ )",
        " |  |   -  |                 | )     | |",
        "  | |    | |                 | |    | |",
        "  | |    < |                 | |   |_/",
        "  < |    /__\\                <  \\",
        "  /__\\                       /___\\"
    ]

    for i in range(pony_height):
        print(' ' * pony_x + pony[i])

    # Pause for a short time to control the frame rate
    time.sleep(0.1)
