import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
#select everything database
mycursor.execute("select * from fsds1.fsds")

for i in mycursor:
    print(i)

#Showing specific column in table
mycursor.execute('select studentid , firstname, class from fsds1.fsds')
for i in mycursor:
    print(i)


#select everything in database studentid is equal 130 )
mycursor.execute('select * from fsds1.fsds where studentid = 130 ')
for i in mycursor:#using looping execute data one by one 
    print(i)

#studentid is greater than 130 row will be executed 
mycursor.execute('select * from fsds1.fsds where studentid > 130 ')
for i in mycursor:
    print(i)

#select everything from database and table (only firstname and class)
mycursor.execute("select * from fsds1.fsds where firstname = 'shubham' and class = 'sql'")
for i in mycursor:
    print(i)


#updating data  
mycursor.execute("update fsds1.fsds set firstname = 'roshan' where studentid = 125 ")
mydb.commit()


mycursor.execute("update fsds1.fsds set class = 'mysql'")
mydb.commit()

#using delete can drop the  specific row 
mycursor.execute("delete from fsds1.fsds where lastname = 'gupta'")
mydb.commit()

#using min can show min value in table
mycursor.execute("select min(studentid) from fsds1.fsds")
for i in mycursor:
    print(i)


#using max can show min value in studentid
mycursor.execute("select max(studentid) from fsds1.fsds")
for i in mycursor:
    print(i)

mycursor.execute("select count(*) from fsds1.fsds")
for i in mycursor:
    print(i)


#updating data between studentid is 125 and 128 as sql
mycursor.execute("update fsds1.fsds set class = 'sql' where studentid between 125 and 128 ")
mydb.commit()

#updating data between studentid is 125 and 128 as mongobd
mycursor.execute("update fsds1.fsds set class = 'mongodb' where studentid between 129 and 133 ")
mydb.commit()

#count how many of class 
mycursor.execute("select count(*) ,class from fsds1.fsds group by class")
for i in mycursor:
    print(i)

#drop entire folder using drop
#mycursor.execute("drop table fsds1.fsds")
#mydb.commit()