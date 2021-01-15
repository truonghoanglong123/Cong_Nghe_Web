from flask import Flask

from flask import request

from flask import jsonify

from flask_cors import CORS

import os

from BusinessObject import Customer as CustomerEntity
from BusinessObject import Categories as CategoriesEntity
from BusinessObject import Employees as EmployeesEntity
from BusinessObject import OrderDetails as OrderDetailsEntity
from BusinessObject import Orders as OrdersEntity
from BusinessObject import Products as ProductsEntity
from BusinessObject import Shippers as ShippersEntity
from BusinessObject import Suppliers as SuppliersEntity
from DataObject import Customer
from DataObject import Categories
from DataObject import Employees
from DataObject import OrderDetails
from DataObject import Orders
from DataObject import Products
from DataObject import Shippers
from DataObject import Suppliers


app = Flask(__name__)

CORS(app)


connection_data = dict()

connection_data['host'] = os.getenv('host')

connection_data['user'] = os.getenv('user')

connection_data['password'] = os.getenv('password')

connection_data['port'] = os.getenv('port')

connection_data['database'] = os.getenv('database')



@app.route('/')
def home():

    return 'This is backend'



@app.route('/index', methods=['GET'])
def index():

    return 'This is index page'



# CRUD(Create, Read, Update, Delete)

# POST, GET, PUT, DELETE



@app.route('/customer', methods=['POST'])

def add_customer():

    data = request.json

    customer = CustomerEntity(customer_name=data['customer_name'],

                                contact_name=data['contact_name'],

                                address=data['address'],

                                city=data['city'],

                                postal_code=data['postal_code'],

                                country=data['country'])

    c = Customer(connection_data)

    message = c.insert_Customer(customer)

    if message is None:

        return jsonify({

            'message': 'Cannot insert data'

        }), 500

    return jsonify({

        'message': message

    })



@app.route('/customer/all')

def get_all_customer():

    c = Customer(connection_data)

    result = c.get_all_Customer()

    return jsonify({
        'data': result
    })



@app.route('/customer/<int:id>', methods=['DELETE', 'PUT'])

def delete_customer_by_id(id):

    if request.method == 'DELETE':

        # Delete user by id

        customer = CustomerEntity(customer_id=id)

        c = Customer(connection_data)

        result = c.delete_Customer(customer)

        return jsonify({

            'message': result[0]

        }), result[1]

    else:
        # Update user by id

        data = request.json

        customer = CustomerEntity(customer_id=id,

                                    customer_name=data['customer_name'],

                                    contact_name=data['contact_name'],

                                    address=data['address'],

                                    city=data['city'],

                                    postal_code=data['postal_code'],

                                    country=data['country'])

        c = Customer(connection_data)

        result = c.update_Customer(customer)

        return jsonify({

            'message': result[0]

        }), result[1]

#################################################################
@app.route('/Categories', methods=['POST'])
def add_Categories():

    data = request.json

    cate = CategoriesEntity(CategoryName=data['CategoryName'],

                                Description=data['Description'])

    c = Categories(connection_data)

    message = c.insert_Categories(cate)

    if message is None:

        return jsonify({

            'message': 'Cannot insert data'

        }), 500

    return jsonify({

        'message': message

    })

@app.route('/Categories/all')

def get_all_Categories():

    c = Categories(connection_data)

    result = c.get_all_Categories()

    return jsonify({
        'data': result
    })


@app.route('/Categories/<int:id>', methods=['DELETE', 'PUT'])

def delete_category_by_id(id):

    if request.method == 'DELETE':

        # Delete user by id

        cate = CategoriesEntity(CategoryID=id)

        c = Categories(connection_data)

        result = c.delete_Categories(cate)

        return jsonify({

            'message': result[0]

        }), result[1]

    else:
        # Update user by id

        data = request.json

        cate = CategoriesEntity(CategoryID=id,
                                CategoryName=data['CategoryName'],
                                Description=data['Description'])

        c = Categories(connection_data)

        result = c.update_Categories(cate)

        return jsonify({

            'message': result[0]

        }), result[1]




