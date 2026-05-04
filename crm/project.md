# Customer Relation Management  

---

## TEAM MEMBERS
- G.Vishnu (23311a6615)
- B.Abhinay (23311a6623)
- K.B.Praneeth (23311a6624)

---

## GUIDED BY
**B. VIJAY KUMAR**

---

# 1. ABSTRACT

This CRM system is a comprehensive web application designed to efficiently manage customer data, sales operations, and business communications. The platform supports dual role-based access for Admin and Customer users, enabling seamless product browsing, inventory management, purchasing, messaging, and support ticket resolution. It automates lead management, tracks customer status (lead/converted/lost), and enhances customer relationships through a structured and interactive digital platform. The system improves business efficiency, centralizes data management, and provides analytics for better decision-making.

---

# 2. INTRODUCTION

Customer Relationship Management (CRM) system is a strategic software solution designed to manage and analyze customer interactions throughout the business lifecycle. This project provides a modern web-based solution for handling customer details, sales tracking, product management, and real-time communication. It streamlines business operations, organizes customer information systematically, provides actionable insights, and supports better decision-making using a comprehensive role-based system for Admin and Customer users with interactive features and secure authentication.

---

# 3. OBJECTIVES

- **Develop a web-based CRM system** for efficient customer relationship and sales management
- **Provide secure role-based access** with CAPTCHA protection for Admin and Customer users
- **Enable product management** including browsing, search, cart management, and purchase functionality
- **Support multi-channel communication** between customers and admin through messaging and support tickets
- **Track customer lifecycle** including lead status, conversion, and customer segmentation
- **Provide analytics and reporting** for sales tracking, performance monitoring, and business growth analysis
- **Ensure data security** through password encryption and secure session management
- **Enable ticket-based support** with file upload capability for efficient issue resolution

---

# 4. TECHNOLOGIES USED

| Category | Technologies |
|----------|---------------|
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5, Font Awesome Icons |
| **Backend** | Python 3.13, Flask Framework |
| **Database** | SQLite3 / MySQL (Configurable) |
| **ORM** | SQLAlchemy |
| **Security** | Werkzeug (Password hashing, secure file handling) |
| **Session Management** | Flask Sessions |
| **IDE/Editor** | Visual Studio Code |
| **Version Control** | Git |

---

# 5. SYSTEM MODULES

### 1. **Authentication Module**
Handles secure user registration and login with CAPTCHA verification, role-based access control (Admin/Customer), and session management for secure authentication.

### 2. **Admin Dashboard Module**
Provides comprehensive analytics including total sales revenue, lead count, customer conversion metrics, and open support tickets. Enables real-time monitoring of business performance and customer engagement.

### 3. **Product Management Module**
Allows admins to create, update, and delete products with company association. Enables customers to browse products, search by name, view details, add to cart, and proceed with checkout for purchases.

### 4. **Customer Management Module**
Tracks customer information including profile details, contact information, company association, and customer lifecycle status (lead/converted/lost). Supports bulk updates and customer segmentation.

### 5. **Shopping Cart & Order Module**
Implements shopping cart functionality with add/remove items, quantity management, order creation, and purchase history tracking. Integrates with checkout process and payment status management.

### 6. **Communication & Support Module**
Enables real-time messaging between customers and admin, product tagging in messages for context, ticket creation for issue reporting, file upload for payment proofs, and ticket status tracking (open/closed).

### 7. **Database Management Module**
Persists and retrieves all system data including users, products, orders, messages, and tickets using SQLite/MySQL. Ensures data integrity, relationships, and efficient query performance.

### 8. **User Profile Module**
Allows customers to view and update their profile information including name, phone, age, gender, address, work details, and contact information.

---

# 6. DETAILED MODULE DESCRIPTION

### **Authentication Module**
- **Registration**: Users can sign up as Customer or Admin with name, email, phone, age, gender, address, work, and contact information
- **Login**: Secure login with email and password verification using hashing
- **CAPTCHA**: Math-based CAPTCHA prevents automated attacks
- **Session Management**: Flask sessions maintain user login state across requets
- **Role-Based Access Control**: Different features available based on user role (Admin/Customer)

### **Admin Dashboard Module**
- **Sales Analytics**: Displays total revenue from all completed orders
- **Lead Tracking**: Shows total leads in the system
- **Customer Conversion**: Tracks converted customers from leads
- **Open Tickets**: Displays count of unresolved support tickets
- **Visualization**: Chart-based representation of key metrics
- **User Management**: View and manage all registered users
- **Product Management**: Add, edit, delete, and bulk update products
- **Order Monitoring**: Track all customer orders and purchase history

