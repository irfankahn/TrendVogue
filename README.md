# Trend Vogue Ecommerce Application

Welcome to the **Trend Vogue Ecommerce Application**! This dynamic platform allows users to explore and purchase stylish clothing and accessories, featuring a seamless shopping experience powered by Python and Flask.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Product Catalog**: Browse a diverse selection of products, each with detailed information and reviews.
- **Shopping Cart**: Add and remove products from your cart, with real-time updates and total price calculations.
- **User Reviews**: Submit reviews for products using AJAX for a smooth user experience.
- **Responsive Design**: Access the application on any device, ensuring a user-friendly shopping experience.
- **Session Management**: Maintain user sessions for cart management.
- **Contact Form**: Reach out through a contact form to send messages.

## Installation

To get started with the Trend Vogue Ecommerce Application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/irfankahn/TrendVogue.git
   cd trend-vogue
   
## Set Up a Virtual Environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install Dependencies:

bash
pip install Flask

## Run the Application:

bash
python app.py
Visit http://127.0.0.1:5000 in your web browser.

# Usage
Navigate to the home page to view the product catalog.
Use the search feature to filter products by name or category.
Click on any product for more details and to submit reviews.
Manage your cart from the cart page, where you can view total prices and items.
Access the contact page to send inquiries.

## Routes
Route	Method	Description
/	GET	Display the homepage with product listings.
/cart	GET	Show items in the user's cart.
/add_to_cart/<product_id>	POST	Add a product to the cart.
/remove_from_cart/<product_id>	POST	Remove a product from the cart.
/checkout	GET	Complete the purchase and clear the cart.
/product/<product_id>	GET, POST	Display product details and handle reviews.
/about	GET	Show information about the application.
/contact	GET, POST	Display the contact form and handle submissions.
/submit_review/<product_id>	POST	Submit a review for a product.

# Technologies
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Database: In-memory product data (can be expanded to use a database)
Session Management: Flask sessions for cart handling

# Contributing
We welcome contributions! If you'd like to help improve the Trend Vogue Ecommerce Application, please fork the repository and submit a pull request.

