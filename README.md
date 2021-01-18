# Entity
## Customer
* CustomerID
* CustomerName
* ContactName
* Address
* City
* PostalCode
* Country
## Categories
* CategoryID
* CategoryName
* Description
## Employees
* EmployeeID 
* LastName 
* FirstName 
* BirthDate 
* Photo 
* Notes 
## OrderDetails
* OrderDetailID 
* OrderID 
* ProductID 
* Quantity 
## Orders
* OrderID 
* CustomerID 
* EmployeeID 
* OrderDate 
* ShipperID 
## Products
* ProductID 
* ProductName 
* SupplierID 
* CategoryID 
* Unit 
* Price 
## Shippers
* ShipperID 
* ShipperName 
* Phone 
## Suppliers
* SupplierID 
* SupplierName 
* ContactName 
* Address 
* City
* PostalCode
* Country
* Phone 
# API
## Customer
### Get All Customer
* Request
  * Method: GET
  * Endpoint: /customer/all
  * Params: None
  * Body: None
 * Reponsive: [Customer]
### Get One Customer
* Request
  * Method: GET
  * Endpoint: /customer/get/:CustomerID 
  * Params: id
  * Body: None
 * Reponsive: [Customer]
### Add a customer
 * Request
  * Method: POST
  * Endpoint: /customer
  * Params: None
  * Body: 
    * CustomerName : string
    * ContactName : string
    * Address : string
    * City : string
    * PostalCode : string
    * Country : string
 * Reponsive: Message
### Update a customer
 * Request:
  * Method: PUT
  * Endpoint: /customer/:CustomerID 
  * Body:
    * CustomerName : string
    * ContactName : string
    * Address : string
    * City : string
    * PostalCode : string
    * Country : string
  * Response: Message
### Delete a customer
* Request:
  * Method: DELETE
  * Endpoint: /customer/:CustomerID 
  * Response: message
## Categories
### Get All Categories
* Request
  * Method: GET
  * Endpoint: /Categories/all
  * Params: None
  * Body: None
 * Reponsive: [Categories]
### Get One Categories
* Request
  * Method: GET
  * Endpoint: /Categories/get/CategoryID 
  * Params: id
  * Body: None
 * Reponsive: [Categories]
### Add a Categories
 * Request
  * Method: POST
  * Endpoint: /Categories
  * Params: None
  * Body: 
    * CategoryName: string
    * Description: string
 * Reponsive: Message
### Update a Categories
 * Request:
  * Method: PUT
  * Endpoint: /Categories/:CategoryID
  * Body:
    * CategoryName : string
    * Description : string
  * Response: message
### Delete a Categories
* Request:
  * Method: DELETE
  * Endpoint: /Categories/:CategoryID
  * Response: message
## Employees
### Get All Employees
* Request
  * Method: GET
  * Endpoint: /Employees/all
  * Params: None
  * Body: None
 * Reponsive: [Employees]
### Get One Employees
* Request
  * Method: GET
  * Endpoint: /Employees/get/EmployeeID  
  * Params: id
  * Body: None
 * Reponsive: [Employees]
### Add a Employees
 * Request
  * Method: POST
  * Endpoint: /Employees
  * Params: None
  * Body: 
    * LastName : string
    * FirstName : string
    * BirthDate : string
    * Photo : string
    * Notes : string
 * Reponsive: Message
### Update a Employees
 * Request:
  * Method: PUT
  * Endpoint: /Employees/:EmployeeID 
  * Body:
    * LastName : string
    * FirstName : string
    * BirthDate : string
    * Photo : string
    * Notes : string
  * Reponsive: Message
### Delete a Employees
* Request:
  * Method: DELETE
  * Endpoint: /Employees/:EmployeeID
  * Response: message
## OrderDetails
### Get All OrderDetails
* Request
  * Method: GET
  * Endpoint: /OrderDetails/all
  * Params: None
  * Body: None
 * Reponsive: [OrderDetails]
### Get One OrderDetails
* Request
  * Method: GET
  * Endpoint: /OrderDetails/get/OrderDetailID   
  * Params: id
  * Body: None
 * Reponsive: [OrderDetails]
### Add a OrderDetails
 * Request
  * Method: POST
  * Endpoint: /OrderDetails
  * Params: None
  * Body: 
    * OrderID  : int
    * ProductID  : int
    * Quantity  : string
 * Reponsive: Message
