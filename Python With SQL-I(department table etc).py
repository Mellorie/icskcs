import mysql.connector
mydb=mysql.connector.connect(host='local host',\user='root',\passwd='ICSK',\database='school')

mycur=mydb.cursor()

deptid=int(input("Enter Dept Id:"))
deptname=input("Enter Dept_Name:")
floorno=int(input("Enter Floor No:"))

q="insert into department values({},'{}',{})".format(deptid,deptname,floorno)
mycur.execute(q)
mydb.commit()
query="select*from department"
mycur.execute(query)
myrec=mycur.fetchall()
for r in myrec:
    print(r[0],r[1],r[2])
    
deptid=int(input("Enter dept_id to modify floor:"))
floor=int(input("Enter New Floor No:"))
q="IPDATE department  SER floor={} WHERE department_id=d{}".format(floor,deptid)
mycur.execute(q)
mydb.commit

mycur.execute("select*from department")
myrec=mycur.fetchall()
for r in my rec:
    print(r[0],r[1],r[2])
                             