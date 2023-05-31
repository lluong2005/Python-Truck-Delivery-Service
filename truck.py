class Truck:
    def __init__(self, startTime=28800):
        self.packages = []
        self.milesTravelled = 0
        self.internalClock = startTime
        self.location = 0

    def loadPackages(self, packages):
        self.packages = packages

    def travelRoute(self, distMatrix, timeMatrix):
        for package in self.packages:
            package.pickupTime = self.internalClock
            print(
                f"Package {package.id} was picked up from hub at {Truck.convert_seconds_to_time(package.pickupTime)}"
            )
        while len(self.packages) != 0:
            # find nearest delivery location
            # (location-id, distance)
            nearestDelivery = (-1, float("inf"))
            for package in self.packages:
                comparison = timeMatrix[self.location, package.deliveryId]
                if comparison < nearestDelivery[1]:
                    nearestDelivery = (package.deliveryId, comparison)

                # travel to delivery location
            self.goToLocation(nearestDelivery[0], distMatrix, timeMatrix)

            # deliver packages at location
            for package in self.packages:
                if package.deliveryId == nearestDelivery[0]:
                    package.deliveryTime = int(self.internalClock)
                    self.packages.remove(package)
                    print(
                        f"package {package.id} was delivered to {package.address}, {package.city}, {package.state} at {Truck.convert_seconds_to_time(package.deliveryTime)}"
                    )
        self.goToLocation(0, distMatrix, timeMatrix)

    def goToLocation(self, locationId, distMatrix, timeMatrix):
        self.milesTravelled += distMatrix[self.location, locationId]
        self.internalClock += timeMatrix[self.location, locationId]
        self.location = locationId

    @staticmethod
    def convert_seconds_to_time(seconds):
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
