class Car:
    def __init__(self, engine, battery):
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()

    def change_battery(self, battery):
        self.battery = battery
