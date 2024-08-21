Account = {}

Balance = 0

def Display() :
    print("1.Login\n2.Create New Account\n3.Exit\n")

def l_display() :
    print("1.Deposit\n2.Money WithDrawl\n3.Check Balance\n4.Logout\n")

def l_info() :
    
    while True :
        l_display()
        l_choice=int(input("Enter Your Choice :"))
        if l_choice == 1 :
            deposit()
        elif l_choice == 2 :
            Withdrawl()
        elif l_choice == 3 :
            Check()
        elif l_choice ==4 :
            print("Logged out Successfully.\n")
            break
        else :
            print("Invalid Choice")

def deposit() :
    global Balance
    d_money=int(input("Enter Money to Deposit:"))
    Balance+=d_money
    print("Deposit Successful. Total Balance : ",Balance)
    
def Withdrawl() :
    global Balance
    w_money=int(input("Enter Money to Withdraw :"))
    s_code=int(input("Enter Your PIN :"))
    if w_money <= Balance :
        Balance-=w_money
        print("Withdrawl Successfully Completed.Remaining Balance :",Balance)
    else :
        print(f"Insufficient Balance. Available Balance {Balance}")
    

def Check() :
    print("Your Total Balance :",Balance)

def login():
        id=int(input("Enter Your Account Number :"))
        password=int(input("Enter Your PassWord :"))
        if id in Account and Account[id] == password :
            print("Login Successful.\n")
            l_info()
    
        else :
            print("User Not Found! Please Create a New Account.\n")
            main()

def create():
    new_id=int(input("Create a Account Number :"))
    new_pass=int(input("Create Your PassWord :"))
    code=int(input("Create Your Secret Pin : "))
    Account[new_id]=new_pass
    print("Account Created Successfully.\n")

def main() :
        while True :
            Display()
            try :
                choice=int(input("Enter Your Choice :"))
                if choice == 1 :
                    login()
                elif choice == 2 :
                    create()
                elif choice == 3 :
                    print("Good Bye!!")
                    break
                else :
                    print("invalid choice. Please Enter Valid Option.")
            except ValueError :
                print("Invalid input ")

if __name__=="__main__" :
    main()