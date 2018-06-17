import cv2,os
import numpy as np
from PIL import Image 
import pickle
import pymysql
import io

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

def getProfile(id):
    conn = pymysql.connect(host='localhost',user='root',password='',db='pfa')
    cursor=conn.cursor()
    cmd=(("SELECT * FROM user Where id=%s")%(id))
    cursor.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font
fontScale = 1
fontColor = (255, 255, 255)
profiles={}
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        #if(nbr_predicted==7):
         #    nbr_predicted='Obama'
        #elif(nbr_predicted==11):
         #    nbr_predicted='Mehdi'
        profile=getProfile(nbr_predicted)
        if(profile!=None):
            cv2.putText(im,str(profile[1]), (x,y+h+30),font, fontScale,fontColor) #Draw the text
            cv2.putText(im,str(profile[2]), (x,y+h+60),font, fontScale,fontColor) #Draw the text
            #cv2.putText(im,str(profile[3]), (x,y+h+90),font, fontScale,fontColor) #Draw the text
            #cv2.putText(im,str(profile[4]), (x,y+h+120),font, fontScale,fontColor) #Draw the text
            #cv2.putText(im,str(profile[5]), (x,y+h+150),font, fontScale,fontColor) #Draw the text
        cv2.imshow('im',im)
        cv2.waitKey(10)









