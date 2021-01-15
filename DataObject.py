import psycopg2

from BusinessObject import Customer as CustomerEntity
from BusinessObject import Categories as CategoriesEntity
from BusinessObject import Employees as EmployeesEntity
from BusinessObject import OrderDetails as OrderDetailsEntity
from BusinessObject import Orders as OrdersEntity
from BusinessObject import Products as ProductsEntity
from BusinessObject import Shippers as ShippersEntity
from BusinessObject import Suppliers as SuppliersEntity


class Customer:

    def __init__(self, connection_data):

        self.connection_data = connection_data



    def insert_Customer(self, customer: CustomerEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """INSERT INTO Customers(customername, contactname, address, city, postalcode, country)

                VALUES(%s, %s, %s, %s, %s, %s)"""

        cursor.execute(sql, (customer.customer_name, customer.contact_name, customer.address, customer.city, customer.postal_code, customer.country))

        conn.commit()

        return 'Insert successfully'

    

    def get_all_Customer(self):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "SELECT * FROM customers"

        cursor.execute(sql)

        conn.commit()

        rows = cursor.fetchall()

        result = []

        for row in rows:

            customer = CustomerEntity()

            customer.fetch_data(row)

            result.append(customer.to_json())

        return result



    def delete_Customer(self, customer: CustomerEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "DELETE FROM customers WHERE customerid = %s"

        cursor.execute(sql, (customer.customer_id, ))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Deleted successfully', 200

        return 'Id not found', 404



    def update_Customer(self, customer: CustomerEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """UPDATE customers SET

                    customername=%s, contactname=%s, address=%s,

                    city=%s, postalcode=%s, country=%s WHERE customerid=%s"""

        cursor.execute(sql, (customer.customer_name, customer.contact_name, customer.address, customer.city, customer.postal_code, customer.country, customer.customer_id))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Updated successfully', 200

        return 'Id not found', 404

#################################################################
class Categories:

    def __init__(self, connection_data):

        self.connection_data = connection_data



    def insert_Categories(self, Categories: CategoriesEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """INSERT INTO Categories( CategoryName , Description)

                VALUES(%s, %s)"""

        cursor.execute(sql, (Categories.CategoryName, Categories.Description))

        conn.commit()

        return 'Insert successfully'

    

    def get_all_Categories(self):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "SELECT * FROM Categories"

        cursor.execute(sql)

        conn.commit()

        rows = cursor.fetchall()

        result = []

        for row in rows:

            Categories = CategoriesEntity()

            Categories.fetch_data(row)

            result.append(Categories.to_json())

        return result



    def delete_Categories(self, Categories: CategoriesEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "DELETE FROM Categories WHERE categoryid = %s"

        cursor.execute(sql, (Categories.CategoryID,))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Deleted successfully', 200

        return 'Id not found', 404



    def update_Categories(self, Categories: CategoriesEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """UPDATE Categories SET categoryname =%s, description =%s where categoryid =%s """ 

        cursor.execute(sql, (Categories.CategoryName, Categories.Description,Categories.CategoryID))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Updated successfully', 200

        return 'Id not found', 404

###########################################################################
class Employees:

    def __init__(self, connection_data):

        self.connection_data = connection_data



    def insert_Employees(self, Employees: EmployeesEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """INSERT INTO Employees(LastName , FirstName , BirthDate , Photo , Notes )

                VALUES(%s, %s,%s, %s, %s)"""

        cursor.execute(sql, (Employees.LastName, Employees.FirstName, Employees.BirthDate, Employees.Photo, Employees.Notes))

        conn.commit()

        return 'Insert successfully'

    

    def get_all_Employees(self):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "SELECT * FROM Employees"

        cursor.execute(sql)

        conn.commit()

        rows = cursor.fetchall()

        result = []

        for row in rows:

            Employees = EmployeesEntity()

            Employees.fetch_data(row)

            result.append(Employees.to_json())

        return result



    def delete_Employees(self, Employees: EmployeesEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "DELETE FROM Employees WHERE employeeid  = %s"

        cursor.execute(sql, (Employees.EmployeeID, ))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Deleted successfully', 200

        return 'Id not found', 404



    def update_Employees(self, Employees: EmployeesEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """UPDATE Employees SET lastname=%s, firstname=%s, birthdate=%s, photo=%s, notes =%s where employeeid=%s"""

        cursor.execute(sql, (Employees.LastName, Employees.FirstName, Employees.BirthDate, Employees.Photo, Employees.Notes, Employees.EmployeeID))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Updated successfully', 200

        return 'Id not found', 404


##################################################################
class OrderDetails:

    def __init__(self, connection_data):

        self.connection_data = connection_data



    def insert_OrderDetails(self, OrderDetails: OrderDetailsEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """INSERT INTO OrderDetails(OrderID  , ProductID  , Quantity ) VALUES (%s, %s, %s)"""

        cursor.execute(sql, (OrderDetails.OrderID, OrderDetails.ProductID, OrderDetails.Quantity))

        conn.commit()

        return 'Insert successfully'

    

    def get_all_OrderDetails(self):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "SELECT * FROM OrderDetails"

        cursor.execute(sql)

        conn.commit()

        rows = cursor.fetchall()

        result = []

        for row in rows:

            OrderDetails = OrderDetailsEntity()

            OrderDetails.fetch_data(row)

            result.append(OrderDetails.to_json())

        return result



    def delete_OrderDetails(self, OrderDetails: OrderDetailsEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "DELETE FROM OrderDetails WHERE orderdetailid= %s"

        cursor.execute(sql, (OrderDetails.OrderDetailID, ))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Deleted successfully', 200

        return 'Id not found', 404



    def update_OrderDetails(self, OrderDetails: OrderDetailsEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """UPDATE OrderDetails SET

                    orderid=%s, productid=%s, quantity=%s where orderdetailid=%s"""

        cursor.execute(sql, (OrderDetails.OrderID, OrderDetails.ProductID, OrderDetails.Quantity, OrderDetails.OrderDetailID))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Updated successfully', 200

        return 'Id not found', 404


##################################################################
class Orders:

    def __init__(self, connection_data):

        self.connection_data = connection_data



    def insert_Orders(self, Orders: OrdersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """INSERT INTO Orders (CustomerID, EmployeeID , OrderDate , ShipperID )

                VALUES(%s, %s, %s, %s)"""

        cursor.execute(sql, (Orders.CustomerID, Orders.EmployeeID, Orders.OrderDate, Orders.ShipperID))

        conn.commit()

        return 'Insert successfully'

    

    def get_all_Orders(self):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "SELECT * FROM Orders"

        cursor.execute(sql)

        conn.commit()

        rows = cursor.fetchall()

        result = []

        for row in rows:

            Orders = OrdersEntity()

            Orders.fetch_data(row)

            result.append(Orders.to_json())

        return result



    def delete_Orders(self, Orders: OrdersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "DELETE FROM Orders WHERE orderid = %s"

        cursor.execute(sql, (Orders.OrderID  , ))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Deleted successfully', 200

        return 'Id not found', 404



    def update_Orders(self, Orders: OrdersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """UPDATE Orders SET

                    customerid=%s, employeeid =%s, orderdate =%s, shipperid = %s where orderid=%s"""

        cursor.execute(sql, (Orders.CustomerID, Orders.EmployeeID, Orders.OrderDate, Orders.ShipperID, Orders.OrderID))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Updated successfully', 200

        return 'Id not found', 404


##################################################################
class Products:

    def __init__(self, connection_data):

        self.connection_data = connection_data



    def insert_Products(self, Products: ProductsEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """INSERT INTO Products (ProductName, SupplierID , CategoryID , Unit, Price )

                VALUES(%s, %s, %s, %s, %s)"""

        cursor.execute(sql, (Products.ProductName, Products.SupplierID, Products.CategoryID, Products.Unit, Products.Price))

        conn.commit()

        return 'Insert successfully'

    

    def get_all_Products(self):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "SELECT * FROM Products"

        cursor.execute(sql)

        conn.commit()

        rows = cursor.fetchall()

        result = []

        for row in rows:

            Products = ProductsEntity()

            Products.fetch_data(row)

            result.append(Products.to_json())

        return result

    def delete_Products(self, Products: ProductsEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "DELETE FROM Products WHERE productid = %s"

        cursor.execute(sql, (Products.ProductID , ))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Deleted successfully', 200

        return 'Id not found', 404



    def update_Products(self, Products: ProductsEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """UPDATE Products SET

                    productname=%s, supplierid=%s, categoryid=%s, unit= %s, price=%s where productid=%s"""

        cursor.execute(sql, (Products.ProductName, Products.SupplierID, Products.CategoryID, Products.Unit, Products.Price, Products.ProductID))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Updated successfully', 200

        return 'Id not found', 404



##################################################################
class Shippers:

    def __init__(self, connection_data):

        self.connection_data = connection_data



    def insert_Shippers(self, Shippers: ShippersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """INSERT INTO Shippers (ShipperName , Phone )

                VALUES(%s, %s)"""

        cursor.execute(sql, (Shippers.ShipperName, Shippers.Phone))

        conn.commit()

        return 'Insert successfully'

    

    def get_all_Shippers(self):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "SELECT * FROM Shippers"

        cursor.execute(sql)

        conn.commit()

        rows = cursor.fetchall()

        result = []

        for row in rows:

            Shippers = ShippersEntity()

            Shippers.fetch_data(row)

            result.append(Shippers.to_json())

        return result



    def delete_Shippers(self, Shippers: ShippersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "DELETE FROM Shippers WHERE shipperid = %s"

        cursor.execute(sql, (Shippers.ShipperID , ))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Deleted successfully', 200

        return 'Id not found', 404



    def update_Shippers(self, Shippers: ShippersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """UPDATE Shippers SET

                    shippername=%s, phone=%s where shipperid=%s"""

        cursor.execute(sql, (Shippers.ShipperName, Shippers.Phone, Shippers.ShipperID))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Updated successfully', 200

        return 'Id not found', 404


##################################################################
class Suppliers:

    def __init__(self, connection_data):

        self.connection_data = connection_data



    def insert_Suppliers(self, Suppliers: SuppliersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """INSERT INTO Suppliers(SupplierName, ContactName ,Address ,City ,PostalCode ,Country ,Phone  )

                VALUES(%s, %s, %s,%s, %s, %s,%s)"""

        cursor.execute(sql, (Suppliers.SupplierName, Suppliers.ContactName, Suppliers.Address, Suppliers.City, Suppliers.PostalCode, Suppliers.Country, Suppliers.Phone))

        conn.commit()

        return 'Insert successfully'

    

    def get_all_Suppliers(self):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "SELECT * FROM Suppliers"

        cursor.execute(sql)

        conn.commit()

        rows = cursor.fetchall()

        result = []

        for row in rows:

            Suppliers = SuppliersEntity()

            Suppliers.fetch_data(row)

            result.append(Suppliers.to_json())

        return result



    def delete_Suppliers(self, Suppliers: SuppliersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = "DELETE FROM Suppliers WHERE supplierid  = %s"

        cursor.execute(sql, (Suppliers.SupplierID , ))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Deleted successfully', 200

        return 'Id not found', 404



    def update_Suppliers(self, Suppliers: SuppliersEntity):

        conn = psycopg2.connect(host=self.connection_data['host'],

                                port=self.connection_data['port'],

                                user=self.connection_data['user'],

                                password=self.connection_data['password'],

                                database=self.connection_data['database'])

        cursor = conn.cursor()

        sql = """UPDATE Suppliers SET

                   suppliername=%s, contactname=%s,address=%s ,city =%s,postalcode=%s ,country=%s ,phone=%s where supplierid=%s"""

        cursor.execute(sql, (Suppliers.SupplierName, Suppliers.ContactName, Suppliers.Address, Suppliers.City, Suppliers.PostalCode, Suppliers.Country, Suppliers.Phone , Suppliers.SupplierID))

        conn.commit()

        n = cursor.rowcount

        if n > 0:

            return 'Updated successfully', 200

        return 'Id not found', 404
