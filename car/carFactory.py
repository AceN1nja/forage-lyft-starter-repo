from car.Car import Car

from engine.Capulet import Capulet
from engine.Sternman import Sternman
from engine.Willoughby import Willoughby

from battery.Spindler import Spindler
from battery.Nubbin import Nubbin


def create_calliope(last_service_date, current_mileage, last_service_mileage):
    battery = Spindler(last_service_date)
    engine = Capulet(current_mileage, last_service_mileage)
    return Car(battery, engine)


def create_glissade(last_service_date, current_mileage, last_service_mileage):
    battery = Spindler(last_service_date)
    engine = Willoughby(current_mileage, last_service_mileage)
    return Car(battery, engine)


def create_palindrome(last_service_date, warning_light):
    battery = Spindler(last_service_date)
    engine = Sternman(warning_light)
    return Car(battery, engine)


def create_rorschach(last_service_date, current_mileage, last_service_mileage):
    battery = Nubbin(last_service_date)
    engine = Willoughby(current_mileage, last_service_mileage)
    return Car(battery, engine)


def create_thovex(last_service_date, current_mileage, last_service_mileage):
    battery = Nubbin(last_service_date)
    engine = Capulet(current_mileage, last_service_mileage)
    return Car(battery, engine)
