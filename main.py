
import time
import pyautogui

number_of_pull_requests = 0

def pull_requests():

        pyautogui.click(254, 646)
        time.sleep(2)
        pyautogui.click(1737, 560)
        time.sleep(2)
        pyautogui.click(1239, 548)
        time.sleep(2)
        pyautogui.write(".")
        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        pyautogui.click(931, 806)
        time.sleep(3)
        pyautogui.click(1185, 926)
        time.sleep(5)
        for _ in range(3):
            pyautogui.scroll(-100)  # Negative value for scrolling down

        time.sleep(5)    
        pyautogui.click(1180, 940)
   
        time.sleep(5)
        for _ in range(3):
            pyautogui.scroll(-100)  # Negative value for scrolling down

        time.sleep(5)
        pyautogui.click(265, 869)
        time.sleep(5)
        pyautogui.click(265, 869)

        time.sleep(3)
        for _ in range(9):
            pyautogui.scroll(100)  # Negative value for scrolling down
        pyautogui.click(434, 240)


x = True

while x == True:
    pull_requests()
    number_of_pull_requests += 1
    print("=====================================================")
    print(f"Number of pull requests: {number_of_pull_requests}")
    print("=====================================================")
