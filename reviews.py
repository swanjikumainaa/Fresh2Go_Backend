import datetime
class Review:
    def __init__(self,customer_name,message,number_of_stars):
        self.customer_name=customer_name
        self.message=message
        self.date=datetime.datetime.now()
        self.number_of_stars=number_of_stars
        self.reply=None

    def __str__(self):
        return f"{self.customer_name} rated {self.number_of_stars}/5 and commented: {self.message} \n" \
                f"Grocer replied: {self.reply}\n"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.reviews = []

    def add_review(self, customer_name, number_of_stars, message):
        review = Review(customer_name, number_of_stars, message)
        self.reviews.append(review)

    def view_reviews(self):
        for review in self.reviews:
            print(review)

    def reply_to_review(self, customer_name, reply):
        for review in self.reviews:
            if review.customer_name == customer_name:
                review.reply = reply
                break


prod1 = Product("Apples", 1.49)
prod2 = Product("Bananas", 0.99)

prod1.add_review("John", 5, "These apples were so fresh!")
prod1.add_review("Mary", 3, "Some of the apples were bruised")
prod2.add_review("Bob", 4, "Great taste but a little too ripe")
prod2.add_review("Sally", 2, "The bananas were overpriced")

prod1.reply_to_review("John", "Thank you for the feedback, we're glad you enjoyed our apples!")
prod1.view_reviews()
prod2.view_reviews()