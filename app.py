from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# Sample product data with reviews
products = [
    {"id": 1, "name": "Stylish Jacket", "price": 99.99, "image": "static/product1.jpg", "category": "men", "reviews": []},
    {"id": 2, "name": "Classic Sneakers", "price": 69.99, "image": "static/product2.jpg", "category": "men", "reviews": []},
    {"id": 3, "name": "Elegant Dress", "price": 89.99, "image": "static/product3.jpg", "category": "women", "reviews": []},
    {"id": 4, "name": "Casual Watch", "price": 49.99, "image": "static/product4.jpg", "category": "men", "reviews": []},
    {"id": 5, "name": "Chic Blouse", "price": 49.99, "image": "static/product5.jpg", "category": "women", "reviews": []},
    {"id": 6, "name": "High Heels", "price": 39.99, "image": "static/product6.jpg", "category": "women", "reviews": []},
    {"id": 7, "name": "Trendy Hoodie", "price": 59.99, "image": "static/product7.jpg", "category": "men", "reviews": []},  # New product
    {"id": 8, "name": "Summer Skirt", "price": 39.99, "image": "static/product8.jpg", "category": "women", "reviews": []}   # New product
]

@app.route('/')
def index():
    search_query = request.args.get('search', '').lower()
    filtered_products = [
        product for product in products
        if search_query in product['name'].lower() or search_query in product['category'].lower()
    ] if search_query else products
    return render_template('index.html', products=filtered_products)

@app.route('/cart')
def cart():
    cart_items = []
    total_price = 0

    if 'cart' not in session:
        session['cart'] = []

    for product_id in session['cart']:
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            cart_items.append(product)
            total_price += product['price']

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []

    if product_id not in session['cart']:
        session['cart'].append(product_id)
        flash('Product added to cart!', 'success')
    else:
        flash('Product is already in the cart!', 'info')

    return redirect(url_for('index'))

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    if 'cart' in session and product_id in session['cart']:
        session['cart'].remove(product_id)
        flash('Product removed from cart!', 'success')

    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    session.pop('cart', None)  # Clear the cart
    return "Thank you for your purchase!"

@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)

    if request.method == 'POST':
        data = request.get_json()
        review_text = data.get('review')
        star_rating = int(data.get('rating', 0))
        if review_text and star_rating:
            product['reviews'].append({'text': review_text, 'rating': star_rating})
            return jsonify({'text': review_text, 'rating': star_rating})

    return render_template('product.html', product=product)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash('Message sent!', 'success')  # Feedback to user
        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/submit_review/<int:product_id>', methods=['POST'])
def submit_review(product_id):
    product=next((p for p in products if p['id'] == product_id), None)
    review_text=request.form.get('review_text')
    star_rating=request.form.get('star_rating')

    if product and review_text and star_rating:
        product['reviews'].append({'text': review_text, 'rating': int(star_rating)})
        flash('Review submitted successfully!', 'success')

    return redirect(url_for('review'))

if __name__ == '__main__':
    app.run(debug=True)