### **Product Management Module**
- **Search Functionality**: Real-time product search by name for customers
- **Product Catalog**: Browse all available products with details and pricing
- **Company Association**: Products linked to company/vendor for organization
- **Cart Management**: Add products to cart with quantity selection
- **Checkout**: Complete order creation from cart items
- **Product Details**: Display name, description, price, and company information

### **Customer Management Module**
- **Customer Profile**: Store and manage comprehensive customer information
- **Status Tracking**: Monitor customer lifecycle (lead → converted/lost)
- **Search & Filter**: Find customers by various criteria
- **Bulk Operations**: Update multiple customer records efficiently
- **Segmentation**: Organize customers by status for targeted actions

### **Shopping Cart & Order Module**
- **Cart Operations**: Add items, update quantity, remove items
- **Checkout Process**: Calculate total, create order, manage payment status
- **Order History**: Customers view their past purchases and order details
- **Order Items**: Track individual products within each order
- **Status Management**: Mark orders as paid/pending for inventory tracking

### **Communication & Support Module**
- **Customer Messaging**: Direct messaging between individual customers and admin
- **Admin Inbox**: Centralized message management for admin users
- **Product Context**: Tag products in messages for specific issue reference
- **Ticket System**: Create support tickets with detailed issue description
- **Attachment Support**: Upload payment proofs or supporting documents
- **Ticket Status**: Track ticket progress (open/closed/resolved)
- **Real-time Updates**: Check for new messages and ticket notifications

### **Database Management Module**
- **Users Table**: Stores user accounts with encrypted passwords
- **Products Table**: Maintains product catalog with pricing
- **Orders & OrderItems**: Tracks purchases and order details
- **CartItems**: Manages temporary shopping cart state
- **Messages**: Stores communication history with timestamps
- **Tickets**: Persists support tickets with attachments
- **Data Integrity**: Foreign keys ensure referential integrity
- **Relationships**: Establishes one-to-many and many-to-many connections

### **User Profile Module**
- **View Profile**: Customers see their registered information
- **Update Profile**: Edit name, phone, age, gender, address, work, contact
- **Data Persistence**: Changes saved securely to database
- **Validation**: Input validation for data quality

---

# 7. ER DIAGRAM

## **Entities and Attributes**

### **Users Table**
```
User
├── id (Primary Key) - Integer, Auto-increment
├── name - String(150), Not Null
├── email - String(150), Unique, Not Null
├── password - String(256), Not Null (Hashed)
├── role - String(20), Not Null (admin/customer)
├── status - String(20), Default: 'lead' (lead/converted/lost)
├── phone - String(30), Optional
├── age - Integer, Optional
├── gender - String(20), Optional
├── address - String(250), Optional
├── work - String(200), Optional
├── contact - String(80), Optional
└── company - String(120), Optional
```

### **Products Table**
```
Product
├── id (Primary Key) - Integer, Auto-increment
├── name - String(150), Not Null
├── price - Float, Not Null
├── description - String(300), Optional
└── company - String(120), Optional, Default: 'TechX Nologoe'
```

### **Orders Table**
```
Order
├── id (Primary Key) - Integer, Auto-increment
├── user_id (Foreign Key) → User.id, Not Null
├── total - Float, Not Null
├── status - String(30), Not Null (paid/pending)
└── created_at - DateTime, Not Null
```

### **OrderItems Table**
```
OrderItem
├── id (Primary Key) - Integer, Auto-increment
├── order_id (Foreign Key) → Order.id, Not Null
├── product_id (Foreign Key) → Product.id, Not Null
├── quantity - Integer, Not Null
└── price - Float, Not Null
```

### **CartItems Table**
```
CartItem
├── id (Primary Key) - Integer, Auto-increment
├── user_id (Foreign Key) → User.id, Not Null
├── product_id (Foreign Key) → Product.id, Not Null
└── quantity - Integer, Default: 1, Not Null
```

### **Messages Table**
```
Message
├── id (Primary Key) - Integer, Auto-increment
├── sender_id (Foreign Key) → User.id, Optional
├── receiver_id (Foreign Key) → User.id, Optional
├── role - String(20), Not Null (customer/admin)
├── content - Text, Not Null
└── created_at - DateTime, Not Null.
```

### **Tickets Table**
```
Ticket
├── id (Primary Key) - Integer, Auto-increment
├── product_id (Foreign Key) → Product.id, Not Null
├── customer_id (Foreign Key) → User.id, Not Null
├── issue - Text, Not Null
├── payment_proof - Text, Optional (File path)
├── status - String(30), Default: 'open' (open/closed/resolved)
└── created_at - DateTime, Not Null
```