#################################################################
@app.route('/Employees', methods=['POST'])
def add_Employees():

    data = request.json

    emp = EmployeesEntity(LastName=data['LastName'],
                        FirstName=data['FirstName'],
                        BirthDate=data['BirthDate'],
                        Photo=data['Photo'],
                        Notes=data['Notes'])

    c = Employees(connection_data)

    message = c.insert_Employees(emp)

    if message is None:

        return jsonify({

            'message': 'Cannot insert data'

        }), 500

    return jsonify({

        'message': message

    })

@app.route('/Employees/all')

def get_all_Employees():

    c = Employees(connection_data)

    result = c.get_all_Employees()

    return jsonify({
        'data': result
    })


@app.route('/Employees/<int:id>', methods=['DELETE', 'PUT'])

def delete_employee_by_id(id):

    if request.method == 'DELETE':

        # Delete user by id

        emp = EmployeesEntity(EmployeeID=id)

        c = Employees(connection_data)

        result = c.delete_Employees(emp)

        return jsonify({

            'message': result[0]

        }), result[1]

    else:
        # Update user by id

        data = request.json

        emp = EmployeesEntity(EmployeeID=id,
                                LastName=data['LastName'],
                                FirstName=data['FirstName'],
                                BirthDate=data['BirthDate'],
                                Photo=data['Photo'],
                                Notes=data['Notes'])

        c = Employees(connection_data)

        result = c.update_Employees(emp)

        return jsonify({

            'message': result[0]

        }), result[1]


#################################################################
@app.route('/OrderDetails', methods=['POST'])
def add_OrderDetails():

    data = request.json

    ord = OrderDetailsEntity(OrderID=data['OrderID'], ProductID=data['ProductID'], Quantity=data['Quantity'])

    c = OrderDetails(connection_data)

    message = c.insert_OrderDetails(ord)

    if message is None:

        return jsonify({

            'message': 'Cannot insert data'

        }), 500

    return jsonify({

        'message': message

    })

@app.route('/OrderDetails/all')

def get_all_OrderDetails():

    c = OrderDetails(connection_data)

    result = c.get_all_OrderDetails()

    return jsonify({
        'data': result
    })


@app.route('/OrderDetails/<int:id>', methods=['DELETE', 'PUT'])

def delete_orderDetail_by_id(id):

    if request.method == 'DELETE':

        # Delete user by id

        ord = OrderDetailsEntity(OrderDetailID=id)

        c = OrderDetails(connection_data)

        result = c.delete_OrderDetails(ord)

        return jsonify({

            'message': result[0]

        }), result[1]

    else:
        # Update user by id

        data = request.json

        ord = OrderDetailsEntity(OrderDetailID=id,
                                OrderID=data['OrderID'],
                                ProductID=data['ProductID'],
                                Quantity=data['Quantity'])

        c = OrderDetails(connection_data)

        result = c.update_OrderDetails(ord)

        return jsonify({

            'message': result[0]

        }), result[1]


################################################################# 
@app.route('/Orders', methods=['POST'])
def add_Orders():

    data = request.json

    order = OrdersEntity(CustomerID =data['CustomerID'], EmployeeID =data['EmployeeID'], OrderDate =data['OrderDate'], ShipperID=data['ShipperID'])

    c = Orders(connection_data)

    message = c.insert_Orders(order)

    if message is None:

        return jsonify({

            'message': 'Cannot insert data'

        }), 500

    return jsonify({

        'message': message

    })

@app.route('/Orders/all')

def get_all_Orders():

    c = Orders(connection_data)

    result = c.get_all_Orders()

    return jsonify({
        'data': result
    })


@app.route('/Orders/<int:id>', methods=['DELETE', 'PUT'])

def delete_Orders_by_id(id):

    if request.method == 'DELETE':

        # Delete user by id

        order = OrdersEntity(OrderID=id)

        c = Orders(connection_data)

        result = c.delete_Orders(order)

        return jsonify({

            'message': result[0]

        }), result[1]

    else:
        # Update user by id

        data = request.json

        order = OrdersEntity(OrderID =id,
                                CustomerID =data['CustomerID'],
                                EmployeeID =data['EmployeeID'],
                                OrderDate =data['OrderDate'],
                                ShipperID=data['ShipperID'])

        c = Orders(connection_data)

        result = c.update_Orders(order)

        return jsonify({

            'message': result[0]

        }), result[1]


