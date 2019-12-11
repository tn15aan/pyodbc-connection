from db_products_oop import *
from db_employees_oop import *
products_table = NWProducts()
employees_table = NWEmployees()

while True:
    print('Options')
    print('1 - Get all products')
    print('2 - Search a single product by ID')
    print('3 - Get top 10 most expensive products')
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

    elif 'bye' in user_i or 'exit' in user_i:
        print('Goodbye! Thank you')
        break

    else:
        print("I didn't quite catch that. Please choose a valid option")