## **Relationships**

```
👉 One User → Many Orders
   User.id ←→ Order.user_id

👉 One User → Many CartItems
   User.id ←→ CartItem.user_id

👉 One User → Many Messages (as sender)
   User.id ←→ Message.sender_id

👉 One User → Many Messages (as receiver)
   User.id ←→ Message.receiver_id

👉 One User → Many Tickets
   User.id ←→ Ticket.customer_id

👉 One Product → Many OrderItems
   Product.id ←→ OrderItem.product_id

👉 One Product → Many CartItems
   Product.id ←→ CartItem.product_id

👉 One Product → Many Tickets
   Product.id ←→ Ticket.product_id

👉 One Order → Many OrderItems
   Order.id ←→ OrderItem.order_id
```

---

# 8. SYSTEM FEATURES

## **Customer Features**
✅ User Registration and Secure Login
✅ Product Browsing and Search
✅ Shopping Cart Management
✅ Order Placement and Payment
✅ Order History Tracking
✅ Profile Management
✅ Direct Messaging with Admin
✅ Support Ticket Creation
✅ Payment Proof Upload
✅ Notification for Messages

## **Admin Features**
✅ Dashboard with Business Analytics
✅ Customer Management and Segmentation
✅ Product Catalog Management (Add/Edit/Delete)
✅ Bulk Product Operations
✅ Order and Sales Tracking
✅ Message Management
✅ Support Ticket Resolution
✅ Lead Tracking and Conversion Metrics
✅ User Monitoring and Management
✅ System Configuration

---

# 9. FUNCTIONAL REQUIREMENTS

| Requirement | Description |
|-------------|-------------|
| **User Registration** | Customers and admins can create accounts with personal information and role selection |
| **Secure Authentication** | Login with email/password and CAPTCHA protection for security |
| **Role-Based Access Control** | Different features accessible based on user role (Admin/Customer) |
| **Product Management** | Admin can create, read, update, delete products; customers can browse and search |
| **Shopping Cart** | Add/remove products, update quantities, calculate totals |
| **Order Management** | Create orders from cart, track order status, view order history |
| **Messaging System** | Real-time communication between customers and admin with timestamps |
| **Ticket Support** | Create support tickets, upload payment proofs, track ticket status |
| **Admin Dashboard** | Display sales, leads, conversions, and open tickets analytics |
| **Customer Profile** | View and update customer information and personal details |
| **Search Functionality** | Search products and customers by name/criteria |
| **Status Tracking** | Monitor customer lifecycle (lead/converted/lost) |
| **Data Persistence** | All data stored securely in database with relationships |

---

# 10. NON-FUNCTIONAL REQUIREMENTS

| Requirement | Description |
|-------------|-------------|
| **Security** | Password encryption using Werkzeug hashing, CAPTCHA protection, session-based authentication |
| **Performance** | Fast page load times, optimized database queries, efficient caching |
| **Scalability** | Database supports growth, modular code architecture allows feature expansion |
| **Usability** | Intuitive UI, responsive design, easy navigation, clear buttons and forms |
| **Reliability** | 99% uptime, proper error handling, data backup mechanisms |
| **Maintainability** | Clean code structure, documented functions, separation of concerns |
| **Compatibility** | Works on all modern browsers (Chrome, Firefox, Safari, Edge) |
| **Accessibility** | WCAG compliance, keyboard navigation, screen reader support |
| **Data Integrity** | Foreign key constraints, transaction management, data validation |
| **Availability** | 24/7 system availability for business operations |

---

# 11. SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                          │
│             (Web Browser - Any Device)                       │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/HTTPS Requests
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   FRONTEND LAYER                             │
│  HTML | CSS | JavaScript | Bootstrap | Font Awesome        │
│           (User Interface & Client-Side Logic)              │
└────────────────────────┬────────────────────────────────────┘
                         │ AJAX/Form Requests
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND LAYER                              │
│              Flask Web Server (Python)                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │   Routing | Request Handling | Business Logic       │  │
│  │   Session Management | Authentication | Validation  │  │
│  │   File Upload Handling | Email Processing           │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │ SQL Queries
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   DATA ACCESS LAYER                          │
│              SQLAlchemy ORM (Python)                         │
│     (Object-Relational Mapping & Query Building)            │
└────────────────────────┬────────────────────────────────────┘
                         │ SQL Commands
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   DATABASE LAYER                             │
│         SQLite3 / MySQL (Depending on Config)               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Users | Products | Orders | Messages | Tickets     │  │
│  │  CartItems | OrderItems | (All Persistent Data)     │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘

