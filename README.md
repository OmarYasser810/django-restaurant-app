Django Project: Restaurant Management System
Project Structure
The project contains 3 Django Apps: Menu, Orders, and Customers.
1- Menu App
Model: Item
- name (string)
- price (decimal)
- description (optional)
Features:
- Display all menu items (Template).
- Add new item (Create).
- Edit item (Update).
- Delete item (Delete).
2- Orders App
Models:
Order:
- customer_name (string)
- phone (string)
- created_at (datetime)
OrderItem:
- order (ForeignKey → Order)
- item (ForeignKey → Item from Menu)
- quantity (integer)
Features:
- Step 1: Create new order (enter customer name & phone).
- Step 2: Add items to the order (choose item & quantity).
- Display order details (customer info, items, total price).
- Update or delete order.
3- Customers App
Model: Customer
- name (string)
- email (optional)
- phone (string)
Relations:
- One-to-Many: Customer → Orders
Features:
- Display all customers.
- View customer details and their orders.
- Add, edit, delete customer.
Steps to Implement
1. Create a new Django project.
2. Create 3 apps: menu, orders, customers.
3. Define models in each app.
4. Apply migrations and set up the database.
5. Create views and templates for displaying and managing data.
6. Configure URLs for each app and include them in the main project.
7. Implement CRUD functionality for each app.
8. Style templates with Bootstrap or Tailwind (optional).
Bonus (Optional)
- Calculate total price for an order.
- Add search functionality for menu items.
