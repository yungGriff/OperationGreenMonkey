import pyautogui
import time
import datetime
import cv2
import numpy as np
from PIL import ImageGrab


def just_press_play():
    try:
        # Capture screenshot using PIL
        screenshot = ImageGrab.grab()
        screenshot_np = np.array(screenshot)

        # Load the template image
        template = cv2.imread('playButton.png', cv2.IMREAD_GRAYSCALE)

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
        if just_press_play():
            match_location, template_size = just_press_play()
            if match_location is not None:
                click_on_bad_popup(match_location, template_size)
                time.sleep(.5)
                pyautogui.click()
                time.sleep(1)
        #print(cv2.__version__)

except KeyboardInterrupt:
    print("Mouse tester stopped")