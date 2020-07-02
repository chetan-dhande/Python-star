import sqlite3
conn=sqlite3.connect("studentdatabase.db")
print("studentdatabase database created")


conn.execute("delete from student where id=4")
conn.commit()
conn.close()