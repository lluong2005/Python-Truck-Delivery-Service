from datetime import datetime


def parse_time_string(time_string):
    if isinstance(time_string, int):
        return time_string

    try:
        time = datetime.strptime(time_string, "%I:%M %p")
        minutes = time.hour * 60 + time.minute
        return minutes
    except ValueError:
        return None


class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
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
        self.status = status

    def getStatusAtTime(self, current_time):
        if self.deliveryTime is None:
            self.status = "At the hub"
        elif current_time < self.pickupTime:
            self.status = "At the hub"
        elif self.pickupTime <= current_time < self.deliveryTime:
            self.status = "En route"
        else:
            self.status = "Delivered"
