class Car:
  total_car = 0

  def __init__(self, brand, model):
    self.__brand = brand
    self.__model = model
    Car.total_car += 1

  def get_brand(self):
    return self.__brand + " !"
  
  def fullname(self):
    return f"{self.__brand} {self.__model}"

  def fuel_type(self):
    return "Petrol or Diesel"

  @staticmethod
  def general_description(): # don't use self when static method used
    return "Cars are means of transport"
  @property
  def model(self):
    return self.__model 


class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
safariTwo = Car("Tata","Nexon")
# print(safari.fuel_type())
# safari.model = "city"
# print(safari.model)

# print(safari.model)

# print(safari.general_description())
# print(Car.general_description())

# print(Car.total_car)

# print(my_tesla.__brand)
# print(my_tesla.fullname())

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())

# my_new_car = Car("TATA", "Safari")
# print(my_new_car.brand)

class Battery:
  def battery_info(slef):
    return "This is battery"


class Engine:
  def engine_info(self):
    return "This is engine"


class ElectricCar2(Battery, Engine, Car):
  pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