################################################################# 
@app.route('/Products', methods=['POST'])
def add_Products():

    data = request.json

    pro = ProductsEntity(ProductName=data['ProductName'], SupplierID=data['SupplierID'], 
                         CategoryID=data['CategoryID'], Unit=data['Unit'], Price=data['Price'])

    c = Products(connection_data)

    message = c.insert_Products(pro)

    if message is None:

        return jsonify({

            'message': 'Cannot insert data'

        }), 500

    return jsonify({

        'message': message

    })

@app.route('/Products/all')

def get_all_Products():

    c = Products(connection_data)

    result = c.get_all_Products()

    return jsonify({
        'data': result
    })


@app.route('/Products/<int:id>', methods=['DELETE', 'PUT'])

def delete_Products_by_id(id):

    if request.method == 'DELETE':

        # Delete user by id

        product = ProductsEntity(ProductID=id)

        c = Products(connection_data)

        result = c.delete_Products(product)

        return jsonify({

            'message': result[0]

        }), result[1]

    else:
        # Update user by id

        data = request.json

        product = ProductsEntity(ProductID=id,
                                ProductName=data['ProductName'],
                                SupplierID=data['SupplierID'],
                                CategoryID=data['CategoryID'],
                                Unit=data['Unit'],
                                Price=data['Price'])

        c = Products(connection_data)

        result = c.update_Products(product)

        return jsonify({

            'message': result[0]

        }), result[1]


################################################################# 
@app.route('/Shippers', methods=['POST'])
def add_Shippers():

    data = request.json

    ship = ShippersEntity(ShipperName=data['ShipperName'], Phone=data['Phone'])

    c = Shippers(connection_data)

    message = c.insert_Shippers(ship)

    if message is None:

        return jsonify({

            'message': 'Cannot insert data'

        }), 500

    return jsonify({

        'message': message

    })

@app.route('/Shippers/all')

def get_all_Shippers():

    c = Shippers(connection_data)

    result = c.get_all_Shippers()

    return jsonify({
        'data': result
    })


@app.route('/Shippers/<int:id>', methods=['DELETE', 'PUT'])

def delete_Shippers_by_id(id):

    if request.method == 'DELETE':

        # Delete user by id

        shipp = ShippersEntity(ShipperID=id)

        c = Shippers(connection_data)

        result = c.delete_Shippers(shipp)

        return jsonify({

            'message': result[0]

        }), result[1]

    else:
        # Update user by id

        data = request.json

        shipp = ShippersEntity(ShipperID =id,
                                ShipperName =data['ShipperName'],
                                Phone=data['Phone'])

        c = Shippers(connection_data)

        result = c.update_Shippers(shipp)

        return jsonify({

            'message': result[0]

        }), result[1]


################################################################# 
@app.route('/Suppliers', methods=['POST'])
def add_Suppliers():

    data = request.json

    supp = SuppliersEntity(SupplierName=data['SupplierName'], ContactName=data['ContactName'], Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'], Phone=data['Phone'])

    c = Suppliers(connection_data)

    message = c.insert_Suppliers(supp)

    if message is None:

        return jsonify({

            'message': 'Cannot insert data'

        }), 500

    return jsonify({

        'message': message

    })

@app.route('/Suppliers/all')

def get_all_Suppliers():

    c = Suppliers(connection_data)

    result = c.get_all_Suppliers()

    return jsonify({
        'data': result
    })


@app.route('/Suppliers/<int:id>', methods=['DELETE', 'PUT'])

def delete_Suppliers_by_id(id):

    if request.method == 'DELETE':

        # Delete user by id

        suppli = SuppliersEntity(SupplierID=id)

        c = Suppliers(connection_data)

        result = c.delete_Suppliers(suppli)

        return jsonify({

            'message': result[0]

        }), result[1]

    else:
        # Update user by id

        data = request.json

        suppli = SuppliersEntity(SupplierID=id,
                                SupplierName=data['SupplierName'],
                                ContactName=data['ContactName'],
                                Address=data['Address'],
                                City=data['City'],
                                PostalCode=data['PostalCode'],
                                Country=data['Country'],
                                Phone=data['Phone'])

        c = Suppliers(connection_data)

        result = c.update_Suppliers(suppli)

        return jsonify({

            'message': result[0]

        }), result[1]



