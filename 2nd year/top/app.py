from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from DB import DB
from Car import Car

app = Flask(__name__)

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "KURSACH"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

db = DB()

# https://127.0.0.1:8000/cars
# type_connection://ip:port/route?params=

# <type_connection://ip:port/cars> [GET- READ, POST - CREATE, PUT - UPDATE, DELETE - DELETE]
@app.route("/cars", methods=['GET', 'POST'])
def cars():
    if request.method == 'GET':
        return db.read_all()

    if request.method == 'POST':
        car = Car(
            id=request.json['id'],
            manufacturer=request.json['manufacturer'],
            model=request.json['model'],
            car_type=request.json['car_type'],
            price=request.json['price']
        )

        output = db.create(car=car)
        print(db.read_all())
        return str(output)

@app.route("/car/<id>", methods=['GET', 'PUT', 'DELETE'])
def car(id):
    if request.method == 'GET':
        car = db.read(car_id=id)
        if car is not False:
            return car.representation_car()
        return 'Not found car for this id'

    if request.method == 'PUT':
        car = db.read(car_id=id)
        if car is not None:
            car.id = request.json['id'] if request.json.get('id') is not None else car.id
            car.manufacturer = request.json['manufacturer'] if request.json.get('manufacturer') is not None else car.manufacturer
            car.model = request.json['model'] if request.json.get('model') is not None else car.model
            car.car_type = request.json['car_type'] if request.json.get('car_type') is not None else car.car_type
            car.price = request.json['price'] if request.json.get('price') is not None else car.price

            return 'True'
        else:
            return 'Not found car for this id'

    if request.method == 'DELETE':
        output = db.delete(car_id=id)
        if output:
            return str(True)
        else:
            return 'Not found car for this id'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port = 5005)
