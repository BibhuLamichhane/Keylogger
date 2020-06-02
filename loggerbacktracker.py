from pynput.keyboard import Key, Controller
import time

try:
    f = open('logs.txt', 'r')
except:
    print("Run the keylogger first")

keyboard = Controller()

data = f.readlines()

special_keys = {
    "Key.esc" : Key.esc,"Key.f1" : Key.f1,"Key.f2" : Key.f2,"Key.f3" : Key.f3,"Key.f4" : Key.f4,
    "Key.f5" : Key.f5,"Key.f6" : Key.f6,"Key.f7" : Key.f7,"Key.f8" : Key.f8,"Key.f9" : Key.f9,
    "Key.f10" : Key.f10,"Key.f11" : Key.f11,"Key.f12" : Key.f12,"Key.delete" : Key.delete,
     "Key.backspace" : Key.backspace, "Key.tab" : Key.tab, "Key.caps_lock" : Key.caps_lock,
    "Key.enter" :  Key.enter, "Key.shift_l" : Key.shift_l, "Key.shift_r" : Key.shift_r, 
    "Key.left" : Key.left, "Key.up" : Key.up, "Key.down" : Key.down, "Key.right" : Key.right, 
    "Key.space" : Key.space,  
}

keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(0.5)
keyboard.type("notepad")
time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.5)

new_data = [x.strip() for x in data]

for d in new_data:
    if d not in special_keys:
        keyboard.press(d)
    else:
        keyboard.press(special_keys[d])

