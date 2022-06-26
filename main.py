from time import sleep
import random

def Code(x):
    if x == "*966#":
        print("loading......")
        sleep(2.5)
        secondPage()
    else:
        print("loading......")
        sleep(2.5)
        print("ussd code not recognised.")

def secondPage():
    print("**************************************************")
    print("Welcome to StarLink bank Plc eazy money.\n"
          "Enter a number according to the service you want.")
    print("1. Open Account.\n"
          "2. Register.\n"
          "3. Transfers.\n"
          "4. Airtime.\n"
          "5. Data.\n"
          "6. Check Balance.")
    response()

def response():
    res = int(input(">: "))
    if res == 1:
        return openAccount()
    elif res == 2:
        return register()
    elif res == 3:
        return transfers()
    elif res == 4:
        return airtime()
    elif res == 5:
        return data()
    else:
        return checkBalance()


def openAccount():
    print("***************************************************************")
    print("Kindly fill in the form down below to create an account with us.")
    while True:
        try:
            firstname = str(input("enter your firstname: "))
            print("Name accepted.")
            break
        except ValueError:
            print("invalid response")

    while True:
        try:
            middlename = str(input("enter your middlename: "))
            if middlename == "":
                pass
            else:
                print("Name accepted")
                break
            break
        except ValueError:
            print("invalid response")

    while True:
        try:
            lastname = str(input("enter your lastname: "))
            print("Name accepted")
            break
        except ValueError:
            print("invalid response")

    while True:
        try:
            dob = int(input("enter your date of birth(in order of dd/mm/yyyy): "))
            print("Accepted value")
            break
        except ValueError:
            print("Invalid response")

    while True:
        try:
            currentAddress = str(input("enter your current residency location: "))
            print("Accepted value")
            break
        except ValueError:
            print("Invalid response")

    while True:
        try:
            nin = input("enter your NIN: ")
            if len(nin) == 11:
                print("Accepted value")
                break
            else:
                print("Incomplete, check again.")
        except ValueError:
            print("Invalid response")

    while True:
        try:
            bvn = input("enter your BVN: ")
            if len(bvn) == 11:
                print("Accepted value")
                break
            else:
                print("Incomplete, check again.")
        except ValueError:
            print("Invalid response")

    while True:
        try:
            phoneNumber = input("enter a working Phone NUmber: ")
            if len(phoneNumber) == 11:
                print("Accepted value")
                break
            else:
                print("Incomplete, check again.")
        except ValueError:
            print("Invalid response")

    accountNumber = random.getrandbits(33)

    print("*********************************************************")
    print("Thank you for providing the following details.\n"
          "Kindly wait while your account number is being generated.")
    print("processing......")
    sleep(3.0)
    print("Congratulations! Account successfully created!")

    newUser = {
        "firstname": firstname.capitalize(),
        "middlename": middlename.capitalize(),
        "lastname": lastname.capitalize(),
        "date of birth": dob,
        "currentAddress": currentAddress,
        "nin": nin,
        "bvn": bvn,
        "phonenumber": phoneNumber,
    }

    def accountDetails():
        print("Account name: ", newUser.get("firstname"), newUser.get("middlename"), newUser.get("lastname"))
        print("Account number: ", accountNumber)

    print("********************************************************")
    accountDetails()
    print("Thank you for banking with us.")
    print("********************************************************")


def register():
    print("********************************************************")
    while True:
        decide = input("Would you like to register for a debit card? y/n: ")
        if decide == "y":
            print("processing............")
            sleep(2.5)
            print("********************************************************")
            print("You have successfully registered for a debit card.\n"
                  "Visit our nearby branch to collect your card.")
            print("********************************************************")
            break
        else:
            print("Thank you for visiting!")


def transfers():

    banklist = {

        "1": "Union Bank",
        "2": "Zenith Bank",
        "3": "UBA",
        "4": "Access/Diamond Bank",
        "5": "Sterling Bank",
        "6": "Ecobank Bank",

    }

    print("**************************************************")
    while True:
        try:
            acct = str(input("Enter account number: "))
            if len(acct) == 10:
                pass
                break
            else:
                print("check account number")
        except ValueError:
            print("invalid response")

    for i, j in banklist.items():
        print(f"{i}. {j}")

    bank = int(input("Select bank: "))

    while True:
        try:
            amount = str(input("Enter amount: "))
            if len(amount) > 1:
                pass
                break
            else:
                print("invalid amount")
        except ValueError:
            print("invalid response")

    while True:
        try:
            pinn = str(input("Enter pin: "))
            if len(pinn) == 4:
                print("Valid pin.")
                break
            else:
                print("invalid pin")
        except ValueError:
            print("invalid response")
    print("processing............")
    sleep(2.5)
    print("***************************************************************")
    print(f"{amount} has been successfully transferred to {acct}, {bank}")
    print("Thank you for banking with us.")
    print("***************************************************************")


def airtime():

    network = {
        "1": "Glo",
        "2": "MTN",
        "3": "Airtel",
        "4": "9mobile"
    }

    print("**************************************************")
    while True:
        try:
            phonenumber = str(input("Enter phone number: "))
            if len(phonenumber) == 11:
                pass
                break
            else:
                print("check phone number.")
        except ValueError:
            print("invalid response")

    while True:
        try:
            amount2 = str(input("Enter amount: "))
            if len(amount2) > 2:
                pass
                break
            else:
                print("check amount number.")
        except ValueError:
            print("invalid response")

    while True:
        try:
            pin2 = str(input("Enter pin: "))
            if len(pin2) == 4:
                pass
                break
            else:
                print("check pin.")
        except ValueError:
            print("invalid response")
    print("processing............")
    sleep(2.5)
    print("***************************************************************")
    print(f"{amount2} has been successfully credited to {phonenumber}")
    print("Thank you for banking with us.")
    print("***************************************************************")


def data():

    plans = {
        "1": "4.5(9)GB",
        "2": "6(12)GB",
        "3": "10(20)GB",
        "4": "12(24)GB",
        "5": "20(40)GB",
        "6": "40(80)GB",
        "7": "75(150)GB",
    }

    network2 = {
        "1": "Glo",
        "2": "MTN",
        "3": "Airtel",
        "4": "9mobile"
    }

    print("**************************************************")
    while True:
        try:
            phonenumber2 = str(input("Enter phone number: "))
            if len(phonenumber2) == 11:
                pass
                break
            else:
                print("check phone number.")
        except ValueError:
            print("invalid response")

    for key, value in network2.items():
        print(f"{key}. {value}")

    net = input("select network: ")

    for key, value in plans.items():
        print(f"{key}. {value}")
    plan = str(input("select plan: "))

    while True:
        try:
            pin2 = str(input("Enter pin: "))
            if len(pin2) == 4:
                pass
                break
            else:
                print("check pin.")
        except ValueError:
            print("invalid response")
    print("processing............")
    sleep(2.5)
    print("***************************************************************")
    print(f"{phonenumber2} has been successfully credited with {plans.get(plan)}.")
    print("Thank you for banking with us.")
    print("***************************************************************")


def checkBalance():
    accountBalance = "N1,000,000,000.00"
    print("***************************************************************")
    while True:
        try:
            pin3 = str(input("Enter pin: "))
            if len(pin3) == 4:
                pass
                break
            else:
                print("check pin.")
        except ValueError:
            print("invalid response")
    print("processing............")
    sleep(2.5)
    print(f"Your account balance is: {accountBalance}")
    print("Thank you for banking with us.")
    print("*******************************************")

pin = input(">: ")
Code(pin)
