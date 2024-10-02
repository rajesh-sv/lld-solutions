from parking_lot import ParkingLot
from level import Level
from car import Car
from motorcycle import Motorcycle
from truck import Truck


class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 2, 2, 1))
        parking_lot.add_level(Level(2, 2, 2, 1))

        motorcycle1 = Motorcycle("M1")
        motorcycle2 = Motorcycle("M2")
        motorcycle3 = Motorcycle("M3")
        car1 = Car("C1")
        car2 = Car("C2")
        car3 = Car("C3")
        car4 = Car("C4")
        truck1 = Truck("T1")
        truck2 = Truck("T2")

        # Park vehicles
        parking_lot.park(motorcycle1)
        parking_lot.park(motorcycle2)
        parking_lot.park(motorcycle3)
        parking_lot.park(car1)
        parking_lot.park(car2)
        parking_lot.park(car3)
        parking_lot.park(car4)
        parking_lot.park(truck1)
        parking_lot.park(truck2)

        # Display parking state
        parking_lot.display_parking_state()

        # Unpark vehicles
        parking_lot.unpark(motorcycle1)
        parking_lot.unpark(car3)
        parking_lot.unpark(truck2)

        # Display updated parking state
        parking_lot.display_parking_state()

if __name__ == "__main__":
    ParkingLotDemo.run()