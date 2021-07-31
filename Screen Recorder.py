import cv2 # pip install opencv-python
import numpy as np # pip install numpy
import pyautogui as gui # pip install pyautogui
from win32api import GetSystemMetrics # pip install pywin32
import datetime

# Setting timestamp for dynamic video name
timestamp = datetime.datetime.now().strftime('%d-%m-%yqq')
filename = f'{timestamp}.mp4'
# Getting width and height of system for full screen recording
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
cc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # Encoding video file
out = cv2.VideoWriter(filename, cc, 24.0, (width, height))

while True:
    img = gui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('Sceen Recorder', frame)
    cv2.waitKey(10)

    if cv2.waitKey(1) == ord('q'):
        break