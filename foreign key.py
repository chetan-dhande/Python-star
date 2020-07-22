import sqlite3
conn=sqlite3.connect('test_databasenew1.db')
print("database created successfully");
conn.execute('create table departments(department_id int primary key,department_name varchar(20));')
print('table employees1 created successfully');
conn.execute('create table employees(employee_id int primary key,last_name varchar(20),first_name varchar(20),department_id int,constraint fk_departmentsNew foreign key (department_id) references departments(department_id)) ;')
conn.execute("insert into departments values (30,'hr');")
conn.execute("insert into departments values (99,'sales');")
conn.execute("insert into employees values (1000,'john','smith',30);")
conn.execute("insert into employees values (1001,'ram','rahul',999);")

cursor=conn.execute(" select * from departments join employees on departments.department_id=employees.department_id")
for row in cursor:
    print("department_id=",row[0])
    print("department_name=",row[1])
    print("employee_id=",row[2])
    print("last name=",row[3])
    print("first name=",row[4])
print("*******************************")

print('operation done  successfully');