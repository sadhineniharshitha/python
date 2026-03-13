name=input("enter yout name: ")
username=input("enter your username: ")
bal=int(input("enter your bal: "))
password=input("enter your password: ")
cpassword=input("confirm your password: ")
if password==cpassword:
    print("Successfully registered")
else:
    print("Please enter correct password ,password doesnt match ")
    exit()
vusername=input("enter your username: ")
vpassword=input("enter your password: ")
if vusername==username and vpassword==password:
    while True:
        print("1.withdrawl")
        print("2.Deposit ")
        print("3.Balance enquiry")
        print("4.Logout")

        option=int(input("Enter YOur Choice: "))
        if option==1:
            amount=int(input("enter the withdrawl amount: "))
            if bal>amount and amount>0:
                bal=bal-amount
                print("Withdrawl successfully")
        elif option==2:
            amount=int(input("enter your deposit amount: "))
            if amount>0:
                bal=bal+amount
                print("Deposit Successfully")
        elif option==3:
            print("Your balance amount is",bal)
        elif option==4:
            print("Logout Successfully")
            break
        else:
            print("Invalid Choice")
else:
    print("Invalid credentials")