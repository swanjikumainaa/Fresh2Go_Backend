# define a function to generate a random password
def generate_password(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# define a function to send password recovery email
def send_recovery_email(email):
    # code to send email with password recovery link or temporary password

# define a function to check password recovery 
 def check_recovery_request(email):
    # check if email exists in the database
    if email in UserDatabase:
        # generate a new temporary password
        temp_password = generate_password(8)
        # update user's password in the database
        UserDatabase[email]['password'] = temp_password
        # send password recovery email with the temporary password
        send_recovery_email(email)
        return "Password recovery email sent"
    else:
        return "Email not found in database"

# use
email = input("Enter your email address: ")
print(check_recovery_request(email))
