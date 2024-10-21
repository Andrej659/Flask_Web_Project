from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from storage_file import Shirts, Jeans, Trousers, Accessories

app = Flask(__name__)  # needed to start Flask
app.debug = True    # needed to start Flask
bootstrap = Bootstrap(app)  # starts bootstrap on the app

cart = []  # initiating my cart as a list

# this list is all items that are available in the shop
items = [Shirts(1, "White T-Shirt", 33, "static/imgs/white_tee.jpg"),
         Shirts(2, "Black T-Shirt", 24, "static/imgs/black_tee.jpg"),
         Shirts(3, "Red T-Shirt", 35, "static/imgs/red_tee.jpg"),
         Shirts(4, "Blue T-Shirt", 40, "static/imgs/blue_tee.jpg"),
         Jeans(5, "Skinny Jeans", 50, "static/imgs/skinny_jeans.jpg"),
         Jeans(6, "Baggy Jeans", 25, "static/imgs/baggy_jeans.jpg"),
         Jeans(7, "Boyfriend Jeans", 34, "static/imgs/boyf_jeans.jpg"),
         Jeans(8, "Bootcut Jeans", 31, "static/imgs/bootcut_jeans.jpg"),
         Trousers(9, "Courdoy Trousers", 33, "static/imgs/corduroyTrousers.jpg"),
         Trousers(10, "Twill-Chinos Trousers", 24, "static/imgs/Twill_Chinos.jpg"),
         Trousers(11, "Wool Trousers", 35, "static/imgs/wool-trousers.jpg"),
         Trousers(12, "Relaxed-legged Trousers", 40, "static/imgs/Relaxed-Legged_Trousers.jpg"),
         Accessories(13, "Necklace", 200, "static/imgs/necklace.jpg"),
         Accessories(14, "Watch", 150, "static/imgs/watch.jpg"),
         Accessories(15, "Ring", 234, "static/imgs/rings.jpg"),
         Accessories(16, "Earrings", 131, "static/imgs/earrings.jpg")]


@app.route("/")  # route that leads to the Home Page
def frontpage():
    return render_template('front-page.html')


@app.route("/shirts")  # route that leads to the Shirts Page
def shirts():
    shirtsList = [item for item in items if isinstance(item, Shirts)]  # selects only Shirts objects
    return render_template('shirts.html', objects=shirtsList)


@app.route("/jeans")  # route that leads to the Jeans Page
def jeans():
    jeansList = [item for item in items if isinstance(item, Jeans)]  # selects only Jeans objects
    return render_template('jeans.html', objects=jeansList)


@app.route("/trousers")  # route that leads to the Trousers Page
def trousers():
    trousersList = [item for item in items if isinstance(item, Trousers)]  # selects only Trousers objects
    return render_template('trousers.html', objects=trousersList)


@app.route("/accessories")  # route that leads to the Accessories Page
def accessories():
    accessoriesList = [item for item in items if isinstance(item, Accessories)]  # selects only Accessories objects
    return render_template('accessories.html', objects=accessoriesList)


@app.route("/about")  # route that leads to the About Page
def about():
    return render_template('about.html')


@app.route("/cartItems")  # route that leads to the Cart Page
def cartitems():
    cartItems = [item for item in cart]
    return render_template('cartItems.html', objects=cartItems)


@app.route("/clothes")   # route that leads to the Clothing Page
def clothes():
    storage = []
    for item in items:
        if isinstance(item, Shirts):
            storage.append(item)
        if isinstance(item, Jeans):
            storage.append(item)
        if isinstance(item, Trousers):
            storage.append(item)
    return render_template('clothing.html', objects=storage)


@app.route("/jeansNtrousers")   # route that leads to the Jeansntrousers Page
def jeansntrousers():
    storage = []
    for item in items:
        if isinstance(item, Jeans):
            storage.append(item)
        if isinstance(item, Trousers):
            storage.append(item)
    return render_template('jeansNtrousers.html', objects=storage)


@app.route('/buyThis', methods=['POST'])   # route that fetches me data from the server and adds items to the cart
def buy_this():
    data = request.get_json()  # here I'm parsing the json data and saving it
    itemId = data['itemId']  # here I'm searching for the data about itemId in the saved data
    for item in items:  # for loop that selects item based on their id
        if int(format(itemId)) == item.id:
            cart.append(item)
            return '{} added to cart'.format(item.name)


@app.route("/checkout")   # route that leads to the Checkout Page
def checkout():
    for i in range(0, len(cart) - 1):  # cleans the cart
        cart.remove(cart[i])
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)