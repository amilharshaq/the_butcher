from flask import *
from src.db import *
import os
from werkzeug.utils import secure_filename

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


@app.route("/add_products")
def add_products():
    return render_template("add_products.html")


@app.route("/insert_products", methods=['post'])
def insert_products():
    category = request.form['select']
    name = request.form['textfield']
    price = request.form['textfield2']
    description = request.form['textfield3']
    stock = request.form['textfield4']

    main_image = request.files['img1']
    sub_image1 = request.files['img2']
    sub_image2 = request.files['img3']
    sub_image3 = request.files['img4']

    main_image_name = secure_filename(main_image.filename)
    main_image.save(os.path.join('static/product_images', main_image_name))

    sub_image1_name = secure_filename(sub_image1.filename)
    main_image.save(os.path.join('static/product_images', sub_image1_name))

    sub_image2_name = secure_filename(sub_image2.filename)
    main_image.save(os.path.join('static/product_images', sub_image2_name))

    sub_image3_name = secure_filename(sub_image3.filename)
    main_image.save(os.path.join('static/product_images', sub_image3_name))

    qry = "INSERT INTO `product` VALUES(NULL,%s,%s,%s,%s,%s)"
    id = iud(qry,(name,price,description,stock,category))

    qry = "INSERT INTO `product_images` VALUES(NULL,%s,%s,%s,%s,%s)"
    iud(qry,(id,main_image_name,sub_image1_name,sub_image2_name,sub_image3_name))

    return '''<script>alert("Successfully added");window.location="add_products"</script>'''


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

