class OrderTracker:
    def __init__(self):
        self.orders = []
    def add_order(self, order):
        self.orders.append(order)
    def remove_order(self, order):
        self.orders.remove(order)
    def get_orders(self):
        return self.orders
    def track_order(self, order):
        print("User:", order.get_user())
        print("Time Ordered:", order.get_time_ordered())
        print("Delivery Time:", order.get_expected_delivery_time())
        print("Delivery Location:", order.get_expected_delivery_location())
        print("Order Status:", order.get_status())