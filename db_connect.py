import pyodbc

# These are our variables to connect
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Making the connection
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Making a cursor
cursor = docker_Northwind.cursor()

# Executing some SQL commands
cursor.execute("SELECT * FROM Customers WHERE city LIKE 'London'")

# Fetching data from the executed SQL command and printing
# row = cursor.fetchone()
# print(row)
#
# # Cursors maintaining state
# print(cursor.fetchone())
#
# # Accessing specific data
#     # use the column name as an attribute of the entry
# row = cursor.fetchone()
# print(row)
# print(row.CompanyName, row.ContactName)
#
# print(type(cursor))
# print(type(row))

# Fetchall method - bad practice
rows_all = cursor.fetchall()
print(rows_all)
print(len(rows_all))
print(type(rows_all))

for row in rows_all:
    print(row.ContactName, '-', row.CompanyName, '-', row.Fax)

# To get lots of data - use a while loop and fetchone at a time
rows = cursor.execute("SELECT * From Products")

while True:
    record = cursor.fetchone()
    if record is None:
        break
    print(record.UnitPrice)