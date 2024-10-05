class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited: ${amount:.2f}")
            self.check_balance()
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew: ${amount:.2f}")
            self.check_balance()
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount.")

    def menu(self):
        while True:
            print("\nWelcome to the ATM!")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            
            choice = input("Select an option (1-4): ")

            if choice == '1':
                self.check_balance()

            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)

            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)

            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice! Please select a valid option.")

# Start the ATM simulation
if __name__ == "__main__":
    atm = ATM()
    atm.menu()
