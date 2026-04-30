from car import Car
from truck import Truck
from motorcycle import Motorcycle

def save_fleet_to_file(vehicles, filename):
    with open(filename, "w") as file:
        for vehicle in vehicles:
            if isinstance(vehicle, Car):
                file.write(f"Car, {vehicle.vid}, {vehicle.model}, {vehicle.year}, {vehicle.fuel_type}, {vehicle.doors}\n")
            elif isinstance(vehicle, Truck):
                file.write(f"Truck, {vehicle.vid}, {vehicle.model}, {vehicle.year}, {vehicle.max_load}, {vehicle.axles}\n")
            elif isinstance(vehicle, Motorcycle):
                file.write(f"Motorcycle, {vehicle.vid}, {vehicle.model}, {vehicle.year}, {vehicle.engine_cc}, {vehicle.type}\n")


def load_fleet_from_file(filename):
    vehicles = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(", ")

            if parts[0] == "Car":
                vehicles.append(Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))

            elif parts[0] == "Truck":
                vehicles.append(Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5])))

            elif parts[0] == "Motorcycle":
                vehicles.append(Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5]))

    return vehicles