import cv2
import pymysql

cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('Classifiers/face.xml')

def insertOrUpdate(Id,Name):
    conn = pymysql.connect(host='localhost',user='root',password='',db='pfa')
    cursor=conn.cursor()
    cmd=(("SELECT * FROM user Where id=%s")%(Id))
    cursor.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        #cmd="UPDATE user SET name="+str(Name)+"WHERE id="+str(Id)
        cmd =  (("UPDATE user SET nom = '%s' WHERE id = %s")%(Name,Id))
        #data_user = (Id, Name)
    else:
        #cmd="INSERT INTO user(id,name) Values("+str(Id)+","+str(Name)+")"
        cmd = (("INSERT INTO user (id, nom) VALUES (%s, '%s')")%(Id,Name))
        #data_user = (Id,Name)
    cursor.execute(cmd)
    conn.commit()
    conn.close()

i=0
offset=50
name=input('enter your id')
nom=input('enter your name')
insertOrUpdate(name,nom)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("dataSet/face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.waitKey(100)
    if i>20:
        cam.release()
        cv2.destroyAllWindows()
        break

