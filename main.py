from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

products = {
    1: {"name": "Телевизор", "price": 15},
    2: {"name": "Кофемашина", "price": 10},
    3: {"name": "Ноутбук", "price": 11}
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("price", type=int)


class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return products
        else:
            return products[course_id]

    def delete(self, course_id):
        del products[course_id]
        return products

    def post(self, course_id):
        products[course_id] = parser.parse_args()
        return products

    def put(self, course_id):
        products[course_id] = parser.parse_args()
        return products


api.add_resource(Main, "/api/products/<int:course_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
