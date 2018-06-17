import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', db='pfa')
cursor = conn.cursor()
name=input('enter your id')
cmd = (("select * from user where id=%s")%(name))

cursor.execute(cmd)

cn=cursor.execute(cmd)
print("number of rows:",cn)
data=cursor.fetchone()
print(data)

