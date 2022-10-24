class Car:
    def __init__(self):
        self.battery = None
        self.engine = None

    def needs_service(self):
        if self.battery.needs_service() or self.engine.needs_service():
            return True
        else:
            return False

    def change_battery(self, battery):
        self.battery = battery
