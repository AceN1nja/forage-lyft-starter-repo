from car import Car

from engine.Capulet import Capulet
from engine.Sternman import Sternman
from engine.Willoughby import Willoughby

from battery.Spindler import Spindler
from battery.Nubbin import Nubbin


def create_calliope(last_service_date, current_mileage, last_service_mileage):
    car = Car
    car.battery = Spindler(last_service_date)
    car.engine = Capulet(current_mileage, last_service_mileage)
    return car


def create_glissade(last_service_date, current_mileage, last_service_mileage):
    car = Car
    car.battery = Spindler(last_service_date)
    car.engine = Willoughby(current_mileage, last_service_mileage)
    return car


def create_palindrome(last_service_date, warning_light):
    car = Car
    car.battery = Spindler(last_service_date)
    car.engine = Sternman(warning_light)
    return car


def create_rorschach(last_service_date, current_mileage, last_service_mileage):
    car = Car
    car.battery = Nubbin(last_service_date)
    car.engine = Willoughby(current_mileage, last_service_mileage)
    return car


def create_thovex(last_service_date, current_mileage, last_service_mileage):
    car = Car
    car.battery = Nubbin(last_service_date)
    car.engine = Capulet(current_mileage, last_service_mileage)
    return car
