
import requests

# data = {}

# data['customer_name'] = 'thang'
# data['contact_name'] = '123123123'
# data['address'] = '12 afdedef'
# data['postal_code'] = '55555'
# data['country'] = 'dn'
# data['city'] = 'dn'

# insert = requests.post('http://192.168.1.4:5000/customer' ,json=data)
# print(insert.text)

# update
#data = {}
# data['customer_name'] = 'minh'
# data['contact_name'] = 'resrer'
# data['address'] = '12 rserse'
# data['postal_code'] = 'rser'
# data['country'] = 'dn'
# data['city'] = 'dn'
# insert = requests.put('http://192.168.1.4:5000/customer/3' ,json=data)
# print(insert.text)

#delete
#insert = requests.delete('http://192.168.1.2:5000/customer/2' ,json=data)
#print(insert.text)


# Categories
# data = {}
# data['CategoryName'] = 'thao'
# data['Description'] = 'hihi'

# insert = requests.post('http://192.168.1.4:5000/Categories', json=data)
# print(insert.text)

# data = {}
# data['CategoryName'] = 'long oc cho'
# data['Description'] = 'cc'
# insert = requests.put('http://192.168.0.116:5000/Categories/2' ,json=data)
# print(insert.text)

# insert = requests.delete('http://192.168.1.4:5000/Categories/3' ,json=data)
# print(insert.text)


# Employees
# data = {}
# data['LastName'] = 'thao'
# data['FirstName'] = 'hihi'
# data['BirthDate'] = 'thao'
# data['Photo'] = 'hihi'
# data['Notes'] = 'thao'

# insert = requests.post('http://192.168.0.116:5000/Employees', json=data)
# print(insert.text)

# data = {}
# data['LastName'] = 'long lz'
# data['FirstName'] = 'oc cho'
# data['BirthDate'] = 'thao'
# data['Photo'] = 'hihi'
# data['Notes'] = 'thao'
# insert = requests.put('http://192.168.0.116:5000/Employees/2' ,json=data)
# print(insert.text)

# insert = requests.delete('http://192.168.0.116:5000/Employees/2' ,json=data)
# print(insert.text)


# OrderDetails
# data = {}
# data['OrderID'] = 1
# data['ProductID'] = 2
# data['Quantity'] = 'thao'

# insert = requests.post('http://192.168.1.8:5000/OrderDetails', json=data)
# print(insert.text)

# data = {}
# data['OrderID'] = 1
# data['ProductID'] = 2
# data['Quantity'] = 'thang dep trai'
# insert = requests.put('http://192.168.1.8:5000/OrderDetails/1' ,json=data)
# print(insert.text)

# insert = requests.delete('http://192.168.1.8:5000/OrderDetails/1' ,json=data)
# print(insert.text)
#cha ra sao // ma sao build lau the nhi..giong nhu b..cahr hiểu nhẽ ra có rồi hì build nhanh boi..h build loi lai vcl

# Orders
# data = {}
# data['CustomerID'] = 1
# data['EmployeeID'] = 2
# data['OrderDate'] = 'thao'
# data['ShipperID'] = 1

# insert = requests.post('http://192.168.1.7:5000/Orders', json=data)
# print(insert.text)

# data = {}
# data['OrderID'] = 1
# data['ProductID'] = 2
# data['Quantity'] = 'thang dep trai'
# insert = requests.put('http://192.168.1.8:5000/OrderDetails/1' ,json=data)
# print(insert.text)

# insert = requests.delete('http://192.168.1.8:5000/OrderDetails/1' ,json=data)
# print(insert.text)


# Products
# data = {}
# data['ProductName'] = 'vu'
# data['SupplierID'] = 2
# data['CategoryID'] = 1
# data['Unit'] = 'hihi'
# data['Price'] = '10'
# print(data)
# insert = requests.post('http://192.168.1.10:5000/Products', json=data)
# print(insert.text)


# data = {}
# data['ProductName'] = 'lz'
# data['SupplierID'] = 2
# data['CategoryID'] = 1
# data['Unit'] = 'hihi'
# data['Price'] = '10'
# insert = requests.put('http://192.168.1.7:5000/Products/1' ,json=data)
# print(insert.text)

# insert = requests.delete('http://192.168.1.7:5000/Products/1' ,json=data)
# print(insert.text)



# Shippers
# data = {}
# data['ShipperName'] = 'thang'
# data['Phone'] = '010101'
# insert = requests.post('http://192.168.1.7:5000/Shippers', json=data)
# print(insert.text)

# data = {}
# data['ShipperName'] = 'cc'
# data['Phone'] = '010101'
# insert = requests.put('http://192.168.1.6:5000/Shippers/1' ,json=data)
# print(insert.text)

# insert = requests.delete('http://192.168.1.6:5000/Shippers/1' ,json=data)
# print(insert.text)



# Suppliers;
# data = {}
# data['SupplierName'] = 'thang'
# data['ContactName'] = '010101'
# data['Address'] = 'thang'
# data['City'] = '010101'
# data['PostalCode'] = 'thang'
# data['Country'] = '010101'
# data['Phone'] = 'thang'
# insert = requests.post('http://192.168.1.6:5000/Suppliers', json=data)
# print(insert.text)

# data = {}
# data['SupplierName'] = 'cc'
# data['ContactName'] = '010101'
# data['Address'] = 'thang'
# data['City'] = '010101'
# data['PostalCode'] = 'thang'
# data['Country'] = '010101'
# data['Phone'] = 'thang'
# insert = requests.put('http://192.168.1.6:5000/Suppliers/1' ,json=data)
# print(insert.text)

# insert = requests.delete('http://192.168.1.6:5000/Suppliers/1' ,json=data)
# print(insert.text)