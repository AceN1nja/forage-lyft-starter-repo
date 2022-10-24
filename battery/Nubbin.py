from battery import Battery
from abc import ABC
from datetime import datetime


class Nubbin(Battery, ABC):

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self, current_date=datetime.now()):
        return self.last_service_date.year - current_date.year > 4
