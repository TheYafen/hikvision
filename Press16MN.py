import pyodbc
import csv
import datetime

server = 'BUBLIK-PC\FTVIEWX64TAGDB'
server1 = '192.168.1.64\FTVIEWX64TAGDB'
server2 = '192.168.1.64'

database = 'ma'
database1 = 'ma' 
database2 = 'Protokoll'

username = 'PrClient' 
password = '741852963'

#cnxn = pyodbc.connect('DRIVER=SQL Server;SERVER='+server1+';DATABASE='+database2+';UID='+username+';PWD='+password)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server1+';DATABASE='+database2+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;")
row = cursor.fetchall()
print(row)


'''
Выдает все базы данных на сервере
SELECT name FROM sys.databases
Выдает все таблицы в Базе данных
SELECT * FROM sys.objects WHERE type in (N'U')
'''
#cursor.execute("SELECT * FROM REMOTE WHERE Zeit<?",datetime.datetime(2012, 1, 31, 7, 58, 40))
cursor.execute("SELECT * FROM REMOTE WHERE Zeit BETWEEN ? AND ?",datetime.datetime(2012, 1, 31, 7, 56, 10),datetime.datetime(2012, 1, 31, 7, 58, 40))
if 1:
    row = cursor.fetchall()
    print(row)
    with open("DATA1.csv", "w", newline="",) as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerows(row)
else:
    with open("DATA0.csv", "a", newline="") as file:
        writer = csv.writer(file)
        row = cursor.fetchone()
        while row: 
            print(row)
            writer.writerow(row)
            row = cursor.fetchone()
cursor.close()
cnxn.close()
del(cnxn)
