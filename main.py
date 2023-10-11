import pyautogui
import time
import keyboard

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
