-- Create the database
CREATE DATABASE ecommerce_db;

-- Use the database
USE ecommerce_db;

-- Create the customers table
CREATE TABLE customers (
  customer_id INT PRIMARY KEY AUTO_INCREMENT, -- Primary key for the table
  first_name VARCHAR(50) NOT NULL, -- Customer's first name
  last_name VARCHAR(50) NOT NULL, -- Customer's last name
  email VARCHAR(100) NOT NULL, -- Customer's email address
  password VARCHAR(100) NOT NULL, -- Customer's password
  address VARCHAR(200) NOT NULL, -- Customer's address
  city VARCHAR(100) NOT NULL, -- Customer's city
  state VARCHAR(100) NOT NULL, -- Customer's state
  zip_code VARCHAR(20) NOT NULL, -- Customer's ZIP code
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for customer creation
  INDEX idx_customer_name (last_name, first_name) -- Index for searching by customer name
);

-- Create the orders table
CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT, -- Primary key for the table
  customer_id INT NOT NULL, -- Foreign key referencing customers table
  order_date DATE NOT NULL, -- Order date
  total_amount DECIMAL(10, 2) NOT NULL, -- Total amount of the order
  status VARCHAR(50) NOT NULL, -- Order status
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for order creation
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) -- Foreign key constraint
);

-- Create the products table
CREATE TABLE products (
  product_id INT PRIMARY KEY AUTO_INCREMENT, -- Primary key for the table
  name VARCHAR(100) NOT NULL, -- Product name
  description TEXT NOT NULL, -- Product description
  price DECIMAL(10, 2) NOT NULL, -- Product price
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for product creation
  INDEX idx_product_category (category) -- Index for searching by product category
);

-- Create the reviews table
CREATE TABLE reviews (
  review_id INT PRIMARY KEY AUTO_INCREMENT, -- Primary key for the table
  product_id INT NOT NULL, -- Foreign key referencing products table
  customer_id INT NOT NULL, -- Foreign key referencing customers table
  rating INT NOT NULL, -- Review rating
  comment TEXT NOT NULL, -- Review comment
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for review creation
  FOREIGN KEY (product_id) REFERENCES products(product_id), -- Foreign key constraint
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id), -- Foreign key constraint
  INDEX idx_review_product (product_id), -- Index for searching by product ID
  INDEX idx_review_customer (customer_id) -- Index for searching by customer ID
);
