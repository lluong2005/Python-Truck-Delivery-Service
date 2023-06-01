from utils import TimeInSeconds


# Class for trucks
class Truck:
    def __init__(self, distMatrix, timeMatrix, startTime=28800):
        self.packages = []
        self.milesTravelled = 0
        self.internalClock = startTime
        self.location = 0
        self.distMatrix = distMatrix
        self.timeMatrix = timeMatrix

    # Loads packages
    def loadPackages(self, packages):
        self.packages = packages

    # Nearest neighbor algorithm is implemented
    def travelRoute(self):
        for package in self.packages:
            package.pickupTime = self.internalClock
            print(
                # f"Package {package.id} was picked up from hub at {TimeInSeconds.fromInt(package.pickupTime)}"
            )
        while len(self.packages) != 0:
            # find nearest delivery location
            # (location-id, distance)
            nearestDelivery = (-1, float("inf"))
            for package in self.packages:
                comparison = self.timeMatrix[self.location, package.deliveryId]
                if comparison < nearestDelivery[1]:
                    nearestDelivery = (package.deliveryId, comparison)

                # travel to delivery location
            self.goToLocation(nearestDelivery[0])

            # deliver packages at location
            for package in self.packages:
                if package.deliveryId == nearestDelivery[0]:
                    package.deliveryTime = self.internalClock
                    self.packages.remove(package)
                    print(
                        # f"package {package.id} was delivered to {package.address}, {package.city}, {package.state} at {TimeInSeconds.fromInt(package.deliveryTime)}"
                    )
        self.goToLocation(0)

    def goToLocation(self, locationId):
        self.milesTravelled += self.distMatrix[self.location, locationId]
        self.internalClock += self.timeMatrix[self.location, locationId]
        self.location = locationId
