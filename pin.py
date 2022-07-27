import getpass

num_attempts = 0
max_attempts = 3
password = "wow"

while num_attempts < max_attempts:
    supplied_pin = getpass.getpass("Enter your PIN: ")
    num_attempts += 1
    if supplied_pin == password:
        print("Authorised!")
        break
    else:
        print("Wrong PIN.")
        print("You have {} attempts left.".format(max_attempts-num_attempts))