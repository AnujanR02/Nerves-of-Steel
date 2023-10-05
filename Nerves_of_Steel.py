"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is is the game "Nerves of Steel"


import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random  # The random library has a choice function that will choose a random number within the set range

# At the start of the program, all players stand
print("Players stand")

# This sets the amount of time the program sleeps for within the range of 5 to 25 seconds
sleep_time = (random.choice(range(5,25)))

time.sleep(sleep_time)

# After the selected time is up, the following is shown
print('Times up! Last to sit down wins.')

