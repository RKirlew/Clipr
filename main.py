import pyautogui as pya
import keyboard
import pyperclip  # handy cross-platform clipboard text handler
import time
count=0
def copy_clipboard():
    return pyperclip.paste()

# double clicks on a position of the cursor
#pya.doubleClick(pya.position())

listT = list()

while len(listT)<9:
        
       
        try:
            if keyboard.is_pressed('1'):
                print("pressed")

                var=copy_clipboard()
                listT.append(var)
                
           
        except:
            break


print("1"+""+str(listT[0]))

print("3"+""+str(listT[2]))

print("5"+""+str(listT[4]))
print("7"+""+str(listT[6]))
print("9"+""+str(listT[8]))


while True:
    try:
        if keyboard.is_pressed('2'):
            pyperclip.copy(str(listT[0]))
        elif keyboard.is_pressed('3'):
             pyperclip.copy(str(listT[2]))
        elif keyboard.is_pressed('4'):
             pyperclip.copy(str(listT[4]))
        elif keyboard.is_pressed('5'):
             pyperclip.copy(str(listT[6]))
        elif keyboard.is_pressed('6'):
             pyperclip.copy(str(listT[8]))     
                           
    except:
        pass
