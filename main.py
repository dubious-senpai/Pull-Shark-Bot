import pyautogui

def find_and_click_button(image_path, confidence=0.9):
    try:
        # Locate the button on the screen
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        
        if button_location is not None:
            # Click the button
            pyautogui.click(button_location)
            print("Button clicked successfully!")
        else:
            print("Button not found on the screen.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Replace 'button.png' with the path to the image of the button you want to find
    find_and_click_button(r'C:\Users\paul\Pictures\Screenshots\Screenshot 2024-02-26 104137.png')
