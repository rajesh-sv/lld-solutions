from vehicle_type import VehicleType
from abc import ABC


class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
    
    def get_license_plate(self) -> str:
        return self.license_plate
    
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
