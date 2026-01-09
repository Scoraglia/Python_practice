import sqlite3 

#The code to create a database file and a table named Track with two columns in the database


#The connect operation makes a “connection” to the database stored in the file music.sqlite in the current directory. 
# If the file does not exist, it will be created.
  
conn = sqlite3.connect('music.sqlite') 

# A cursor is like a file handle that we can use to perform operations on the data stored in the database. 
# Calling cursor() is very similar conceptually to calling open() when dealing with text files.
cur = conn.cursor() 

# Once we have the cursor, we can begin to execute commands on the contents of the database using the execute() method.
cur.execute('DROP TABLE IF EXISTS Track') 
cur.execute('CREATE TABLE Track (title TEXT, plays INTEGER)') 

conn.close()