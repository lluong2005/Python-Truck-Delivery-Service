class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.deliveryId = -1
        self.pickupTime = -1
        self.deliveryTime = -1

    def getStatusAtTime(self, current_time):
        if self.deliveryTime is -1:
            return "At the hub"
        elif current_time < self.pickupTime:
            return "At the hub"
        elif self.pickupTime <= current_time < self.deliveryTime:
            return "En route"
        else:
            return "Delivered"
