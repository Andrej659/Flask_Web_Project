# AMShop

This project is a simple web application that simulates a basic webshop experience. It is built using Python's Flask framework and allows users to browse through various categories of items, add products to a shopping cart, and proceed to checkout.

## Features

- Browse different categories of products, including:
  - Shirts
  - Jeans
  - Trousers
  - Accessories
- Add selected items to a shopping cart.
- View the contents of the cart.
- Checkout and clear the cart after completing the purchase.

## Tools & Technologies

This project uses the following tools and libraries:

- **Python**: Main programming language used for backend logic.
- **Flask**: A lightweight WSGI web application framework used to build the web application.
- **Flask-Bootstrap**: Used to integrate Bootstrap into the Flask app for styling and responsive design.
- **HTML & Jinja2**: For rendering templates and dynamic web pages.
- **CSS & Bootstrap**: To style the front-end and ensure responsiveness.
- **JavaScript**: For handling interactivity, including sending `POST` requests for adding items to the cart.
- **Jinja2 Templating Engine**: For dynamically rendering HTML pages with Python data.
- **Virtualenv**: To create an isolated Python environment for managing dependencies.

## Installation

1. Clone the repository:

    ```bash
    git clone <your-repo-url>
    ```

2. Navigate into the project directory:

    ```bash
    cd flask-app
    ```

3. Set up a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:
        ```bash
        venv\Scripts\activate
        ```
    - For macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure the `requirements.txt` includes `Flask` and `Flask-Bootstrap`:

    ```text
    Flask
    Flask-Bootstrap
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`.

3. You will be directed to the homepage where you can browse different product categories.

4. Add items to the cart by selecting them and clicking on "Add to Cart."

5. Review the items in your cart by clicking on the cart icon or visiting the cart page.

6. Proceed to checkout when ready.

## Project Overview

This simple webshop allows users to explore various categories of products, such as shirts, jeans, trousers, and accessories. Users can add items to their cart and view them on the cart page. The checkout option will clear the cart after simulating a purchase.


## License

This project is open-source and available under the MIT License.


