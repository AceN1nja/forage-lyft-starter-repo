from tires.Tires import Tires


class Cariggan(Tires):
    def __init__(self, tire_set):
        self.tire_set = tire_set

    def needs_service(self):
        for tire in self.tire_set:
            if tire > 0.9:
                return True

        return False
