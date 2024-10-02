from vehicle import Vehicle


class ParkingSpot:
    def __init__(self, spot_number: int):
        self.spot_number = spot_number
        self.vehicle = None
    
    def park(self, vehicle: Vehicle) -> bool:
        if self.vehicle is None:
            self.vehicle = vehicle
            return True
        return False
    
    def unpark(self, vehicle: Vehicle) -> bool:
        if self.vehicle == vehicle:
            self.vehicle = None
            return True
        return False
    
    def display_parking_state(self):
        print(f'Spot Number {self.spot_number}: {"Occupied" if self.vehicle else "Available"}')