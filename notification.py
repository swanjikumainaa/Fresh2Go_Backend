class Notification:
    def __init__(self, message):
        self.message = message

    def send_notification(self, recipient):
        pass  # This is just a placeholder, will be implemented in subclasses


class Customer:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def notify_order(self, grocer, product, quantity):
        message = f"Thank you for your order of {quantity} {product}! We will inform you when the product is delivered."
        notification = OrderNotification(message)
        grocer.receive_notification(notification)


    def notify_delivery(self, grocer, product):
        message = f"The {product} that you ordered has been delivered and received. Thank you for your purchase!"
        notification = DeliveryNotification(message)
        grocer.receive_notification(notification)


class Grocer:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def receive_notification(self, notification):
        # Here is where we can define how to send the notification (e.g. email, SMS, app notification, etc.)
        print("Received notification: ", notification.message)


class OrderNotification(Notification):
    def send_notification(self, recipient):
        print(f"Sending order notification to {recipient.email} and {recipient.phone_number}: {self.message}")


class DeliveryNotification(Notification):
    def send_notification(self, recipient):
        print(f"Sending delivery notification to {recipient.email} and {recipient.phone_number}: {self.message}")



        # create customer and grocer objects
customer = Customer("John Doe", "+123456789", "johndoe@example.com")
grocer = Grocer("Jane Smith", "+987654321", "janesmith@example.com")

# send order and delivery notifications
customer.notify_order(grocer, "Apples", 5)
grocer.receive_notification(OrderNotification("New order received!"))
customer.notify_delivery(grocer, "Apples")
grocer.receive_notification(DeliveryNotification("Delivery complete!"))