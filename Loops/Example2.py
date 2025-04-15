password = 0
while password != 1234:
    try:
        password = int(input("Enter the password:- "))
        
    except ValueError:
        print("The password is in the numeric format, Enter numeric password only.")
        
print("Accessed granted.")