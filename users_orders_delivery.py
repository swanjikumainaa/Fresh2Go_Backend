class Order:
    def __init__(self, user, time_ordered, expected_delivery_time, expected_delivery_location):
        self.user = user
        self.time_ordered = time_ordered
        self.expected_delivery_time = expected_delivery_time
        self.expected_delivery_location = expected_delivery_location
        self.status = "In Progress"
    def set_status(self, new_status):
        self.status = new_status
    def get_user(self):
        return self.user
    def get_time_ordered(self):
        return self.time_ordered
    def get_expected_delivery_time(self):
        return self.expected_delivery_time
    def get_expected_delivery_location(self):
        return self.expected_delivery_location
    def get_status(self):
        return self.status
    