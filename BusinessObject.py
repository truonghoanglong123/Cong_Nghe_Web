class Customer:

    def __init__(self, customer_id=None, customer_name=None, contact_name=None, address=None, city=None, postal_code=None, country=None):

        self.customer_id = customer_id

        self.customer_name = customer_name

        self.contact_name = contact_name

        self.address = address

        self.city = city

        self.postal_code = postal_code

        self.country = country



    def fetch_data(self, row):

        self.customer_id = row[0]

        self.customer_name = row[1]

        self.contact_name = row[2]

        self.address = row[3]

        self.city = row[4]

        self.postal_code = row[5]

        self.country = row[6]



    def to_json(self):

        return {

            'customer_id': self.customer_id,

            'customer_name': self.customer_name,

            'contact_name': self.contact_name,

            'address': self.address,

            'postal_code': self.postal_code,

            'country': self.country,

            'city': self.city

        }


############################################################
#douma bua sua lai bi sot
class Categories:

    def __init__(self, CategoryID=None, CategoryName=None, Description=None):

        self.CategoryID = CategoryID

        self.CategoryName = CategoryName

        self.Description = Description


    def fetch_data(self, row):

        self.CategoryID = row[0]

        self.CategoryName = row[1]

        self.Description = row[2]


    def to_json(self):

        return {

            'CategoryID': self.CategoryID,

            'CategoryName': self.CategoryName,

            'Description': self.Description,

        }


############################################################
class Employees:

    def __init__(self, EmployeeID =None, LastName=None, FirstName=None,  BirthDate=None,  Photo=None, Notes=None):

        self.EmployeeID = EmployeeID

        self.LastName = LastName

        self.FirstName = FirstName

        self.BirthDate = BirthDate

        self.Photo = Photo

        self.Notes = Notes


    def fetch_data(self, row):

        self.EmployeeID = row[0]

        self.LastName = row[1]

        self.FirstName = row[2]

        self.BirthDate = row[3]

        self.Photo = row[4]

        self.Notes = row[5]


    def to_json(self):

        return {

            'EmployeeID': self.EmployeeID,

            'LastName': self.LastName,

            'FirstName': self.FirstName,

            'BirthDate': self.BirthDate,

            'Photo': self.Photo,

            'Notes': self.Notes

        }


############################################################
class OrderDetails:

    def __init__(self, OrderDetailID=None, OrderID=None, ProductID=None,  Quantity=None):

        self.OrderDetailID = OrderDetailID

        self.OrderID = OrderID

        self.ProductID = ProductID

        self.Quantity = Quantity


    def fetch_data(self, row):

        self.OrderDetailID = row[0]

        self.OrderID = row[1]

        self.ProductID = row[2]

        self.Quantity = row[3]



    def to_json(self):

        return {

            'OrderDetailID': self.OrderDetailID,

            'OrderID': self.OrderID,

            'ProductID': self.ProductID,

            'Quantity': self.Quantity,

        }



############################################################
class Orders:

    def __init__(self, OrderID=None, CustomerID=None, EmployeeID=None,  OrderDate=None, ShipperID=None):

        self.OrderID = OrderID

        self.CustomerID = CustomerID

        self.EmployeeID = EmployeeID

        self.OrderDate = OrderDate

        self.ShipperID = ShipperID


    def fetch_data(self, row):

        self.OrderID = row[0]

        self.CustomerID = row[1]

        self.EmployeeID = row[2]

        self.OrderDate = row[3]

        self.ShipperID = row[4]




    def to_json(self):

        return {

            'OrderID': self.OrderID,

            'CustomerID': self.CustomerID,

            'EmployeeID': self.EmployeeID,

            'OrderDate': self.OrderDate,

            'ShipperID': self.ShipperID

        }

############################################################
class Products:

    def __init__(self, ProductID=None, ProductName=None, SupplierID=None,  CategoryID=None, Unit=None, Price=None):

        self.ProductID = ProductID

        self.ProductName = ProductName

        self.SupplierID = SupplierID

        self.CategoryID = CategoryID

        self.Unit = Unit

        self.Price = Price


    def fetch_data(self, row):

        self.ProductID = row[0]

        self.ProductName = row[1]

        self.SupplierID = row[2]

        self.CategoryID = row[3]

        self.Unit = row[4]

        self.Price = row[5]



    def to_json(self):
    
        return {

            'ProductID': self.ProductID,

            'ProductName': self.ProductName,

            'SupplierID': self.SupplierID,

            'CategoryID': self.CategoryID,

            'Unit': self.Unit,

            'Price': self.Price

        }


############################################################
class Shippers:

    def __init__(self, ShipperID=None, ShipperName=None, Phone=None):

        self.ShipperID = ShipperID

        self.ShipperName = ShipperName

        self.Phone = Phone


    def fetch_data(self, row):

        self.ShipperID = row[0]

        self.ShipperName = row[1]

        self.Phone = row[2]

    def to_json(self):

        return {

            'ShipperID': self.ShipperID,

            'ShipperName': self.ShipperName,

            'Phone': self.Phone,

        }


############################################################
class Suppliers:

    def __init__(self, SupplierID=None, SupplierName=None, ContactName =None, Address= None,City=None ,PostalCode =None,Country=None,Phone=None ):

        self.SupplierID = SupplierID

        self.SupplierName = SupplierName

        self.ContactName = ContactName

        self.Address = Address

        self.City = City

        self.PostalCode = PostalCode

        self.Country = Country

        self.Phone = Phone


    def fetch_data(self, row):

        self.SupplierID = row[0]

        self.SupplierName = row[1]

        self.ContactName = row[2]

        self.Address = row[3]

        self.City = row[4]

        self.PostalCode = row[5]

        self.Country = row[6]

        self.Phone = row[7]


    def to_json(self):

        return {

            'SupplierID': self.SupplierID,

            'SupplierName': self.SupplierName,

            'ContactName': self.ContactName,

            'Address': self.Address,

            'City': self.City,

            'PostalCode': self.PostalCode,

            'Country': self.Country,

            'Phone': self.Phone

        }