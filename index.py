import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="employees"
)

mycursor = mydb.cursor()

# mycursor.execute("INSERT INTO departments VALUES (10,'product')")

# mydb.commit()    

mycursor.execute("SELECT * FROM departments WHERE dept_no <= 5 ORDER BY dept_no DESC")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)