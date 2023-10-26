# E-Commerce API  

An API built using Django and Django Rest Framework for e-commerce functionality, allowing users to browse products, manage carts, and place orders.

## Features 
**Product Browsing:** View product categories and individual products.

**Cart Management:** Add products to cart, update cart item quantities, and view cart details.

**Order Placement:** Check out a cart, creating an order with associated items.

## Installation
#### 1. Clone the Repository:
`git clone <repository-url>`
`cd Ecommerce`
#### 2.Set Up a Virtual Environment:
`python -m venv venv`
use venv\Scripts\activate
#### 3.Install Dependencies:
`pip install -r requirements.txt`
#### 4.Run Migrations:
`python manage.py makemigrations`
python manage.py migrate`
#### 5.Load Initial Data (Optional):
`python manage.py loaddata api/fixtures/initial_data.json`
#### 6.Run the Development Server:
`python manage.py runserver`





