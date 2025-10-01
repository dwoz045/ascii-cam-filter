import cv2
import os
import math
from time import sleep

capture = cv2.VideoCapture(0)

def pixelToASCII(pixel_intensity):  
    ASCII_CHARS = "€&@%#*+=-'."
    return ASCII_CHARS[math.floor((pixel_intensity/256)*len(ASCII_CHARS))]

while True:
    success, frame = capture.read()
    if success:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fps = capture.get(cv2.CAP_PROP_FPS)
        delta = 1/fps
        resized_image = cv2.resize(gray_frame, (os.get_terminal_size().columns, os.get_terminal_size().lines))
        ascii_image = ''
        for i in range(os.get_terminal_size().lines):
            for j in range(os.get_terminal_size().columns):
                ascii_image += pixelToASCII(resized_image[i][j])
            ascii_image += '\n'
        print(ascii_image)
        sleep(delta)
        os.system('clear')
    else:
        os.system('clear')
        capture.release()
        break

