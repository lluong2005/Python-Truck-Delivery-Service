# Lea Luong
# 010464466

from difference_matrix import DiffMatrix
from package import Package
from datetime import datetime
from hash_table import HashTable
from truck import Truck
import copy
import csv
from utils import TimeInSeconds

# reads package file

with open("data/packages.csv") as csvfile:
    CSV_package = csv.reader(csvfile)
    CSV_package = list(CSV_package)


# Set known constants such as truck speed and which packages go on which trucks
TRUCK_SPEED_MPH = 18
PACKAGE_PRIORITIES = [
    [
        1,
        13,
        14,
        15,
        16,
        20,
        29,
        30,
        31,
        34,
        37,
        40,
        19,
    ],  # *First truck. Truck then pulls from 3
    [
        25,
        28,
        32,
        36,
        38,
        18,
        6,
        3,
    ],  # *Second truck. Truck then pulls from 3. Departs at 9:10
    [
        2,
        4,
        5,
        7,
        8,
        10,
        11,
        12,
        17,
        21,
        22,
        23,
        24,
        26,
        27,
        33,
        35,
        39,
    ],  # *Anything left over after trucks 1 & 2 full goes on 3rd truck
    [9],  # * Reserved for last truck
]

# Create difference matrices
DISTANCE_MATRIX = DiffMatrix()
DISTANCE_MATRIX.createFromCsv("data/distMatrix.csv")
TIME_MATRIX = copy.deepcopy(DISTANCE_MATRIX)
for i in range(TIME_MATRIX.size):
    for j in range(TIME_MATRIX.size):
        TIME_MATRIX[i, j] *= 200
with open("data/distMatrix.csv") as file:
    LOCATION_IDS = [line.split(",")[0].strip('" ') for line in file]

# Creates hash table
PACKAGE_HASH_TABLE = HashTable()
with open("data/packages.csv") as package_info:
    package_data = csv.reader(package_info)
    next(package_data)  # Skip the header row
    for row in package_data:
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        deadline = row[5]
        weight = float(row[6])

        # Create a new Package object
        package = Package(package_id, address, city, state, zipcode, deadline, weight)
        package.deliveryId = LOCATION_IDS.index(
            f"{package.address} ({package.zipcode})"
        )

        # Insert the package into the hash table
        PACKAGE_HASH_TABLE.insert(package_id, package)

# Create trucks, load packages onto them, and send them off
TRUCK_1 = Truck(DISTANCE_MATRIX, TIME_MATRIX)
truck1Packages = []
for i in PACKAGE_PRIORITIES[0]:
    truck1Packages.append(PACKAGE_HASH_TABLE.lookup(i))
for i in PACKAGE_PRIORITIES[2][:3]:
    truck1Packages.append(PACKAGE_HASH_TABLE.lookup(i))
    PACKAGE_PRIORITIES[2].remove(i)
TRUCK_1.loadPackages(truck1Packages)
TRUCK_1.travelRoute()
TRUCK_2 = Truck(DISTANCE_MATRIX, TIME_MATRIX, 33000)
truck2Packages = []
for i in PACKAGE_PRIORITIES[1]:
    truck2Packages.append(PACKAGE_HASH_TABLE.lookup(i))
for i in PACKAGE_PRIORITIES[2][:8]:
    truck2Packages.append(PACKAGE_HASH_TABLE.lookup(i))
    PACKAGE_PRIORITIES[2].remove(i)
TRUCK_2.loadPackages(truck2Packages)
TRUCK_2.travelRoute()
TRUCK_3 = Truck(DISTANCE_MATRIX, TIME_MATRIX, TRUCK_2.internalClock)
truck3Packages = []
for i in PACKAGE_PRIORITIES[2]:
    truck3Packages.append(PACKAGE_HASH_TABLE.lookup(i))
truck3Packages.append(PACKAGE_HASH_TABLE.lookup(PACKAGE_PRIORITIES[3][0]))
TRUCK_3.loadPackages(truck3Packages)
TRUCK_3.travelRoute()

# for package in PACKAGES:
#     print(f"package: {package.id} was delivered to {package.address}, {package.city}, {package.state} at {package.deliveryTime} and was picked up from the hub at {package.pickupTime}")


def parse_time_string(time_string):
    try:
        return datetime.strptime(time_string, "%I:%M %p")
    except ValueError:
        return None


if __name__ == "__main__":
    while True:
        print("Welcome to the WGUPS Delivery Simulation")
        # Ask for user input
        user_input = input("Enter the time (HH:MM AM/PM): ")

        if user_input.lower() == "quit":
            break

        # Parse the user input time
        current_time = parse_time_string(user_input)

        if current_time is None:
            print("Invalid time format. Please try again.")
            continue

        # Convert current_time to seconds
        current_time_seconds = current_time.hour * 3600 + current_time.minute * 60

        # Ask for user input to choose the operation
        operation = input(
            "Choose an operation:\n1. Lookup package tracking info\n2. View all packages tracking info\n3. View total mileage\n"
        )

        if operation == "1":
            # Lookup a single package tracking info
            package_id = input("Enter the package ID: ")
            package = PACKAGE_HASH_TABLE.lookup(int(package_id))

            if package is not None:
                print("Package ID:", package_id)
                print("Address:", package.address)
                print("City:", package.city)
                print("State:", package.state)
                print("Zip code:", package.zipcode)
                print("Deadline:", package.deadline)
                print("Weight:", package.weight)
                print(
                    "Status:",
                    package.getStatusAtTime(current_time_seconds),
                    Truck.convert_seconds_to_time(package.deliveryTime),
                )

            else:
                print("Package not found.")

        elif operation == "2":
            # View all packages tracking info
            for package_id in range(1, 41):
                package = PACKAGE_HASH_TABLE.lookup(package_id)
                print("Package ID:", package_id)
                print("Address:", package.address)
                print("City:", package.city)
                print("State:", package.state)
                print("Zip code:", package.zipcode)
                print("Deadline:", package.deadline)
                print("Weight:", package.weight)
                if package.getStatusAtTime(current_time_seconds) == "Delivered":
                    print(
                        "Status:",
                        package.getStatusAtTime(current_time_seconds),
                        "to",
                        f"{package.address},",
                        f"{package.city},",
                        f"{package.state},",
                        "at",
                        TimeInSeconds.fromInt(package.deliveryTime),
                    )
                else:
                    print("Status:", package.getStatusAtTime(current_time_seconds))
                print("")

        elif operation == "3":
            # View total mileage
            total_mileage = (
                TRUCK_1.milesTravelled + TRUCK_2.milesTravelled + TRUCK_3.milesTravelled
            )
            print("Total mileage:", total_mileage, "miles")

        else:
            print("Invalid operation. Please try again.")
