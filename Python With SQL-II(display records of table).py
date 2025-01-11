import mysql.connector as mc
mydb=mc.connect(host="localhost",\user='root',\passwd='ICSK',\database='school')
mycur=mydb.cursor()
query="Select*from department"
mycur.execute(query)
myrec=mycur.fetchall()
for in myrec:
    print(r[0],r[1],r[2])
deptid=int(input("Enter department_id for deletion"))
q="DELETE FROM department WHERE department_id={}" format(deptid)
mycur.execute(q)
mycur.commit()
mycur.execute(query)
myrec=mycur.fetchall()
for r in myrec:
    print(r[0],r[1],r[2])