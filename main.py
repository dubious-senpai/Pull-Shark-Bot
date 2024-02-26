#
#...
#
#
#
#
#
# 
#
#
#
#
#


import time
import pyautogui

def click_and_wait(image_path, wait_time=3, confidence=0.7):
    try:
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if button_location is not None:
            pyautogui.click(button_location)
            print(f"Clicked '{image_path}' successfully!")
            time.sleep(wait_time)
            return True
        else:
            print(f"Failed to find '{image_path}' on the screen.")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}") 
        return False

# Example usage:
if __name__ == "__main__":
    # Adjust the confidence level as needed
    confidence_level = 0.9

    # Click the first image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 115317.png', confidence=confidence_level)

    # Click the second image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 115341.png', confidence=confidence_level)

    pyautogui.click()
    pyautogui.write(".")

    # Click the third image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 115444.png', confidence=confidence_level)

    # Click the fourth image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 115502.png', confidence=confidence_level)

    

    # Click the fifth image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 115514.png', confidence=confidence_level)

    pyautogui.scroll(-300)
    time.sleep(1)
    
   

    # Click the sixth image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 115536.png', confidence=confidence_level)

    pyautogui.scroll(-300)
    time.sleep(1)

    # Click the seventh image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 104137.png', confidence=confidence_level)

    

    # Click the eighth image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 104142.png', confidence=confidence_level)

    pyautogui.scroll(300)
    time.sleep(1)

    # Click the ninth image and wait 3 seconds
    click_and_wait('C:/Users/ur_username_here/Pictures/Screenshots/Screenshot 2024-02-26 115645.png', confidence=confidence_level)
