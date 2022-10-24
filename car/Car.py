class Car:
    def __init__(self, engine, battery, tire_set):
        self.battery = battery
        self.engine = engine
        self.tires_set = tire_set

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tires_set.needs_service()

    def change_battery(self, battery):
        self.battery = battery
