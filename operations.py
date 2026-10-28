
class BankAccount:
    def __init__(self,name:str,Balance:float = 0) -> None:
        self.Name = name
        self.Balance = Balance

    def show_methods(self):
        print("\n1.) Deposite Money")
        print("2.) Withdraw Money")
        print("3.)SHOW CURRENT BALANCE")
        print("4.)SHOW DETAILS")
        print("5.)EXIT")


    def deposit(self):
        try:
            Amount = int(input("\nENTER THE AMOUNT YOU WANT TO DEPOSIT:"))
        except ValueError as e:
            print(e)

        if Amount > 0:
            self.Balance += Amount
            print(f"{Amount} IS ADDED TO YOUR ACCOUNT")
        else:
            print("ENTER A VALID POSTIVE AMOUNT")

    def withdraw(self):
        try:
            Amount = int(input("\nENTER THE AMOUNT YOU WANT TO WITHDRAW:"))
        except ValueError as e:
            print(e)

        if Amount > 0:
            if self.Balance >= Amount:
                self.Balance -= Amount
                print(f"{Amount} IS WITHDRAWN FROM YOUR ACCOUNT")
            else:
                print("BALANCE INSUFFICIENT")
        else:
            print("ENTER A VALID AMOUNT")

    def display_balance(self):
        print(f"YOUR CURRENT ACCOUNT BALANCE IS {self.Balance}")

    def display_details(self):
        print(f"YOUR USERNAME IS {self.Name}")
        print(f"YOUR CURRENT ACCOUNT BALANCE IS {self.Balance}")



