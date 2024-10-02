from vehicle_type import VehicleType
from vehicle import Vehicle
from parking_spot import ParkingSpot


class Level:
    def __init__(self, floor: int, num_motorcycle_spots: int, num_car_spots: int, num_truck_spots: int):
        self.floor = floor

        motorcycle_spots = [ParkingSpot(i) for i in range(num_motorcycle_spots)]
        car_spots = [ParkingSpot(i) for i in range(num_car_spots)]
        truck_spots = [ParkingSpot(i) for i in range(num_truck_spots)]
        
        self.parking_spots = {
            VehicleType.MOTORCYCLE: motorcycle_spots,
            VehicleType.CAR: car_spots,
            VehicleType.TRUCK: truck_spots
        }

    def park(self, vehicle: Vehicle) -> bool:
        for parking_spot in self.parking_spots[vehicle.get_vehicle_type()]:
            if parking_spot.park(vehicle):
                return True
        return False
    
    def unpark(self, vehicle: Vehicle) -> bool:
        for parking_spot in self.parking_spots[vehicle.get_vehicle_type()]:
            if parking_spot.unpark(vehicle):
                return True
        return False
    
    def display_parking_state(self) -> None:
        print(f'Floor {self.floor}:')
        for vehicle_type in self.parking_spots:
            print(f'{vehicle_type}:')
            for parking_spot in self.parking_spots[vehicle_type]:
                parking_spot.display_parking_state()