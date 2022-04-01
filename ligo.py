import pyautogui
import time

dellin = "https://www.dellin.ru/"
whr = input("(1-МСК,2-ЕКБ,3-СПБ,4-КЗН-ТАТАР)Откуда:")
whr_to = input("(1-МСК,2-ЕКБ,3-СПБ,4-КЗН-ТАТАР)Куда:")

def check_int(potential_int):
    try:
        float(potential_int)

        return True
    except ValueError:

        return False
def box2(chc2):
        pyautogui.click(379,426)
        if int(chc2) == 1:
            pyautogui.click(322,514)
            time.sleep(1)
        elif int(chc2) == 2:
            pyautogui.click(322,647)
            time.sleep(1)
        elif int(chc2) == 3:
            pyautogui.click(322,564)
            time.sleep(1)
        elif int(chc2) == 4:
            pyautogui.click(322,607)
            time.sleep(1)
def box1(chc1):
        pyautogui.click(379,358)
        if int(chc1) == 1:
            pyautogui.click(322,459)
            time.sleep(1)
        elif int(chc1) == 2:
            pyautogui.click(322,579)
            time.sleep(1)
        elif int(chc1) == 3:
            pyautogui.click(322,495)
            time.sleep(1)
        elif int(chc1) == 4:
            pyautogui.click(322,535)
            time.sleep(1)
        
if check_int(whr) == False or check_int(whr_to) == False:
    print("Invalid Input. Please check if you chose between 1-4")
else:
    if int(whr) > 4 or int(whr) < 1 or int(whr_to) > 4 or int(whr_to) < 1:
        print("Invalid Input. Please check if you chose between 1-4")
    else:
        time.sleep(2)
        pyautogui.click(405,49)
        time.sleep(1)
        pyautogui.typewrite(dellin)
        pyautogui.press("enter")
        time.sleep(5) #dont forget to put 10 later
        pyautogui.click(379,358)
        time.sleep(1)
        box1(whr)
        box2(whr_to)
        pyautogui.screenshot("dellin_ab_1p.png")
        