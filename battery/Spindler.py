from battery.Battery import Battery
from datetime import datetime


class Spindler(Battery):

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self, current_date=datetime.today()):
        return current_date.year - self.last_service_date.year > 2
