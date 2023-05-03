
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()

#insert muliple lines
mycursor.execute("""insert into fsds1.fsds values(123 , 'chandra', 'vani','2022-11-11','sql','fsds'),
(124 , 'r', 'singh','2022-11-11','sql','fsds'),
(125 , 'rohan', 'kumar','2022-11-11','sql','fsds'),
(126 , 'shreeja', 'maynale','2022-11-11','sql','fsds'),
(127 , 'shubham', 'vedi','2022-11-11','sql','fsds'),
(128 , 'abhishek', 'saini','2022-11-11','sql','fsds'),
(129 , 'manoj', 'tripathi','2022-11-11','sql','fsds'),
(130 , 'mayur ', 'gupta','2022-11-11','sql','fsds'),
(131 , 'sumay', 'cahtterjee','2022-11-11','sql','fsds'),
(132 , 'raunak', 'shgaow','2022-11-11','sql','fsds'),
(133 , 'danish', 'khan','2022-11-11','sql','fsds')""")

mydb.commit()

#select everything from table
mycursor.execute('select * from fsds1.fsds')
for i in mycursor: #using looping can execute one by one 
    print(i)


#select specific columns in table
mycursor.execute('select studentid , firstname, class from fsds1.fsds')
for i in mycursor:
    print(i)
    