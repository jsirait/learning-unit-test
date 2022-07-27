var = input("Please enter an integer: ")

if not var.isdecimal():
    print("Sorry, your input is not an integer. Please try again!")
else:
    for ii in range(int(var), 0, -2):
        print(ii)
        if ii==1:
            break