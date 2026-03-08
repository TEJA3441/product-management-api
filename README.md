# Product Management Backend API

## Project Overview

This project is a **Product Management Backend System** built using **FastAPI and PostgreSQL**. The system provides APIs to manage products with **role-based access control (RBAC)**. It allows administrators to manage product data while regular users can only view product information.

The backend also includes **authentication, pagination, filtering, sorting, activity logging, and proper error handling** to simulate a real-world backend service.

---

## Features

### User Authentication
- User Registration
- User Login
- Password hashing using bcrypt
- JWT Token-based authentication

### Role-Based Access Control (RBAC)

Two roles are implemented:

**Admin**
- Create products
- Update products
- Delete products
- View products

**User**
- View products only

Admin-only routes are protected using RBAC dependencies.

---

## Product Management APIs

The system provides the following product-related APIs:

- Add a new product
- Fetch all products
- Fetch a product by ID
- Update product (Admin only)
- Delete product (Admin only)

Each product contains:

- Product Name
- Description
- Price
- Category
- Created Timestamp

---

## Pagination, Filtering and Sorting

The product listing API supports:

### Pagination
Example:

GET /products?page=1&limit=10

### Filtering

Filter products by:

- Category
- Minimum price
- Maximum price

Examples:

GET /products?category=electronics

GET /products?min_price=1000&max_price=5000

### Sorting

Products can be sorted by price.

GET /products?sort=price_asc

GET /products?sort=price_desc

---

## Activity Logging

The system maintains activity logs whenever an admin performs product operations.

Actions logged include:

- Product Creation
- Product Update
- Product Deletion

Logs are stored in:

logs/activity.log

Example log entry:

2026-03-08 12:10:45 - Admin Ravi created product iPhone

---

## Database Schema

### Users Table

| Column | Type | Description |
|------|------|-------------|
| id | Integer | Primary Key |
| username | String | Username |
| email | String | User email |
| password | String | Hashed password |
| role | String | admin / user |

---

### Products Table

| Column | Type | Description |
|------|------|-------------|
| id | Integer | Primary Key |
| name | String | Product name |
| description | String | Product description |
| price | Float | Product price |
| category | String | Product category |
| created_at | Timestamp | Creation time |

---

### Logs Table (Optional)

| Column | Type | Description |
|------|------|-------------|
| id | Integer | Primary Key |
| action | String | Action performed |
| user_id | Integer | Admin performing action |
| product_id | Integer | Product affected |
| timestamp | Timestamp | Log time |

---

## Project Structure
