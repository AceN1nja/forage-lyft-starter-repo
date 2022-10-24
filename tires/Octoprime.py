from tires.Tires import Tires


class Octoprime(Tires):
    def __init__(self, tire_set):
        self.tire_set = tire_set

    def needs_service(self):
        return sum(self.tire_set) > 3