### Update a OrderDetails
 * Request:
  * Method: PUT
  * Endpoint: /OrderDetails/:OrderDetailID  
  * Body:
    * OrderID  : int
    * ProductID  : int
    * Quantity  : string
  * Reponsive: Message
### Delete a OrderDetails
* Request:
  * Method: DELETE
  * Endpoint: /OrderDetails/:OrderDetailID
  * Response: message
## Orders
### Get All Orders
* Request
  * Method: GET
  * Endpoint: /Orders/all
  * Params: None
  * Body: None
 * Reponsive: [Orders]
### Get One Orders
* Request
  * Method: GET
  * Endpoint: /Orders/get/OrderID    
  * Params: id
  * Body: None
 * Reponsive: [Orders]
### Add a Orders
 * Request
  * Method: POST
  * Endpoint: /Orders
  * Params: None
  * Body: 
    * CustomerID : int
    * EmployeeID : int
    * OrderDate : string
    * ShipperID : int
 * Reponsive: Message
### Update a Orders
 * Request:
  * Method: PUT
  * Endpoint: /Orders/:OrderID  
  * Body:
    * CustomerID : int
    * EmployeeID : int
    * OrderDate : string
    * ShipperID : int
  * Reponsive: Message
### Delete a Orders
* Request:
  * Method: DELETE
  * Endpoint: /Orders/:OrderID
  * Response: message
## Products
### Get All Products
* Request
  * Method: GET
  * Endpoint: /Products/all
  * Params: None
  * Body: None
 * Reponsive: [Products]
### Get One Products
* Request
  * Method: GET
  * Endpoint: /Products/get/ProductID    
  * Params: id
  * Body: None
 * Reponsive: [Products]
### Add a Products
 * Request
  * Method: POST
  * Endpoint: /Products
  * Params: None
  * Body: 
    * ProductName  : int
    * SupplierID  : int
    * CategoryID  : int
    * Unit  : string
    * Price : string
 * Reponsive: Message
### Update a Products
 * Request:
  * Method: PUT
  * Endpoint: /Products/:ProductID  
  * Body:
    * ProductName  : int
    * SupplierID  : int
    * CategoryID  : int
    * Unit  : string
    * Price : string
  * Reponsive: Message
### Delete a Products
* Request:
  * Method: DELETE
  * Endpoint: /Products/:ProductID
  * Response: message
## Shippers
### Get All Shippers
* Request
  * Method: GET
  * Endpoint: /Shippers/all
  * Params: None
  * Body: None
 * Reponsive: [Shippers]
### Get One Shippers
* Request
  * Method: GET
  * Endpoint: /Shippers/get/ShipperID    
  * Params: id
  * Body: None
 * Reponsive: [Shippers]
### Add a Shippers
 * Request
  * Method: POST
  * Endpoint: /Shippers
  * Params: None
  * Body: 
    * ShipperName : int
    * Phone : int
 * Reponsive: Message
### Update a Shippers
 * Request:
  * Method: PUT
  * Endpoint: /Shippers/:ShipperID  
  * Body:
    * ShipperName : int
    * Phone : int
  * Reponsive: Message
### Delete a Shippers
* Request:
  * Method: DELETE
  * Endpoint: /Shippers/:ShipperID
  * Response: message
## Suppliers
### Get All Suppliers
* Request
  * Method: GET
  * Endpoint: /Suppliers/all
  * Params: None
  * Body: None
 * Reponsive: [Suppliers]
### Get One Suppliers
* Request
  * Method: GET
  * Endpoint: /Suppliers/get/SupplierID    
  * Params: id
  * Body: None
 * Reponsive: [Suppliers]
### Add a Suppliers
 * Request
  * Method: POST
  * Endpoint: /Suppliers
  * Params: None
  * Body: 
    * SupplierName : string
    * ContactName : string
    * Address  : string
    * City  : string
    * PostalCode  : string
    * Country  : string
    * Phone  : string
 * Reponsive: Message
### Update a Suppliers
 * Request:
  * Method: PUT
  * Endpoint: /Suppliers/:SupplierID   
  * Body:
    * SupplierName : string
    * ContactName : string
    * Address  : string
    * City  : string
    * PostalCode  : string
    * Country  : string
    * Phone  : string
  * Reponsive: Message
### Delete a Suppliers
* Request:
  * Method: DELETE
  * Endpoint: /Suppliers/:SupplierID
  * Response: message
