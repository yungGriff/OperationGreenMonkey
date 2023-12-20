import pyautogui
import time
import datetime
import cv2
import numpy as np
from PIL import ImageGrab

"""
# Function to click keys on the keyboard the specified number of times
def click_keys(keys, num_clicks):
    for _ in range(num_clicks):
        keyboard.press_and_release(keys)
        time.sleep(0.5)  # Adjust sleep time as needed

#starting the Game Coords.
homePlay = (864, 780)
Intermediate = (864, 780)
backOnePage = (501, 447)
endOTRoad = (1236, 323)
easy = (730, 437)
Deflation = (1168, 461)
OK = (951, 664)

time.sleep(5)

pyautogui.moveTo(*homePlay)
time.sleep(1)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(*Intermediate)
time.sleep(0.5)
pyautogui.click(button='left')
time.sleep(1)
pyautogui.moveTo(*backOnePage)
time.sleep(0.5)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(*endOTRoad)
time.sleep(0.5)
pyautogui.click(button='left')
time.sleep(1)
#visual spacing now selecting easy -> deflation and starting
time.sleep(0.5)
pyautogui.moveTo(*easy)
time.sleep(0.5)
pyautogui.click(button='left')
time.sleep(1)
pyautogui.moveTo(*Deflation)
time.sleep(0.5)
pyautogui.click(button='left')
time.sleep(1)
time.sleep(0.5)
pyautogui.moveTo(*OK)
time.sleep(0.5)
pyautogui.click(button='left')
time.sleep(6)
pyautogui.click(button='left')



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   
"""


def is_bad_popup_present():
    #screenshot = pyautogui.screenshot()
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)

    if screenshot_np.dtype != np.uint8:
        screenshot_np = screenshot_np.astype(np.uint8)

    template = cv2.imread('badPopUpBTD.png')

    # convert images to grayscale
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    # init ORB detector
    # Apply template matching
    result = cv2.matchTemplate(gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Adjust this threshold as needed
    loc = np.where(result >= threshold)

    # If there are matches, consider the popup is present
    if len(loc[0]) > 0:
        return True
    else:
        return False


# homeScreen_image = 'homeScreen.png'
# print("Pillow", PIL.Image.__version__)
try:
    while True:
        x, y = pyautogui.position()
        if is_bad_popup_present():
            print("Pop Up image found.")
            time.sleep(1)
        print(f"Mouse position x={x}, y={y}")
        now = datetime.datetime.now()
        print(" ", now)
        time.sleep(2)
        #print(cv2.__version__)

except KeyboardInterrupt:
    print("Mouse tester stopped")
