import random
import string

class User:
    def __init__(self, name, username, email, phone_number=None, bank_details=None):
        self.name = name
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.bank_details = bank_details
        
    def __str__(self):
        return f"Name: {self.name}\nUsername: {self.username}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nBank Details: {self.bank_details}"

class UserDatabase:
    def __init__(self):
        self.users = {}
        
    def add_user(self, name, username, email, phone_number=None, bank_details=None):
        user_id = random.randint(10000, 99999)
        user = User(name, username, email, phone_number, bank_details)
        self.users[user_id] = user
        return user_id
    
    def get_user(self, user_id):
        if user_id in self.users:
            return self.users[user_id]
        else:
            return None

# Use case
db = UserDatabase()
user_id = db.add_user("Susan", "maina", "susan@gmail.com", "0768390908", "0899876545664566")
user = db.get_user(user_id)
print(user)
