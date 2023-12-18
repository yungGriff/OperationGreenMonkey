import pyautogui
import time
import keyboard
import datetime

# Function to click keys on the keyboard the specified number of times
def click_keys(keys, num_clicks):
    for _ in range(num_clicks):
        keyboard.press_and_release(keys)
        time.sleep(0.5)  # Adjust sleep time as needed

now = datetime.datetime.now()
#Session Counter Track the number of run throughs
sessionCounter = 0
#Monkey Monies Will only track session earnings
monkeyMonies = 0
# Hero coordinates
hero_coords = (707, 308)
#hero_coords = (573, 473)  -- End of the Road
superMonkey_coords = (715, 234)
#superMonkey_coords = (623, 429) -- End of the Road
ninja_coords = (708, 368)
#ninja_coords = (565, 523) -- End of the Road
# levelingMonkey = (577, 597)
levelingMonkey = (762, 368)
gamePlay = (1532, 829)
gameHome = (792, 726)
Next = (956, 765)
#starting the Game Coords.
homePlay = (864, 780)
Intermediate = (864, 780)
Expert = (1210, 817)
anotherBrick = (673, 332)
backOnePage = (501, 447)
endOTRoad = (1236, 323)
easy = (730, 437)
Deflation = (1168, 461)
OK = (951, 664)
while True:
# Delay before starting
    time.sleep(4)
    #Track the session activity
    sessionCounter = sessionCounter + 1
    print(sessionCounter, now) 
# Select Hero
    click_keys('u', 1)

# Pause for demonstration purposes
    time.sleep(1.5)

# Place Hero using mouse click
    pyautogui.moveTo(*hero_coords)
    time.sleep(1.5)

    pyautogui.click(button='left')
# Pause for demonstration purposes
# Pause for demonstration purposes
    time.sleep(1)

#Select Super Monkey.
    click_keys('s',1)
    time.sleep(1)
    pyautogui.moveTo(*superMonkey_coords)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.click(*superMonkey_coords, button='left')
    time.sleep(0.5)
    click_keys(',', 2)
    time.sleep(1)
    click_keys('/', 3)
#PLAY the game
    pyautogui.moveTo(*gamePlay)
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.click(*gamePlay, button='left')
    keyboard.press_and_release('esc')
    time.sleep(0.5)
#Select Ninja.
    click_keys('d',1)
    time.sleep(1)
    pyautogui.moveTo(*ninja_coords)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.click(*ninja_coords, button='left')
    time.sleep(0.5)
    click_keys(',', 1)
    time.sleep(0.5)
    click_keys(',', 1)
    time.sleep(0.5)
    click_keys(',', 2)
    time.sleep(1)
    click_keys('/', 1)
    time.sleep(1)
#Leveling Monkey Code Here
# Try implementing this into better paying game modes.
    """
    click_keys('d',1)
    time.sleep(1)
    pyautogui.moveTo(*levelingMonkey)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.click(*levelingMonkey, button='left')
    time.sleep(0.5)
    """

# Place Leveling monkey more time effective || Places the free dart monkey
    click_keys('q',1)
    time.sleep(1)
    pyautogui.moveTo(*levelingMonkey)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(0.5)
    
#Start New Match
    print(sessionCounter, now)
    monkeyMonies = monkeyMonies + 49
    print(monkeyMonies)
    pyautogui.moveTo(*Next)
    time.sleep(6 * 50)
    pyautogui.moveTo(*Next)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(0.5)

#Return home.
    pyautogui.moveTo(*gameHome)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(0.5)

#Start a game.
    time.sleep(5)
    pyautogui.moveTo(*homePlay)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(0.5)
#This is the easiest way to get to the End of the Road Map
    pyautogui.moveTo(*Expert)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(1)
#Go back to the page that has End of the Road
    pyautogui.moveTo(*backOnePage)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(0.5)
#Pick Map Another Brick in the Wall 
    pyautogui.moveTo(*anotherBrick)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(1)
#visual spacing now selecting easy -> deflation and starting
    time.sleep(0.5)
#Select Easy
    pyautogui.moveTo(*easy)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(1)
#Select Deflation
    pyautogui.moveTo(*Deflation)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(1)
    time.sleep(0.5)
#Select OK
    pyautogui.moveTo(*OK)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(6)
    pyautogui.click(button='left')