import pyautogui as pya
import keyboard
import winsound
from threading import Thread
import pyperclip  # handy cross-platform clipboard text handler
import time
count=0
def copy_clipboard():
    return pyperclip.paste()

# double clicks on a position of the cursor
#pya.doubleClick(pya.position())

listT = list()
def checkPress():
    #global listT
    
    while True:
        
       
        try:   
            if keyboard.is_pressed('1'):
                    pyperclip.copy(str(listT[0]))
            elif keyboard.is_pressed('2'):
                 pyperclip.copy(str(listT[2]))
            elif keyboard.is_pressed('3'):
                 pyperclip.copy(str(listT[4]))
            elif keyboard.is_pressed('4'):
                 pyperclip.copy(str(listT[6]))
            elif keyboard.is_pressed('5'):
                 pyperclip.copy(str(listT[8])) 
        except:
            pass
                               
        

def copyClip():
    global listT
    while True:
            

            
            try:
                if keyboard.is_pressed('ctrl+c'):
                    print("pressed")

                    var=copy_clipboard()
                    listT.append(var)
                    if len(listT)==8:
                        winsound.MessageBeep()
                    if len(listT)==11:
                        print("1"+""+str(listT[0]))

                        print("3"+""+str(listT[2]))

                        print("5"+""+str(listT[4]))
                        print("7"+""+str(listT[6]))
                        print("9"+""+str(listT[8]))
                        
                        listT.clear()
                        #print(len(listT))
                        var=copy_clipboard()
                        listT.append(var)
                if keyboard.is_pressed('='):
                    listT.clear()
               
            except:
                  print("error")
        

if __name__=="__main__":
    t1=Thread(target=copyClip)
    t2=Thread(target=checkPress)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        time.sleep(.5)