FLOW:
1. User accesses CRM through web browser
2. Frontend renders HTML/CSS and handles user interactions
3. JavaScript sends AJAX requests or form submissions
4. Flask backend receives and routes requests to appropriate handler
5. Handlers validate input, process business logic, manage sessions
6. SQLAlchemy ORM translates operations to SQL queries
7. Database executes queries and returns data
8. Backend processes response and sends JSON/HTML back to frontend
9. Frontend renders response and updates user interface
10. User sees updated content and results
```

---

# 12. INSTALLATION & SETUP

## **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## **Installation Steps**

```bash
# 1. Navigate to project directory
cd d:/crm

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install Flask Flask-SQLAlchemy Werkzeug

# 5. Run the application
python app.py

# 6. Access the application
# Open browser and navigate to: http://127.0.0.1:5000
```

## **Database Configuration**

The system uses SQLite by default. To use MySQL:

```bash
# Install MySQL connector
pip install PyMySQL cryptography

# Set environment variable (Windows PowerShell):
$env:DATABASE_URL = 'mysql+pymysql://root:password@localhost/crm'

# Set environment variable (Linux/Mac):
export DATABASE_URL='mysql+pymysql://root:password@localhost/crm'
```

---

# 13. USER GUIDE

### **For Customers**

1. **Registration**: Click "Sign Up" → Fill details → Select "Customer" role → Complete CAPTCHA → Submit
2. **Login**: Enter email/password → Complete CAPTCHA → Access dashboard
3. **Browse Products**: View all available products with prices and descriptions
4. **Search Products**: Use search bar to find specific products by name
5. **Add to Cart**: Click "Add to Cart" button on product
6. **Checkout**: Go to cart → Review items → Click "Checkout" → Order confirmed
7. **View Orders**: Navigate to "Orders" section to see purchase history
8. **Message Admin**: Use messaging section to communicate with support team
9. **Create Ticket**: Submit support tickets with issue description and payment proof
10. **Update Profile**: Edit personal information in profile section

### **For Admins**

1. **Login**: Enter email/password → Complete CAPTCHA → Access admin panel
2. **Dashboard**: View sales metrics, leads, conversions, and open tickets
3. **Manage Products**: Add new products, edit existing ones, delete products
4. **Manage Users**: View all customers, update status, segment customers
5. **View Orders**: Monitor all customer orders and sales
6. **Reply Messages**: Check messages from customers and respond
7. **Handle Tickets**: Review support tickets and mark as resolved
8. **Bulk Operations**: Perform batch updates on multiple products or users

---

# 14. FUTURE ENHANCEMENTS

- 📧 Email notification system for orders and messages
- 💳 Real payment gateway integration (Stripe, PayPal)
- 📱 Mobile application (Android/iOS)
- 📊 Advanced analytics and reporting with charts
- 🔔 Push notifications for real-time alerts
- 📁 Document management system
- 🌍 Multi-language support
- 🔍 AI-powered recommendation system
- 📅 Appointment scheduling system
- 🔐 Two-factor authentication (2FA)
- 📈 ML-based customer behavior analysis
- 🌐 API endpoints for third-party integrations

---

# 15. CONCLUSION

This CRM web application successfully demonstrates a comprehensive solution for managing customer relationships, sales operations, and business communications in a structured, secure, and scalable manner. The system provides dual interfaces for Admin and Customer roles with distinct features tailored to each user type.

**Key Achievements:**
- ✅ Secure authentication with role-based access control
- ✅ Complete product and inventory management
- ✅ Seamless shopping experience with cart and checkout
- ✅ Multi-channel communication (messaging and tickets)
- ✅ Business analytics and lead tracking
- ✅ Efficient database design with proper relationships
- ✅ Responsive and user-friendly interface
- ✅ Scalable architecture for future growth

**Business Impact:**
- Improves data organization and customer information management
- Enhances customer interaction and satisfaction
- Automates lead management and sales tracking
- Provides actionable insights for decision-making
- Reduces manual processes and improves efficiency
- Enables better customer service through ticket support
- Supports business growth with scalable infrastructure

This CRM system makes business processes more structured, automated, and effective, positioning organizations for sustainable growth and improved customer relationships in the digital age.

---

## **DOCUMENT METADATA**
- **Document Type**: Project Documentation
- **Version**: 1.0
- **Last Updated**: March 30, 2026
- **Status**: Complete
- **Document ID**: CRM-PROJ-001

---

*End of Document*
