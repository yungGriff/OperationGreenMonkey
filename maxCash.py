import pyautogui
import time
import keyboard
import datetime
import win32api, win32con
import cv2
from PIL import ImageGrab
import numpy as np


# Function to click keys on the keyboard the specified number of times
def click_keys(keys, num_clicks):
    for _ in range(num_clicks):
        keyboard.press_and_release(keys)
        time.sleep(0.5)  # Adjust sleep time as needed

# Function to click on the bad popup
def click_on_bad_popup(match_location, template_size):
    try:
        # Extract the match location
        click_x = match_location[0] + template_size[0] // 2
        click_y = match_location[1] + template_size[1] // 2
        pyautogui.click(click_x, click_y)
        print(f"Clicked at ({click_x}, {click_y})")
    except Exception as e:
        print(f"Error while clicking: {e}")

# Function to check if bad popup is present

def is_bad_popup_present():
    try:
        # Capture screenshot using PIL
        screenshot = ImageGrab.grab()
        screenshot_np = np.array(screenshot)

        # Load the template image
        template = cv2.imread('testerPopUp.png', cv2.IMREAD_GRAYSCALE)

        # Get template size
        template_size = template.shape[:2]

        # Convert images to grayscale
        gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

        # Apply template matching
        result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # Set a threshold for considering a match
        threshold = 0.7
        if max_val >= threshold or max_val == 1.0:
            return max_loc, template_size
        else:
            return None, None
    except Exception as e:
        print(f"Error in is_bad_popup_present: {e}")
        return None, None



# Session Counter Track the number of run throughs
sessionCounter = 0
bad_popup_check_counter = 0
#Changing this value for testing... ATTENTION
sessions_before_check = 5
imageFinder_counter = 0
bad_Checks_before_continue = 3
# Monkey Monies Will only track session earnings
monkeyMonies = 0
# Hero coordinates
hero_coords = (734, 303)
# hero_coords = (573, 473)  -- End of the Road (733, 266)
superMonkey_coords = (741, 222)
# superMonkey_coords = (623, 429) -- End of the Road 735, 234
ninja_coords = (727, 368)
# ninja_coords = (565, 523) -- End of the Road (727, 368)
# levelingMonkey = (577, 597)
levelingMonkey = (855, 368)
gamePlay = (1560, 819)
gameHome = (792, 726)
Next = (979, 749)
# starting the Game Coords.
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
    now = datetime.datetime.now()
    time.sleep(2)
    # Track the session activity
    sessionCounter = sessionCounter + 1
    print(sessionCounter)
    print(" ", now)

    # Check for bad popup
    if bad_popup_check_counter % sessions_before_check == 0:
        try:
          while imageFinder_counter < bad_Checks_before_continue:
            match_location, template_size = is_bad_popup_present()
            if match_location is not None:
                print("Pop Up image found. Clicking on it.")
                click_on_bad_popup(match_location, template_size)
                time.sleep(.5)
                pyautogui.click()
                time.sleep(1)
                imageFinder_counter += 1
            else:
                print("Pop up not found.")
                break
        except KeyboardInterrupt:
            print("Recognition stopped")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            #reset the sessions counter
            bad_popup_check_counter = 0
            imageFinder_counter = 0
            pyautogui.moveTo(*OK)
            pyautogui.click(button='left')
    bad_popup_check_counter += 1
    #Delay before starting
    time.sleep(3)
    # Select Super Monkey.
    click_keys('s', 1)
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
    # PLAY the game
    """
    Thinking about implementing this approach to starting the game. I believe it may be considerably faster and doable without any down time and while placing the next Monkey Tower.
    
    click_keys('space', 2)
    """
    pyautogui.moveTo(*gamePlay)
    pyautogui.click(button='left')
    time.sleep(0.5)
    pyautogui.click(*gamePlay, button='left')
    keyboard.press_and_release('esc')
    time.sleep(0.5)

    # Select Hero
    click_keys('u', 1)
    # Pause for demonstration purposes
    time.sleep(1)
    # Place Hero using mouse click
    pyautogui.moveTo(*hero_coords)
    time.sleep(1)
    pyautogui.click(button='left')
    # Pause for demonstration purposes
    time.sleep(1)


    # Select Ninja.
    click_keys('d', 1)
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
    # Leveling Monkey Code Here
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
    click_keys('q', 1)
    time.sleep(1)
    pyautogui.moveTo(*levelingMonkey)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(0.5)

    # Start New Match
    # print(sessionCounter, now)  -- With the current implementation this line would print the same minute.
    monkeyMonies = monkeyMonies + 49
    print(monkeyMonies)
    pyautogui.moveTo(*Next)
    time.sleep(6 * 48)
    pyautogui.moveTo(*Next)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(0.5)

    # Return home.
    pyautogui.moveTo(*gameHome)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(0.5)

    # Start a game.
    time.sleep(3.8)
    pyautogui.moveTo(*homePlay)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(0.5)
    # This is the easiest way to get to the End of the Road Map
    pyautogui.moveTo(*Expert)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(1)
    # Go back to the page that has End of the Road
    pyautogui.moveTo(*backOnePage)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(0.5)
    # Pick Map Another Brick in the Wall
    pyautogui.moveTo(*anotherBrick)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(1)
    # visual spacing now selecting easy -> deflation and starting
    time.sleep(0.5)
    # Select Easy
    pyautogui.moveTo(*easy)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(1)
    # Select Deflation
    pyautogui.moveTo(*Deflation)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(1)
    time.sleep(0.5)
    # Select OK
    pyautogui.moveTo(*OK)
    time.sleep(0.5)
    pyautogui.click(button='left')
    time.sleep(5)
    pyautogui.click(button='left')

