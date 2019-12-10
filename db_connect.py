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
row = cursor.fetchone()
print(row)

# Cursors maintaining state
print(cursor.fetchone())

# Accessing specific data
    # use the column name as an attribute of the entry
row = cursor.fetchone()
print(row)
print(row.CompanyName, row.ContactName)

print(type(cursor))
print(type(row))