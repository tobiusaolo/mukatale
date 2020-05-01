from flask import Flask, request,url_for,render_template,redirect,g
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from json import dumps
import base64
import sqlite3
import io
from io import BytesIO
from flask_jsonpify import jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String,LargeBinary


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Mukatale.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db  = SQLAlchemy(app)
api = Api(app)
#Create user table 
class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    contact = db.Column(db.String)
    location = db.Column(db.String)
    def __init__(self,name,contact,location):
        self.name= name
        self.contact = contact
        self.location = location
#create table for orders
class Order(db.Model):
    __tablename__ = "orderz"
    id=db.Column(db.Integer,primary_key=True)
    user_id =db.Column(db.String)
    payment_method=db.Column(db.String)
    order_status=db.Column(db.String)
    product_name=db.Column(db.String)
    qty=db.Column(db.String)
    total_price=db.Column(db.String)
    date =db.Column(db.String)
    def __init__(self,user_id,payment_method,order_status,product_name,qty,total_price,date):
        self.user_id= user_id
        self.payment_method=payment_method
        self.order_status= order_status
        self.product_name = product_name
        self.qty = qty
        self.total_price = total_price
        self.date = date

    


#Create item table
class Item(db.Model):

    __tablename__ = "item"

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String) 
    price =db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.LargeBinary) 


    def __init__(self,title,price,description,image):
        self.title = title
        self.price = price
        self.description = description
        self.image = image 
DATABASE="Mukatale.db" 
def getConnection():
    con = getattr(g, '_database', None)
    if con is None:
        con = g._database = sqlite3.connect(DATABASE)
    return con 
# create api to display items
class Data(Resource):
    def get(self):
        db = getConnection()
        c = db.cursor()
        query = c.execute("select * from item")
        return {'items':[i[0] for i in query.fetchall()]}
#create api link for registering users
class Register(Resource):
    def post(self):
        db = getConnection()
        c = db.cursor()
        print(request.json)
        rname=request.json['rname']
        rcontact=request.json['rcontact']
        rlocation=request.json['rlocation']
        query = c.execute("insert into user(name,contact,location) values('{0}','{1}','{2}')".format(rname,rcontact,rlocation))

        return {'status':'success'}
#create api link for making orders
class Iorder(Resource):
    def get(self):
        db = getConnection()
        c = db.cursor()
        query = c.execute("select * from orderz")
        return {'orders':[i[0] for i in query.fetchall()]}
    def post(self):
        db = getConnection()
        c = db.cursor()
        print(request.json)
        ruser_id=request.json['ruser_id']
        rpayment=request.json['rpayment']
        rstatus=request.json['rstatus']
        rtitle=request.json['rtitle']
        rqty=request.json['rqty']
        rprice=request.json['rprice']
        rdate=request.json['rdate']
        query = c.execute("insert into orderz(user_id,payment_method,order_status,product_name,qty,total_price,date) values('{0}','{1}','{2}'),'{3}','{4}','{5}','{6}'".format(ruser_id,rpayment,rstatus,rtitle,rqty,rprice,rdate))
        return {'status':'success'}

@app.route('/')
def index():
    return render_template("home.html")
@app.route('/add_item')
def add_item():
    return render_template("add_item.html")
@app.route('/add_product',methods=['POST','GET'])
def add_product():
    if request.method == "POST":
        
        title=request.form["title"]
        
        price = request.form["price"]
        
        descrip = request.form["description"]
        
        image = request.files["image"]
        img=image.read()
        data=Item(title=title,price=price,description=descrip,image=img)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('list_view'))

@app.route('/list_view')
def list_view():
    img_df = []
    items = Item.query.all()
    # # base64.b64encode(file.image).decode('ascii')
    for i in items:
        images=base64.b64encode(i.image).decode('ascii')
        img_df.append(images)
    item_zipped = zip(items,img_df)
    return render_template("items_list.html",item_zipped=item_zipped)
#register user
api.add_resource(Register, '/register')
#display items link
api.add_resource(Data, '/items')
#add order api link
api.add_resource(Iorder, '/orders')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)