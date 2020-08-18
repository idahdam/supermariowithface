import cv2
import pyautogui
import pydirectinput
import time
import pygame
import tkinter as tk

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
smile = cv2.CascadeClassifier('haarcascade_smile.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
counterSmile = 0
shit = True
clock = pygame.time.Clock()

while shit:

    
    count = 0
    #pydirectinput.keyDown('l')
    jump = False
    jumpHigh = False
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        jump = True       
        cv2.circle(frame, (int(x+w/2),int(y+h/2)), 150, (0,255, 0), 2)
        roi_color = frame[y:y + h, x:x + w]
        roi_gray = gray[y:y + h, x:x + w] 

        smiles = smile.detectMultiScale(roi_gray,1.3,5)
        for(sx,sy,sw,sh) in smiles:
            pass
            #counterSmile+=1
            #print('stop smiling for the {} time'.format(counterSmile))
            print('mario run')
            #pydirectinput.keyDown('l')
            cv2.rectangle(roi_color, (sx,sy), ((sx+sw),(sy+sh)), (0,255,255), 2)
        
    eyes = eye.detectMultiScale(gray, 1.8, 20)
    for(rx, ry, rw, rh) in eyes:
        jumpHigh = True
        #print('mario jump high')
        #pydirectinput.keyDown('a')
        cv2.circle(frame, (int(rx+rw/2), (int(ry+rh/2))), 30, (255, 0, 0), 2)
        
    if not jump and not jumpHigh:
        pass
        print('mario jump')
        ##pydirectinput.press('a')
        
    elif not jump and jumpHigh:
        pass
        print('mario jumpHigh')
        ##pydirectinput.keyDown('a')
        
    #cv2.imshow(('saycheese'), cv2.flip(frame , 1))
    cv2.imshow('say cheese',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    clock.tick(60)

cap.release()
cv2.destroyAllWindows()
