from variables import display_b,deposit,withdraw,show_state
def main():
    print("\n ________________________________________")
    
    print("       Welcome to ISSA'S ATM      ")
    print("  _________________________________________")

    while True:
        print("  1. Display Balance")
        print("  2. Deposit Money")
        print("  3. Withdraw Money")
        print("  4. Transaction Statement")
        print("  5. Exit")
        print("  _________________________________")

        choice = input("  Enter your choice (1-5): ")

        if choice == "1":
            display_b()

        elif choice == "2":
                amount = float(input("  Enter deposit amount: Rs. "))
                deposit(amount)

        elif choice == "3":
                amount = float(input("  Enter withdrawal amount: Rs."))
                withdraw(amount)
        elif choice == "4":
            show_state()

        elif choice == "5":
            print("\n Thank You for using ISSA'S ATM !\n")
            break

        else:
            print("  Invalid choice. Please select 1–5.")
main()