#Sigurður Ingi 30.11.2018
import pymysql

db = pymysql.connect(host = "tsuts.tskoli.is", user = "1507012360", passwd = "mypassword", db = "horde")

def printHighscore():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM HIGHSCORE")

    for row in cursor.fetchall():
        print(row[0])
    db.close()

printHighscore()

def Register():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM USERNAME")
