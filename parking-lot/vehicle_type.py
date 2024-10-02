from enum import Enum


class VehicleType(Enum):
    MOTORCYCLE = 'Motorcycle'
    CAR = 'Car'
    TRUCK = 'Truck'

    def __str__(self) -> str:
        return str(self.value)