import pyodbc
from db_connect_oop import *

class NWEmployees(MSDBConnection):

    def print_all_emp(self):
        query = 'SELECT * FROM Employees'
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)

    def set_id_emp(self): #Set's ID
        id = int(input('Select an ID'))
        return id

    def read_one_emp(self, id):
        query = f"SELECT * FROM Employees WHERE EmployeeID = {id}"
        result = self._MSDBConnection__sql_query(query)
        return result

    def set_employee_name(self):
        employeeName = input('Enter the Employees last name')
        return employeeName

    def read_employee_name(self, employeeName):
        query = f"SELECT * FROM Employees WHERE LastName = '{employeeName}'"
        result = self._MSDBConnection__sql_query(query)
        return result

    def create_employee(self):
        employeeID = input('Employee ID: ')
        lastName = input('Last name: ')
        firstName = input('First name: ')
        # title = input('Employee title: ')
        # titleOfCourtesy = input('Title of Courtesy e.g. Ms. Mr. Dr.: ')
        # birthDate = input('Birth date (YYYY-MM--DD): ')
        # hireDate = input('Start of employment (YYYY-MM--DD): ')
        query = f"INSERT INTO Employees VALUES ({employeeID}, '{lastName}', '{firstName}'"
        result = self._MSDBConnection__sql_query(query)
        self.cursor.commit()
        return 'Employee added'



# Create one employee
    # sudo code
    # What data do you need to create an employee?
# update/change one employee data
    # sudo code



# Get all employees data

# Get one employee by id

# Search for one employee by name or last_name

## Add all this to our run_products while loop