import sqlite3
conn=sqlite3.connect("studentdatabase.db")
print("studentdatabase database created")

result=conn.execute("select * from student")
r=result.fetchall()
print(r)

result1=conn.execute("select * from student")
r1=result1.fetchone()
print(r1)

result2=conn.execute("select * from student")
r2=result2.fetchmany(2)
print(r2)

result3=conn.execute("select * from student where fname='rahul'")
r3=result3.fetchall()
print(r3)


