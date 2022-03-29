import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="guru",
  passwd="Dominus@5",
  database="network_manager"
)
def getuser(email):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT password FROM  users where email = %s ",(email,))
    result = mycursor.fetchall()
    print(result)
    return result