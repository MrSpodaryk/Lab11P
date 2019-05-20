from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from enums.type_of_menu import TypeOfMenu
from enums.temperature import Temperature
from enums.level_of_spicy import LevelOfSpicy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_menu = db.Column(db.String(80), unique=False)
    currency = db.Column(db.String(120), unique=False)
    price = db.Column(db.Integer, unique=False)
    name = db.Column(db.String(120), unique=False)
    temperature = db.Column(db.String(120), unique=False)
    weigh = db.Column(db.Integer, unique=False)
    level_of_spicy = db.Column(db.String(120), unique=False)

    def __init__(self, type_of_menu=TypeOfMenu.STANDARD_MENU, currency="", price=0, name="",
                 temperature=Temperature.NORMAL, weigh=0, level_of_spicy=LevelOfSpicy.NORMAL):
        self.type_of_menu = type_of_menu
        self.currency = currency
        self.price = price
        self.name = name
        self.temperature = temperature
        self.weigh = weigh
        self.level_of_spicy = level_of_spicy


class DishSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('type_of_menu', 'currency', 'price', 'name', 'temperature', 'weigh', 'level_of_spicy')


dish_schema = DishSchema()
dishes_schema = DishSchema(many=True)


# endpoint to create new user
@app.route("/dish", methods=["POST"])
def add_dish():
    type_of_menu = request.json['type_of_menu']
    currency = request.json['currency']
    price = request.json['price']
    name = request.json['name']
    temperature = request.json['temperature']
    weigh = request.json['weigh']
    level_of_spicy = request.json['level_of_spicy']

    new_dish = Dish(type_of_menu, currency, price, name, temperature, weigh, level_of_spicy)

    db.session.add(new_dish)
    db.session.commit()

    return jsonify(request.json)


# endpoint to show all users
@app.route("/dish", methods=["GET"])
def get_dish():
    all_dishes = Dish.query.all()
    result = dishes_schema.dump(all_dishes)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/dish/<id>", methods=["GET"])
def dish_detail(id):
    dish = Dish.query.get(id)
    return dish_schema.jsonify(dish)


# endpoint to update user
@app.route("/dish/<id>", methods=["PUT"])
def dish_update(id):
    dish = Dish.query.get(id)
    dish.type_of_menu = request.json['type_of_menu']
    dish.currency = request.json['currency']
    dish.price = request.json['price']
    dish.name = request.json['name']
    dish.temperature = request.json['temperature']
    dish.weigh = request.json['weigh']
    dish.level_of_spicy = request.json['level_of_spicy']

    db.session.commit()
    return dish_schema.jsonify(dish)


# endpoint to delete user
@app.route("/dish/<id>", methods=["DELETE"])
def user_delete(id):
    dish = Dish.query.get(id)
    db.session.delete(dish)
    db.session.commit()

    return dish_schema.jsonify(dish)


if __name__ == '__main__':
    app.run(debug=True)
