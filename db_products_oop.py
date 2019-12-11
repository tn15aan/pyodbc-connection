import pyodbc
from db_connect_oop import *

class NWProducts(MSDBConnection):
    # def __sql_query(self, sql_query):
    #     return self.cursor.execute(sql_query)

    def read_all(self):
        # Build our SQL query
        query = 'SELECT * FROM Products'
        # Execute our query
        data = self._MSDBConnection__sql_query(query)
        # Return an iteratable object
        return data

    def set_id(self): #Set's ID
        id = int(input('Select an ID'))
        return id

    def read_one(self, id):
        query = f"SELECT * FROM Products WHERE ProductID = {id}"
        result = self._MSDBConnection__sql_query(query)
        return result

    def print_all(self):
        query = 'SELECT * FROM Products'
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"ID: {record.ProductID} = {record.ProductName} - £{record.UnitPrice}")

    def print_top_ten(self):
        query = 'SELECT TOP 10 * FROM Products ORDER BY UnitPrice desc'
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"Product Name: {record.ProductName} - Price {record.UnitPrice}")
        return 'Top ten products query completed'

    def print_bottom_ten(self):
        query = 'SELECT TOP 10 ProductName, UnitPrice FROM Products ORDER BY UnitPrice asc'
        data = self._MSDBConnection__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"Product Name: {record.ProductName} - Price {record.UnitPrice}")
        return 'Bottom ten products query completed'

    def set_product_name(self):
        productName = input('Enter the product name')
        return productName

    def read_product_name(self, productName):
        query = f"SELECT * FROM Products WHERE ProductName = '{productName}'"
        result = self._MSDBConnection__sql_query(query)
        return result




    # prints top 10 products by price - Formatted

    # prints bottom 10 products by price - Formatted

    # search product by name

# # Variable for NW Product table instead of products = NWProducts().read_all()
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
#
#     # Read one - using ID
#     # Prints all product using the while loop and fetchone()






    # read / list all

    # read one

    # ask for input ---> front end --> input()

    # create one --> make things persistant in DB

    # update one

    # destroy one