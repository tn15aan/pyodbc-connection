from db_products_oop import *
from db_employees_oop import *
products_table = NWProducts()
employees_table = NWEmployees()

while True:
    print('Options')
    print('1 - Get all products')
    print('2 - Search a single product by ID')
    print('3 - Get top 10 most expensive products')
    print('4 - Get all employees data')
    print('5 - Search a single employee by ID')
    print('6 - Search for employee using their last name')
    user_i = input('Choose 1, 2 or 3').strip()

    if user_i == '1':
        products_table.print_all()

    elif user_i == '2':
        print('Getting a single product')
        id = products_table.set_id()
        product = products_table.read_one(id)
        print(product.fetchone()) # Fetchone to get the row

    elif user_i == '3':
        print('Printing top 10 products by price')
        topTenProducts = products_table.print_top_ten()
        print(topTenProducts)

    elif user_i == '4':
        print(employees_table.print_all_emp())

    elif user_i == '5':
        emp_id = employees_table.set_id_emp()
        employee = employees_table.read_one_emp(emp_id)
        print(employee.fetchone())

    elif user_i == '6':
        employeeName = employees_table.set_employee_name()
        employeeSearch = employees_table.read_employee_name(employeeName)
        print(employeeSearch.fetchone())

    elif 'bye' in user_i or 'exit' in user_i:
        print('Goodbye! Thank you')
        break

    else:
        print("I didn't quite catch that. Please choose a valid option")

# topTenProducts = products_table.print_top_ten()
# print(topTenProducts)
#
# bottomTenProducts = products_table.print_bottom_ten()
# print(bottomTenProducts)
#
# #get product name
# print('Getting a single product')
# productName = products_table.set_product_name()
# productSearch = products_table.read_product_name(productName)
# print(productSearch.fetchone())

# EMPLOYEES STUFF
# # Print all employees
# print('//')
# print(employees_table.print_all_emp())
#
# # Get one employee by ID
# emp_id = employees_table.set_id_emp()
# employee = employees_table.read_one_emp(emp_id)
# print(employee.fetchone()) # Fetchone to get the row
#
# # Get employees using their last name
# print('Getting a single product')
# employeeName = employees_table.set_employee_name()
# employeeSearch = employees_table.read_employee_name(employeeName)
# print(employeeSearch.fetchone())

addEmployee = employees_table.create_employee()
print("Added employee!")

# Variable for NW Product table instead of products = NWProducts().read_all()
# tables_products = NWProducts()
#
# products = tables_products.read_all() # Method read all returns sometimes, but did not alter original variable
# print(products.fetchone())
#
# # Read one using ID
# product = tables_products.read_one()
# print(product.fetchone())
#
# # Read all and print
# all_product = tables_products.read_all()
# while True:
#     record = all_product.fetchone()
#     if record is None:
#         break
#     print(record)

    # Read one - using ID
    # Prints all product using the while loop and fetchone()