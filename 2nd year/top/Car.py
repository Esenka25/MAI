class Car():
    def __init__(self, id: int, manufacturer: str, model: str, car_type: str, price: int):
        self.id = id

        self.manufacturer = manufacturer
        self.model = model
        self.car_type = car_type
        self.price = price 

    def representation_car(self):
        return {
            "id": self.id,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "car_type": self.car_type,
            "price": self.price,
        }


# inst1 = Car(
#     id=1,
#     manufacturer='manufacturer1',
#     model='model1',
#     car_type='car_type1',
#     price=100
# )

# print(inst1)
#
# print(inst1.representation_car())