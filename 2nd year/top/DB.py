from Car import Car
from typing import Optional

class DB:
    __instance = None
    carsDB = list()
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DB, cls).__new__(cls)
        return cls.instance

    def create(self, car: Car):
        self.carsDB.append(car)
        return True

    def read(self, car_id: int):
        for car in self.carsDB:
            if int(car.id) == int(car_id):
                return car
        return False


    def read_all(self):
        output = list()
        if len(self.carsDB) != 0:
            for car in self.carsDB:
                output.append(car.representation_car())
            return output

        return self.carsDB


    def update(self, car_id: int, manufacturer: Optional[str] = None, model: Optional[str] = None, car_type: Optional[str] = None, price: Optional[int] = None):
        for car in self.carsDB:
            if int(car.id) == int(car_id):
                car.manufacturer = manufacturer if manufacturer is not None else car.manufacturer
                car.model = model if model is not None else car.model
                car.car_type = car_type if car_type is not None else car.car_type
                car.price = price if price is not None else car.price

    def delete(self, car_id: int):
        for car in self.carsDB:
            if int(car.id) == int(car_id):
                self.carsDB.remove(car)
                return True
            else:
                return False



# database = DB()
#
# car1 = Car(
#     id=1,
#     manufacturer='manufacturer1',
#     model='model1',
#     car_type='car_type1',
#     price=100
# )
#
# car2 = Car(
#     id=2,
#     manufacturer='manufacturer2',
#     model='model2',
#     car_type='car_type2',
#     price=200
# )

# database.create(car=car1)
# database.create(car=car2)
# print(database.read_all())
# database.read(car_id = 1)
# database.update(car_id=1, manufacturer = 'UPDATED')
# database.delete(car_id=1)
