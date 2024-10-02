from __future__ import annotations
from typing import List
from level import Level
from vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is None:
            ParkingLot._instance = self
            self.levels: List[Level] = []
        else:
            raise Exception('This class is a singleton!')
        
    @staticmethod
    def get_instance() -> ParkingLot:
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    
    def add_level(self, level: Level) -> None:
        self.levels.append(level)

    def park(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False
    
    def unpark(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unpark(vehicle):
                return True
        return False
    
    def display_parking_state(self) -> None:
        for level in self.levels:
            level.display_parking_state()
