#
#....
#
#
#
#
#
#
#

import pyautogui
import time
 
def find_and_click_button(image_path, confidence=0.9):
    try:
        # Locate the button on the screen
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        
        if button_location is not None:
            # Click the button
            pyautogui.click(button_location)
            print(f"Button at '{image_path}' clicked successfully!")
            return True
        else:
            print(f"Button at '{image_path}' not found on the screen.")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

# Click the first image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 115317.png')

# Click the second image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 115341.png')

# Press space
pyautogui.press('space')

# Click the third image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 115444.png')

# Click the fourth image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 115502.png')

# Click the fifth image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 115514.png')

# Scroll down three times
for _ in range(3):
    pyautogui.scroll(-100)

# Click the sixth image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 115536.png')

# Scroll down three times
for _ in range(3):
    pyautogui.scroll(-100)

# Wait for 5 seconds
time.sleep(5)

# Click the seventh image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 104137.png')

# Click the eighth image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 104142.png')

# Scroll back up
pyautogui.scroll(300)

# Press the ninth image
find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 115645.png')
