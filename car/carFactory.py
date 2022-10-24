from car.Car import Car

from engine.Capulet import Capulet
from engine.Sternman import Sternman
from engine.Willoughby import Willoughby

from battery.Spindler import Spindler
from battery.Nubbin import Nubbin

from tires.Cariggan import Cariggan
from tires.Octoprime import Octoprime

def create_calliope(last_service_date, current_mileage, last_service_mileage, tire_set):
    battery = Spindler(last_service_date)
    engine = Capulet(current_mileage, last_service_mileage)
    tires = Cariggan(tire_set)
    return Car(battery, engine, tires)


def create_glissade(last_service_date, current_mileage, last_service_mileage, tire_set):
    battery = Spindler(last_service_date)
    engine = Willoughby(current_mileage, last_service_mileage)
    tires = Cariggan(tire_set)
    return Car(battery, engine, tires)


def create_palindrome(last_service_date, warning_light, tire_set):
    battery = Spindler(last_service_date)
    engine = Sternman(warning_light)
    tires = Octoprime(tire_set)
    return Car(battery, engine, tires)


def create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_set):
    battery = Nubbin(last_service_date)
    engine = Willoughby(current_mileage, last_service_mileage)
    tires = Octoprime(tire_set)
    return Car(battery, engine, tires)


def create_thovex(last_service_date, current_mileage, last_service_mileage, tire_set):
    battery = Nubbin(last_service_date)
    engine = Capulet(current_mileage, last_service_mileage)
    tires = Cariggan(tire_set)
    return Car(battery, engine, tires)
