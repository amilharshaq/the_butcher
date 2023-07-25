from flask import *
from src.db import *

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login_code', methods=['post'])
def login_code():
    username = request.form['textfield']
    password = request.form['textfield2']
    qry = "select * from login where username=%s and password=%s"
    res = selectone(qry, (username, password))

    if res is None:
        return '''<script>alert("Invalid username or password");window.location="/"</script>'''
    elif res['type'] == "admin":
        return redirect("admin_home")
    else:
        return '''<script>alert("Invalid username or password");window.location="/"</script>'''


@app.route("/admin_home")
def admin_home():
    return render_template("home.html")


@app.route("/manage_products")
def manage_products():
    return render_template("manage_products.html")


@app.route("/filter_products", methods=['post'])
def filter_products():

    type = request.form['select']
    qry = "SELECT `product`.*,`product_images`.`main_image` FROM `product` JOIN `product_images` ON `product`.`id`=`product_images`.`pid` WHERE `product`.`category`=%s"
    res = selectall2(qry,type)

    return render_template("manage_products.html", val = res)

app.run(debug="true")

